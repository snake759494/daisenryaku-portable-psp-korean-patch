import struct
from PIL import Image
import gim
def blocks(d,off,end):
    while off<end:
        bid,_,size,nxt,doff=struct.unpack_from('<HHIII',d,off)
        yield bid,off,size,doff
        if bid in (2,3): yield from blocks(d,off+doff,off+size); break
        if nxt==0: break
        off+=nxt
def info(d):
    """returns dict with image header offset, pixel offset etc."""
    r={}
    for bid,off,size,doff in blocks(d,0x10,len(d)):
        if bid in (4,5):
            h=off+doff
            hl,_,fmt,order,w,hh=struct.unpack_from('<HHHHHH',d,h)
            pitch_al,=struct.unpack_from('<H',d,h+0xe)
            pix=h+struct.unpack_from('<I',d,h+0x1c)[0]
            k='img' if bid==4 else 'pal'
            if k in r: continue
            r[k]=dict(h=h,fmt=fmt,order=order,w=w,hgt=hh,pix=pix,end=off+size)
    return r
BPP={0:16,1:16,2:16,3:32,4:4,5:8}
def stride(w,fmt): 
    b=w*BPP[fmt]//8; return (b+15)//16*16
def decode(d):
    I=info(d); im=I['img']; fmt=im['fmt']; w,h=im['w'],im['hgt']
    st=stride(w,fmt); hp=(h+7)//8*8
    raw=d[im['pix']:im['pix']+st*hp]
    if len(raw)<st*hp: raw=raw+b'\0'*(st*hp-len(raw))
    if im['order']==1: raw=gim.unswizzle(raw,st,hp)
    def col(fmt,v):
        if fmt==3: return v
        if fmt==0: return ((v&31)*255//31,((v>>5)&63)*255//63,((v>>11)&31)*255//31,255)
        if fmt==1: return ((v&31)*255//31,((v>>5)&31)*255//31,((v>>10)&31)*255//31,255 if v>>15 else 0)
        if fmt==2: return ((v&15)*17,((v>>4)&15)*17,((v>>8)&15)*17,(v>>12)*17)
    out=Image.new('RGBA',(w,h))
    P=out.load()
    if fmt in (4,5):
        pl=I['pal']; pf=pl['fmt']; n=pl['w']
        pal=[]
        for i in range(max(n,256 if fmt==5 else 16)):
            if i<n:
                if pf==3: pal.append(tuple(d[pl['pix']+4*i:pl['pix']+4*i+4]))
                else: pal.append(col(pf,struct.unpack_from('<H',d,pl['pix']+2*i)[0]))
            else: pal.append((0,0,0,0))
        for y in range(h):
            row=raw[y*st:(y+1)*st]
            for x in range(w):
                v=row[x] if fmt==5 else (row[x>>1]>>(4*(x&1)))&15
                P[x,y]=pal[v]
    else:
        bp=BPP[fmt]//8
        for y in range(h):
            for x in range(w):
                o=y*st+x*bp
                v=d[o] if False else int.from_bytes(raw[o:o+bp],'little')
                P[x,y]=tuple(raw[o:o+4]) if fmt==3 else col(fmt,v)
    return out
