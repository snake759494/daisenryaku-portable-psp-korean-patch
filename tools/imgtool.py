"""Image-text replacement for GIM textures inside *_ash containers.
spec job: [x,y,w,h,text,{opts}]  opts: font(sans|bold|serif|pixel|pixelb) size align(l|c|r) fill outline shadow bg(keep|row|col|clear|color) sx(min hscale) dy
"""
import os,sys,json,struct
import numpy as np
from PIL import Image,ImageDraw,ImageFont,ImageFilter
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
import gim,gimfile,cont,lzss
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SP=os.environ.get('IMG_PREVIEW_DIR','preview/')
FONTS={'sans':'NanumSquareNeo-cBd.ttf','bold':'NanumSquareNeo-dEb.ttf','heavy':'NanumSquareNeo-eHv.ttf','reg':'NanumSquareNeo-bRg.ttf',
       'serif':'SeoulHangangEB.ttf','serifb':'SeoulHangangB.ttf','pixel':'fonts/Galmuri11.ttf','pixelb':'fonts/Galmuri11-Bold.ttf','pixel9':'fonts/Galmuri9.ttf'}
class Tex:
    def __init__(s,b):
        s.b=bytearray(b); I=gimfile.info(s.b); s.I=I; im=I['img']
        s.w,s.h=im['w'],im['hgt']; s.st=gimfile.stride(s.w,im['fmt']); s.hp=(s.h+7)//8*8; s.fmt=im['fmt']
        raw=bytes(s.b[im['pix']:im['pix']+s.st*s.hp])
        if im['order']==1: raw=gim.unswizzle(raw,s.st,s.hp)
        assert s.fmt==5
        s.idx=np.frombuffer(raw,np.uint8).reshape(s.hp,s.st)[:,:s.w].copy(); s.orig=s.idx.copy()
        pl=I['pal']; n=pl['w']
        s.pal=np.array([list(s.b[pl['pix']+4*i:pl['pix']+4*i+4]) for i in range(n)]+[[0,0,0,0]]*(256-n),np.float64)
        s.pals=[]
        import struct as _st
        b=bytes(s.b)
        def walk(off,end):
            while off<end:
                bid,_,size,nxt,doff=_st.unpack_from('<HHIII',b,off)
                if bid==5:
                    hh=off+doff; w_=_st.unpack_from('<H',b,hh+8)[0]; px=hh+_st.unpack_from('<I',b,hh+0x1c)[0]
                    s.pals.append(np.array([list(b[px+4*i:px+4*i+4]) for i in range(w_)]+[[0,0,0,0]]*(256-w_),np.float64))
                if bid in (2,3): walk(off+doff,off+size); return
                if nxt==0: return
                off+=nxt
        walk(0x10,len(b))
    def rgba(s): return s.pal[s.idx]
    def save_back(s):
        im=s.I['img']; full=np.zeros((s.hp,s.st),np.uint8); full[:,:s.w]=s.idx
        raw=full.tobytes()
        if im['order']==1: raw=gim.swizzle(raw,s.st,s.hp)
        s.b[im['pix']:im['pix']+len(raw)]=raw
        return bytes(s.b)
    def quant(s,rgba,allowed=None):
        """rgba: (h,w,4) float -> indices, nearest palette entry (alpha weighted)"""
        ids=np.arange(256) if allowed is None else np.array(sorted(allowed))
        P=s.pal[ids]; flat=rgba.reshape(-1,4)
        a=flat[:,3:4]/255.; pa=P[:,3:4].T/255.
        # premultiplied distance + alpha
        d=((flat[:,None,:3]*a[:,:,None]-P[None,:,:3]*pa[:,:,None])**2).sum(-1)+((flat[:,None,3]-P[None,:,3])**2)*1.0
        return ids[d.argmin(1)].astype(np.uint8).reshape(rgba.shape[:2])
def font(name,size): return ImageFont.truetype(os.path.join(ROOT,FONTS[name]),size)
GAL=[('Galmuri14.ttf',15),('Galmuri11.ttf',12),('Galmuri9.ttf',10)]
GAL_LOG=[]
GAL_SLACK=[0,0]
GAL_OVER=[False]
GAL_START=[0]
def _gal_render(text,fn,sz,k):
    F=ImageFont.truetype(os.path.join(ROOT,'fonts',fn),sz); F.fontmode='1'
    lines=text.split(chr(10)); bbs=[F.getbbox(l) if l else (0,0,0,0) for l in lines]
    top=min(b[1] for b in bbs if b[3]); bot=max(b[3] for b in bbs if b[3]); lh=bot-top+1
    tw=max(b[2] for b in bbs)
    im=Image.new('L',(tw+2,lh*len(lines)),0); dr=ImageDraw.Draw(im); dr.fontmode='1'
    for i,l in enumerate(lines): dr.text((0,i*lh-top),l,font=F,fill=255)
    bb=im.getbbox()
    if not bb: return None
    im=im.crop((bb[0],0,bb[2],lh*len(lines)-1))
    if k>1: im=im.resize((im.width*k,im.height*k),Image.NEAREST)
    return im,lines
def gal_mask(text,w,h,align='c',dy=0,maxk=4):
    best=None
    for k in range(maxk,0,-1):
        for fn,sz in GAL[GAL_START[0]:]:
            r=_gal_render(text,fn,sz,k)
            if r is None: return np.zeros((h,w))
            im,lines=r
            if im.height<=h and im.width<=w: best=im; break
        if best is not None: break
    if best is None and ' ' in text:
        return gal_mask(text.replace(' ',''),w,h,align,dy,maxk)
    if best is None:
        best=_gal_render(text,'Galmuri9.ttf',10,1)[0]; GAL_OVER[0]=True
        if best.width>w+GAL_SLACK[0] or best.height>h+GAL_SLACK[1]: GAL_LOG.append((text,w,h,best.width,best.height))
    a=(np.asarray(best,float)>127).astype(float); nh,nw=a.shape
    m=np.zeros((h,w)); ox={'l':0,'c':(w-nw)//2,'r':w-nw}[align]; oy=(h-nh)//2+dy
    ys0,xs0=max(0,oy),max(0,ox); ys1,xs1=min(h,oy+nh),min(w,ox+nw)
    m[ys0:ys1,xs0:xs1]=a[ys0-oy:ys1-oy,xs0-ox:xs1-ox]
    return m
def render_mask(text,fnt,size,w,h,align='c',sxmin=0.6,dy=0,spacing=0):
    return gal_mask(text,w,h,align,dy)
def _old_render_mask(text,fnt,size,w,h,align='c',sxmin=0.6,dy=0,spacing=0):
    f=font(fnt,size)
    lines=text.split('\n'); lh=size+spacing
    bbs=[f.getbbox(l) for l in lines]
    tw=max(b[2]-min(0,b[0]) for b in bbs); 
    big=Image.new('L',(max(tw,1)+8,lh*len(lines)+size),0); dr=ImageDraw.Draw(big)
    for i,l in enumerate(lines):
        bw=f.getbbox(l)[2]
        x=4+{'l':0,'c':(tw-bw)//2,'r':tw-bw}[align]
        dr.text((x,i*lh),l,font=f,fill=255)
    bb=big.getbbox()
    if not bb: return np.zeros((h,w))
    # vertical extent based on font metrics, horizontal on ink
    asc,desc=f.getmetrics()
    top=min(f.getbbox(l)[1] for l in lines if l) ; bot=max(f.getbbox(l)[3] for l in lines if l)+(len(lines)-1)*lh
    crop=big.crop((bb[0],top,bb[2],bot))
    cw,ch=crop.size
    sx=min(1.0,w/cw); sy=1.0
    if ch>h: sy=h/ch
    if sx<sxmin:  # too wide even after squeeze: shrink uniformly
        k=w/(cw*sxmin); sx=sxmin*k*1.0; sy=min(sy,k) if True else sy
        sx=w/cw
    nw=max(1,int(round(cw*sx))); nh=max(1,int(round(ch*sy)))
    crop=crop.resize((nw,nh),Image.LANCZOS)
    m=np.zeros((h,w))
    ox={'l':0,'c':(w-nw)//2,'r':w-nw}[align]; oy=(h-nh)//2+dy
    ys,xs=max(0,oy),max(0,ox)
    sub=np.asarray(crop,float)/255
    m[ys:ys+nh,xs:xs+nw]=sub[ys-oy:ys-oy+min(nh,h-ys),xs-ox:xs-ox+min(nw,w-xs)][:h-ys,:w-xs]
    return m
def lum(c): return 0.299*c[...,0]+0.587*c[...,1]+0.114*c[...,2]
def analyze(box):
    """box rgba (h,w,4) -> bg estimate per pixel, fill color, outline color(or None)"""
    h,w,_=box.shape
    left=box[:,0]; right=box[:,-1]
    t=np.linspace(0,1,w)[None,:,None]
    bg=left[:,None,:]*(1-t)+right[:,None,:]*t
    diff=np.abs(box-bg).sum(-1)
    txt=diff>60
    return bg,txt
def apply_job(T,job,debug=False):
    x,y,w,h,text=job[:5]; o=job[5] if len(job)>5 else {}
    if text is None: T.idx[y:y+h,x:x+w]=T.orig[y:y+h,x:x+w]; return {}
    if o.get('overlay'):
        # subtitle drawn over a photo: keep background, quantize to the whole palette
        R=T.rgba()[y:y+h,x:x+w].astype(float)
        im=Image.new('L',(w,h)); dr=ImageDraw.Draw(im)
        f=font(o.get('font','heavy'),o.get('size',22))
        al=o.get('align','r'); px={'l':4,'c':w//2,'r':w-4}[al]
        dr.text((px,h//2),text,font=f,fill=255,anchor={'l':'lm','c':'mm','r':'rm'}[al])
        m=np.asarray(im,float)/255
        om=np.asarray(im.filter(ImageFilter.MaxFilter(2*o.get('ow',2)+1)).filter(ImageFilter.GaussianBlur(0.6)),float)/255
        out=R*(1-om[...,None])+np.array(o.get('outline',[45,35,30,255]),float)*om[...,None]
        out=out*(1-m[...,None])+np.array(o.get('fill',[250,248,240,255]),float)*m[...,None]
        T.idx[y:y+h,x:x+w]=T.quant(out,None); return {}
    if o.get('autoix') and 'ix' not in o:
        # labels drawn with their own (alpha) palette: keep transparent bg index, reuse original fill/outline indices
        from scipy import ndimage as nd
        ob=T.orig[y:y+h,x:x+w]; cnt=np.bincount(ob.ravel(),minlength=256); bgi=int(cnt.argmax())
        cands=[(int((P[np.nonzero(cnt)[0],3]>200).sum()),k) for k,P in enumerate(T.pals) if P[bgi,3]<40]
        if cands:
            P=T.pals[max(cands)[1]]
            ink=(ob!=bgi)&(P[ob,3]>100)
            if ink.sum()>8:
                adj=ink&nd.binary_dilation(~ink)
                lum_=P[:,:3].mean(1)
                inn=ob[ink&~adj] if (ink&~adj).any() else ob[ink]
                ic=np.bincount(inn,minlength=256); c_=np.nonzero(ic>=max(1,0.08*ic.sum()))[0]
                if not len(c_): c_=np.nonzero(np.bincount(ob[ink],minlength=256))[0]
                fi=int(c_[np.argmax(lum_[c_])])
                ac=np.bincount(ob[adj],minlength=256); a_=np.nonzero(ac>=max(1,0.08*ac.sum()))[0]
                oi=int(a_[np.argmin(lum_[a_])]) if len(a_) else fi
                ix={'bg':bgi,'fill':fi}
                if abs(lum_[fi]-lum_[oi])>40: ix['outline']=oi
                o=dict(o,ix=ix,ow=o.get('ow',1)); job=list(job[:5])+[o]
    if o.get('uni') and o.get('gen'):
        return uni_apply(T,job)
    if o.get('uni'):
        ob=T.orig[y:y+h,x:x+w]; bgi=int(np.bincount(np.concatenate([ob[0],ob[-1],ob[:,0],ob[:,-1]])).argmax())
        ink=ob==255; rows=np.nonzero(ink.any(1))[0]
        top=rows.min() if len(rows) else 0
        fn,sz=o.get('gal',('Galmuri11.ttf',12)); r=_gal_render(text,fn,sz,1)
        if r[0].width>w: r=_gal_render(text.replace(' ',''),fn,sz,1)
        if r[0].width>w: r=_gal_render(text,'Galmuri9.ttf',10,1); GAL_LOG.append(('uni-shrink',text,w))
        a=np.asarray(r[0])>127; nh,nw=a.shape
        oy=(o['ty']-y if 'ty' in o else top)+o.get('dy',0); oy=max(0,min(oy,h-nh)); cols=np.nonzero(ink.any(0))[0]
        ox=min(int(cols.min()) if len(cols) else 0,max(0,w-nw))+o.get('dx',0) if o.get('align','L')=='L' else {'l':0,'c':(w-nw)//2,'r':w-nw}[o.get('align')]
        if nh>h or nw>w: GAL_LOG.append(('uni-clip',text,w,h,nw,nh))
        ox=max(0,ox); bx=np.full((h,w),bgi,T.idx.dtype); sub=a[:h-oy,:w-ox]
        bx[oy:oy+sub.shape[0],ox:ox+sub.shape[1]][sub]=o.get('fillidx',255)
        T.idx[y:y+h,x:x+w]=bx
        for cx0,cy0,cx1,cy1 in o.get('clr',[]): T.idx[cy0:cy1,cx0:cx1]=bgi
        return {}
    if o.get('auto'):
        from scipy import ndimage as nd
        ob=T.orig[y:y+h,x:x+w]; bgi=o.get('bgidx',int(np.bincount(np.concatenate([ob[0],ob[-1],ob[:,0],ob[:,-1]])).argmax()))
        fi=o.get('fillidx',255); ink=ob==fi
        if ink.sum()>4:
            ring=nd.binary_dilation(ink)&~ink&(ob!=bgi)
            oi=int(np.bincount(ob[ring]).argmax()) if ring.any() else bgi
            ys,xs=np.nonzero(ink); y0,y1,x0,x1=ys.min(),ys.max()+1,xs.min(),xs.max()+1
            # clear whole box to bg, then draw into ink bbox (+1 for outline)
            T.idx[y:y+h,x:x+w]=np.where(ob==bgi,ob,bgi)
            nx,ny=x+max(x0-1,0),y+max(y0-1,0); nw=min(x1+1,w)-max(x0-1,0); nh=min(y1+1,h)-max(y0-1,0)
            th=y1-y0; fnt='sans' if th>=14 else ('pixel' if th>=10 else 'pixel9'); sz=th+2 if th>=14 else (12 if th>=10 else 10)
            o2=dict(font=o.get('font',fnt),size=o.get('size',sz),fit=False,ow=1,gstart=o.get('gstart',0),align=o.get('align','c'),dy=o.get('dy',0),ix=({'bg':bgi,'fill':fi} if o.get('noout') else {'bg':bgi,'fill':fi,'outline':oi}))
            return _apply(T,job,x,ny,w,nh,text,o2)
    P0=T.pal
    if 'pal' in o: T.pal=T.pals[o['pal']]
    try: return _apply(T,job,x,y,w,h,text,o)
    finally: T.pal=P0
def _apply(T,job,x,y,w,h,text,o):
    GAL_START[0]=o.get('gstart',0)
    try: return _apply2(T,job,x,y,w,h,text,o)
    finally: GAL_START[0]=0
def _apply2(T,job,x,y,w,h,text,o):
    R=T.rgba()
    box=R[y:y+h,x:x+w].copy()
    bgmode=o.get('bg','row')
    if bgmode=='row':
        bg,txt=analyze(box)
    elif bgmode=='outside':
        L_=R[y:y+h,max(0,x-2)]; Rr=R[y:y+h,min(T.w-1,x+w+1)]; t_=np.linspace(0,1,w)[None,:,None]
        bg=L_[:,None,:]*(1-t_)+Rr[:,None,:]*t_; txt=np.abs(box-bg).sum(-1)>60
    elif bgmode=='edge':
        ib=T.idx[y:y+h,x:x+w]; e=np.concatenate([ib[0],ib[-1],ib[:,0],ib[:,-1]]); m_=np.bincount(e).argmax()
        bg=np.zeros_like(box)+T.pal[m_]; txt=np.abs(box-bg).sum(-1)>60
    elif bgmode=='mode':
        ib=T.idx[y:y+h,x:x+w]; m_=np.bincount(ib.ravel()).argmax()
        bg=np.zeros_like(box)+T.pal[m_]; txt=np.abs(box-bg).sum(-1)>60
    elif bgmode=='rowmed':
        thr=o.get('thr',100); L=lum(box); bg=np.zeros_like(box)
        for r in range(h):
            sel=box[r][L[r]>thr]
            bg[r]=np.median(sel,0) if len(sel) else box[r].mean(0)
        txt=np.abs(box-bg).sum(-1)>60
    elif bgmode=='lcol':
        bg=np.repeat(box[:,:1],w,1); txt=np.abs(box-bg).sum(-1)>60
    elif bgmode=='col':
        top=box[0]; bot=box[-1]; t=np.linspace(0,1,h)[:,None,None]
        bg=top[None]*(1-t)+bot[None]*t; txt=np.abs(box-bg).sum(-1)>60
    elif bgmode=='clear':
        bg=np.zeros_like(box); txt=box[...,3]>40
    elif bgmode=='keep':
        bg=box.copy(); txt=np.zeros(box.shape[:2],bool)
    else:
        bg=np.zeros_like(box)+np.array(bgmode,float); txt=np.abs(box-bg).sum(-1)>60
    # colors
    if 'fill' in o: fill=np.array(o['fill'],float)
    else:
        tp=box[txt]
        if len(tp)==0: fill=np.array([255,255,255,255.])
        else:
            L=lum(tp); bl=lum(bg[txt])
            # fill = text pixels farthest from bg luminance direction of majority
            sign=np.sign(np.median(L-bl)) or 1
            score=(L-bl)*sign
            sel=tp[score>=np.percentile(score,70)]
            fill=np.median(sel,0)
    outline=o.get('outline','auto')
    if outline=='auto':
        outline=None
        tp=box[txt]
        if len(tp)>20:
            d=np.abs(tp-fill).sum(-1)
            far=tp[d>150]
            bgl=np.median(lum(bg[txt]))
            if len(far)>0.25*len(tp):
                c=np.median(far,0)
                if abs(lum(c)-bgl)>40: outline=c
    elif outline is not None: outline=np.array(outline,float)
    size=o.get('size',h)
    fn=o.get('font','sans')
    if fn in('pixel','pixelb') and font(fn,12).getbbox(text)[2]>w-1: fn='pixel9'; size=min(size,10)
    hasol=(outline is not None) or ('outline' in o.get('ix',{})) or o.get('xfer')
    q=o.get('ow',1) if hasol else 0
    q=q+o.get('pad',0)
    qy=(o.get('ow',1) if hasol else 0)
    GAL_SLACK[0]=2*q; GAL_SLACK[1]=2*qy
    GAL_OVER[0]=False
    mk=o.get('maxk',4 if h>=30 else 1)
    # vertical target = original ink rows (so the new glyphs never exceed the old ones)
    ty0,th_=0,h
    if chr(10) not in text and not o.get('fullh'):
        ob=T.orig[y:y+h,x:x+w]; bm=np.bincount(np.concatenate([ob[0],ob[-1],ob[:,0],ob[:,-1]])).argmax()
        rows=np.nonzero((ob!=bm).sum(1)>0)[0]
        if len(rows) and rows[-1]-rows[0]+1>=8 and rows[-1]-rows[0]+1<h:
            ty0=max(0,rows[0]-qy+ (1 if qy else 0)); th_=min(h-ty0,rows[-1]-rows[0]+1+ (0 if qy else 0))
            ty0=max(0,rows[0]-0); th_=min(h-ty0,rows[-1]-rows[0]+1)
    mi=gal_mask(text,max(1,w-2*q),max(1,th_-2*qy),o.get('align','c'),0,mk)
    oy0=min(h-mi.shape[0],max(0,ty0+qy+o.get('dy',0)))
    if GAL_OVER[0]:
        q=qy=0; oy0=0; mi=gal_mask(text,w,h,o.get('align','c'),o.get('dy',0),mk)
    m=np.zeros((h,w)); m[oy0:oy0+mi.shape[0],q:q+mi.shape[1]]=mi
    if False:
        ob=T.orig[y:y+h,x:x+w]
        if o.get('xfer') or 'ix' in o:
            e=np.concatenate([ob[0],ob[-1],ob[:,0],ob[:,-1]]); ink=ob!=np.bincount(e).argmax()
        else: ink=txt
        ys_,xs_=np.where(ink)
        if len(ys_)>8:
            k=o.get('ow',1) if (outline is not None or 'outline' in o.get('ix',{}) or o.get('xfer')) else 0
            y0,y1=ys_.min()+k,ys_.max()+1-k; x0,x1=xs_.min()+k,xs_.max()+1-k
            if 'pad' in o: x0=max(x0,o['pad']); x1=min(x1,w-o['pad'])
            th,tw=y1-y0,x1-x0
            if th>=6 and tw>=6:
                pix=fn in('pixel','pixelb','pixel9')
                sz=size if pix else max(size,th*2)
                mm=render_mask(text,fn,sz,tw,th,o.get('align','c'),o.get('sx',0.6),0,0)
                m=np.zeros((h,w)); m[y0:y1,x0:x1]=mm
    if o.get('hard',True): m=(m>0.45).astype(float)
    if o.get('xfer'):
        from scipy import ndimage as nd
        ib=T.orig[y:y+h,x:x+w]
        bi=int(o['xfer_bg']) if 'xfer_bg' in o else int(np.bincount(np.concatenate([ib[0],ib[-1],ib[:,0],ib[:,-1]])).argmax())
        isbg=ib==bi; dist=nd.distance_transform_edt(~isbg)
        ring=(dist>0)&(dist<=o.get('ring',1.5)); inner=dist>=o.get('inner',3)
        oi=int(np.bincount(ib[ring]).argmax()) if ring.any() else bi
        rowf=[]
        for r in range(h):
            v=ib[r][inner[r]]; v=v[(v!=oi)&(v!=bi)]
            rowf.append(int(np.bincount(v).argmax()) if len(v) else -1)
        known=[r for r in range(h) if rowf[r]>=0]
        for r in range(h):
            if rowf[r]<0: rowf[r]=rowf[min(known,key=lambda k:abs(k-r))] if known else oi
        k=o.get('ow',1)
        om=np.asarray(Image.fromarray((m*255).astype(np.uint8)).filter(ImageFilter.MaxFilter(2*k+1)),float)/255
        res=np.full((h,w),bi,np.uint8); res[om>0.5]=oi
        fm=m>0.5
        for r in range(h): res[r][fm[r]]=rowf[r]
        T.idx[y:y+h,x:x+w]=res
        return dict(bg=bi,outline=oi)
    if 'ix' in o:
        ix=o['ix']; k=o.get('ow',1)
        if ix.get('bg')=='rowmode':
            ob2=T.orig[y:y+h,x:x+w]; res=np.zeros((h,w),np.uint8)
            for r in range(h):
                v=ob2[r][(ob2[r]!=ix['fill'])&(ob2[r]!=ix.get('outline',-1))&~np.isin(ob2[r],ix.get('excl',[]))]
                res[r]=np.bincount(v).argmax() if len(v) else ob2[r][0]
        elif isinstance(ix.get('bg'),dict):
            g=ix['bg']; res=np.zeros((h,w),np.uint8)
            for r in range(h):
                ph=(y+r-g['phase'])%g['period']; src=g['grid'] if ph==0 else (g.get('pre',g['norm']) if ph==g['period']-1 else g['norm'])
                res[r]=g['gridval'] if (ph==0 and 'gridval' in g) else T.orig[src,x:x+w]
        elif ix.get('bg')=='inpaint':
            from scipy import ndimage as nd
            res=T.orig[y:y+h,x:x+w].copy(); txt=np.isin(res,ix['excl']); txt=nd.binary_dilation(txt,iterations=ix.get('grow',1))
            for r in range(h):
                ok=np.nonzero(~txt[r])[0]
                if not len(ok): continue
                for c in np.nonzero(txt[r])[0]: res[r,c]=res[r,ok[np.abs(ok-c).argmin()]]
        elif ix.get('bg')=='boxmode':
            ob2=T.orig[y:y+h,x:x+w].ravel(); v=ob2[(ob2!=ix['fill'])&(ob2!=ix.get('outline',-1))]
            res=np.full((h,w),np.bincount(v).argmax(),np.uint8)
        else: res=np.full((h,w),ix['bg'],np.uint8) if 'bg' in ix else T.idx[y:y+h,x:x+w].copy()
        if 'outline' in ix:
            om=np.asarray(Image.fromarray((m*255).astype(np.uint8)).filter(ImageFilter.MaxFilter(2*k+1)),float)/255
            res[om>0.5]=ix['outline']
        if ix.get('ramp'):
            b0=ix['bg']; sel=m>0.08; res[sel]=np.clip(np.round(b0+m[sel]*(ix['fill']-b0)),0,255).astype(np.uint8)
        else: res[m>0.5]=ix['fill']
        T.idx[y:y+h,x:x+w]=res
        return {}
    out=bg.copy()
    if outline is not None:
        k=o.get('ow',1)
        mi=Image.fromarray((m*255).astype(np.uint8)).filter(ImageFilter.MaxFilter(2*k+1))
        om=np.asarray(mi,float)/255
        out=out*(1-om[...,None])+np.array(outline,float)*om[...,None]
    if o.get('shadow'):
        sh=np.zeros_like(m); sh[1:,1:]=m[:-1,:-1]
        sc=np.array(o['shadow'],float)
        out=out*(1-sh[...,None])+sc*sh[...,None]
    out=out*(1-m[...,None])+fill*m[...,None]
    q=T.quant(out,set(np.unique(T.idx[y:y+h,x:x+w]).tolist()) if o.get('restrict',True) else None)
    T.idx[y:y+h,x:x+w]=q
    return dict(fill=fill.round().tolist(),outline=None if outline is None else np.round(outline).tolist())
def load_container(path):
    d=open(path,'rb').read()
    if path.endswith('_ash.dat'): d=lzss.decompress(d)
    return d
def grid(img,x,y,w,h,scale=4,step=8,name='grid.png'):
    """save zoomed crop with grid & coordinates"""
    im=img.crop((x,y,x+w,y+h)); bg=Image.new('RGBA',im.size,(60,90,60,255)); bg.alpha_composite(im)
    big=bg.convert('RGB').resize((w*scale,h*scale),Image.NEAREST); dr=ImageDraw.Draw(big)
    f=ImageFont.truetype('arial.ttf',10)
    for gx in range((x//step+1)*step,x+w,step):
        X=(gx-x)*scale; dr.line([(X,0),(X,h*scale)],fill=(255,0,255) if gx%32==0 else (120,0,120))
        if gx%32==0: dr.text((X+1,0),str(gx),fill=(255,255,0),font=f)
    for gy in range((y//step+1)*step,y+h,step):
        Y=(gy-y)*scale; dr.line([(0,Y),(w*scale,Y)],fill=(255,0,255) if gy%32==0 else (120,0,120))
        if gy%32==0: dr.text((0,Y+1),str(gy),fill=(255,255,0),font=f)
    big.save(SP+name)

def expand_jobs(T,jobs,maxgrow=4,maxcomp=600):
    """grow each box to cover small original-ink components (index 255 or job fill) that stick out of it"""
    from scipy import ndimage as nd
    H,W=T.orig.shape
    boxes=[list(j[:4]) for j in jobs]
    out=[]
    for k,j in enumerate(jobs):
        x,y,w,h,t=j[:5]; o=j[5] if len(j)>5 else {}
        if t is None or o.get('noexpand'): out.append(j); continue
        fi={255}
        if 'ix' in o and isinstance(o['ix'].get('fill'),int): fi.add(o['ix']['fill'])
        x0,y0=max(0,x-maxgrow-1),max(0,y-maxgrow-1); x1,y1=min(W,x+w+maxgrow+1),min(H,y+h+maxgrow+1)
        reg=T.orig[y0:y1,x0:x1]; ink=np.isin(reg,list(fi))
        lab,n=nd.label(ink,structure=np.ones((3,3)))
        bx=np.zeros_like(ink); bx[y-y0:y-y0+h,x-x0:x-x0+w]=True
        nx0,ny0,nx1,ny1=x,y,x+w,y+h
        for i in set(np.unique(lab[bx&ink]))-{0}:
            comp=lab==i
            if comp.sum()>maxcomp: continue
            ys,xs=np.nonzero(comp)
            cx0,cy0,cx1,cy1=xs.min()+x0,ys.min()+y0,xs.max()+x0+1,ys.max()+y0+1
            if cx0<x-maxgrow or cy0<y-maxgrow or cx1>x+w+maxgrow or cy1>y+h+maxgrow: continue
            nx0,ny0,nx1,ny1=min(nx0,cx0-1),min(ny0,cy0-1),max(nx1,cx1+1),max(ny1,cy1+1)
        nx0,ny0=max(0,nx0),max(0,ny0); nx1,ny1=min(W,nx1),min(H,ny1)
        # don't intrude into other boxes
        for m,(bx_,by_,bw_,bh_) in enumerate(boxes):
            if m==k: continue
            if bx_<nx1 and bx_+bw_>nx0 and by_<ny1 and by_+bh_>ny0 and not (bx_<x+w and bx_+bw_>x and by_<y+h and by_+bh_>y):
                # overlap introduced: trim along the axis it came from
                if bx_>=x+w: nx1=min(nx1,bx_)
                elif bx_+bw_<=x: nx0=max(nx0,bx_+bw_)
                elif by_>=y+h: ny1=min(ny1,by_)
                elif by_+bh_<=y: ny0=max(ny0,by_+bh_)
        out.append([nx0,ny0,nx1-nx0,ny1-ny0,t]+list(j[5:]))
    return out

def uni_info(T,job):
    x,y,w,h,t=job[:5]; o=job[5] if len(job)>5 else {}
    ob=T.orig[y:y+h,x:x+w]; e=np.concatenate([ob[0],ob[-1],ob[:,0],ob[:,-1]]); bgi=o.get('bgidx',int(np.bincount(e).argmax()))
    ink=ob!=bgi; ys,xs=np.nonzero(ink)
    if not len(xs): return None
    fi=o.get('fillidx',255)
    fy=np.nonzero((ob==fi).any(1))[0]
    bb=(xs.min(),xs.max()+1,(fy.min() if len(fy) else ys.min()),(fy.max()+1 if len(fy) else ys.max()+1))
    return dict(bgi=bgi,uniform=1.0,fi=fi,bb=bb,L=x,R=x+w,ink=ink)
def uni_pick(text,bw,bh):
    for i,(fn,sz) in enumerate(GAL):
        for tt in (text,text.replace(' ','')):
            r=_gal_render(tt,fn,sz,1)
            if r[0].width<=bw and r[0].height<=bh: return i,tt
    return len(GAL)-1,text.replace(' ','')
def uni_apply(T,job):
    x,y,w,h,t=job[:5]; o=job[5]; inf=uni_info(T,job)
    if inf is None: return
    x0,x1,y0,y1=inf['bb']; bw,bh=x1-x0+o.get('xs',1),max(y1-y0+o.get('ys',1),11 if h>=12 else 9)
    fi,_=uni_pick(t,bw,bh); gi=max(o.get('gi',0),fi); fn,sz=GAL[gi]
    tt=t if _gal_render(t,fn,sz,1)[0].width<=bw else t.replace(' ','')
    a=np.asarray(_gal_render(tt,fn,sz,1)[0])>127; nh,nw=a.shape
    if nw>bw: GAL_LOG.append(('W',t,bw,nw))
    ox=x0 if o.get('align','L')=='L' else x0+(x1-x0-nw)//2
    oy=(o['ty']-y) if 'ty' in o else y0+(y1-y0-nh+1)//2
    oy=min(max(0,oy+o.get('dy',0)),h-nh)
    L,R=inf['L'],inf['R']; reg=T.idx[y:y+h,L:R]
    if inf['uniform']>=0.7: reg[inf['ink']]=inf['bgi']
    else: reg[T.orig[y:y+h,L:R]==inf['fi']]=inf['bgi']
    cur=T.idx[y:y+h,x:x+w]
    gx=x+ox+o.get('dx',0); T.idx[y+oy:y+oy+nh,gx:gx+nw][a[:h-oy]]=inf['fi']
    for c0,r0,c1,r1 in o.get('clr',[]): T.idx[r0:r1,c0:c1]=inf['bgi']
def uni_prepare(T,jobs):
    """mark eligible small single-line jobs as uni and unify font within (height-bin) groups"""
    out=[];grp={}
    for j in jobs:
        j=list(j); o=dict(j[5]) if len(j)>5 else {}
        x,y,w,h,t=j[:5]
        if t and chr(10) not in t and h<24 and not o.get('keep'):
            inf=uni_info(T,[x,y,w,h,t,o])
            if inf and (o.get('uni') or inf['uniform']>=0.7):
                o['uni']=True; x0,x1,y0,y1=inf['bb']
                fi,_=uni_pick(t,x1-x0+2,y1-y0+1); grp.setdefault(y1-y0,[]).append((fi,o))
        out.append(j[:5]+[o])
    for k,l in grp.items():
        fs=[f for f,_ in l]; g=max(set(fs),key=fs.count)
        for f,o in l: o.setdefault('gi',g)
    return out

def _bb(a,x,y,w,h):
    ob=a[y:y+h,x:x+w]; b=np.bincount(np.concatenate([ob[0],ob[-1],ob[:,0],ob[:,-1]])).argmax()
    ys,xs=np.nonzero(ob!=b); return (xs.min(),xs.max(),ys.min(),ys.max()) if len(xs) else None
def apply_fit(T,job):
    """apply job; if result spills outside the original text extent, retry with a smaller Galmuri, then shift into place"""
    x,y,w,h,t=job[:5]; o=dict(job[5]) if len(job)>5 else {}
    if t is None or chr(10) in t or h>=24 or o.get('nofit'): return apply_job(T,job)
    snap=T.idx[y:y+h,x:x+w].copy(); ob=_bb(T.orig,x,y,w,h)
    for gs in range(o.get('gstart',0),3):
        T.idx[y:y+h,x:x+w]=snap; o['gstart']=gs; apply_job(T,job[:5]+[o]); nb=_bb(T.idx,x,y,w,h)
        if not ob or not nb: return
        if nb[1]-nb[0]<=ob[1]-ob[0]+1: break
    dx=0
    if nb[0]<ob[0]-1: dx=ob[0]-nb[0]
    elif nb[1]>ob[1]+1: dx=ob[1]-nb[1]
    if dx and nb[1]-nb[0]<=ob[1]-ob[0]+1:
        bx=T.idx[y:y+h,x:x+w]; b=np.bincount(np.concatenate([bx[0],bx[-1],bx[:,0],bx[:,-1]])).argmax()
        r=np.roll(bx,dx,1)
        if dx>0: r[:,:dx]=b
        else: r[:,dx:]=b
        T.idx[y:y+h,x:x+w]=r

def fit_jobs(T,jobs):
    """decide one Galmuri size per style group (same style + height) so siblings match, then apply"""
    import copy
    need={}
    base=T.idx.copy()
    for j in jobs:
        x,y,w,h,t=j[:5]; o=j[5] if len(j)>5 else {}
        if t is None or chr(10) in t or h>=24 or o.get('nofit'): continue
        k=(repr(sorted((a,repr(b)) for a,b in o.items() if a not in('dy','ty','clr'))),h)
        ob=_bb(T.orig,x,y,w,h)
        for gs in range(o.get('gstart',0),3):
            T.idx[y:y+h,x:x+w]=base[y:y+h,x:x+w]; o2=dict(o,gstart=gs); apply_job(T,j[:5]+[o2]); nb=_bb(T.idx,x,y,w,h)
            if not ob or not nb or nb[1]-nb[0]<=ob[1]-ob[0]+1: break
        need[k]=max(need.get(k,0),gs)
        T.idx[y:y+h,x:x+w]=base[y:y+h,x:x+w]
    T.idx[:]=base
    for j in jobs:
        x,y,w,h,t=j[:5]; o=j[5] if len(j)>5 else {}
        if t is None or chr(10) in t or h>=24 or o.get('nofit'): apply_job(T,j); continue
        k=(repr(sorted((a,repr(b)) for a,b in o.items() if a not in('dy','ty','clr'))),h)
        apply_fit(T,j[:5]+[dict(o,gstart=need.get(k,0))])
