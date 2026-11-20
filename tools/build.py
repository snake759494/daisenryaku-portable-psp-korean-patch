"""한글 패치 빌드: python tools/build.py [--noiso]"""
import os,sys,json,glob,re,struct,shutil
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
import lzss,strfile,jtable,kfont,isobuild
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
W=lambda *p:os.path.join(ROOT,*p)
ORIG=W('Daisenryaku Portable (Japan) (v1.03).iso')
OUT=W('Daisenryaku Portable (Korean).iso')
USR='work/ext/PSP_GAME/USRDIR/'
def load_trans():
    ids=dict(json.load(open(W('work','trans','ja_list.json'),encoding='utf8')))
    T={}
    for f in sorted(glob.glob(W('work','trans','ko_*.json'))):
        for k,v in json.load(open(f,encoding='utf8')).items():
            T[ids[k] if k in ids else k]=v
    return T
def units(s):
    n=0
    for t in tokens(s):
        if isinstance(t,int): n+=1 if 0x80<=t<=0xbf else (0 if t==0x1ff else 2)
        else:
            c=kfont.SYM.get(t)
            n+=1 if (c is not None and 0x80<=c<=0xbf) else 2
    return n
def jaunits(s):
    return sum(1 if (isinstance(t,int) and 0x80<=t<=0xbf) else 2 for t in tokens(s) if t!=0x1ff)
def wrap(ja,ko):
    """ko starting with '#': auto wrap to the original layout (indent / separator / width)."""
    body=ko[1:]
    sep='{1FF}{1FF}' if '{1FF}{1FF}' in ja else '{1FF}'
    lines=[l for l in ja.split(sep)]
    ind='　' if all(l.startswith('　') for l in lines if l) else ''
    width=max(jaunits(l) for l in lines)-2*len(ind)
    out=[]
    for para in body.split(chr(10)):
        if para=='': out.append(''); continue
        cur=''
        for w in para.split(' '):
            cand=(cur+' '+w) if cur else w
            if units(cand)<=width: cur=cand
            else:
                if cur: out.append(cur)
                while units(w)>width:
                    t=list(tokens(w)); out.append(''.join(x if isinstance(x,str) else '{%X}'%x for x in t[:width])); w=''.join(x if isinstance(x,str) else '{%X}'%x for x in t[width:])
                cur=w
        out.append(cur)
    return sep.join(ind+l if l else '' for l in out)
LIM={15:12,21:12,12:3}
TAG=re.compile(r'\{([0-9A-Fa-f]+)\}')
def tokens(s):
    i=0
    while i<len(s):
        m=TAG.match(s,i)
        if m: yield int(m.group(1),16); i=m.end()
        else: yield s[i]; i+=1
def main():
    T=load_trans()
    raw=open(W('work','dec','STRING__string_ash.dat'),'rb').read()
    S=strfile.parse(raw)
    chars=set()
    for k,v in T.items():
        for t in tokens(v):
            if isinstance(t,str): chars.add(t)
    cmap=kfont.assign(chars)
    enc=dict(kfont.SYM); enc.update(cmap)
    warn=[]; used=0
    for si,ents in enumerate(S):
        for ei,e in enumerate(ents):
            ja=jtable.dec(e)
            if not ja or ja not in T: continue
            ko=T[ja]
            if ko.startswith('#'):
                ko=wrap(ja,ko)
                if ko.count('{1FF}')>max(ja.count('{1FF}'),LIM.get(si,0)): warn.append('%d.%d LINES %d>%d'%(si,ei,ko.count('{1FF}'),ja.count('{1FF}')))
            codes=[]
            for t in tokens(ko):
                if isinstance(t,int): codes.append(t)
                else:
                    if t not in enc: raise SystemExit('unmapped %r in %r'%(t,ko))
                    codes.append(enc[t])
            # line-length check
            ol=max(jaunits(x) for x in re.split(r'\{1FF\}',ja)); nl=max(units(x) for x in re.split(r'\{1FF\}',ko))
            if nl>ol and ol>6: warn.append('%d.%d len %d>%d : %s'%(si,ei,nl,ol,ko))
            ents[ei]=strfile.pad(codes); used+=1
    print('translated entries',used,'hangul glyphs',len(cmap),'/',len(kfont.free_slots()))
    for w in warn: print('WARN',w)
    sb=strfile.build(S)
    fb=kfont.build(open(W('work','dec','STRING__font_ash.dat'),'rb').read(),cmap)
    os.makedirs(W('work','out'),exist_ok=True)
    files={'PSP_GAME/USRDIR/STRING/string_ash.dat':lzss.compress(sb),
           'PSP_GAME/USRDIR/STRING/font_ash.dat':lzss.compress(fb)}
    json.dump({k:'%04x'%v for k,v in cmap.items()},open(W('work','out','cmap.json'),'w',encoding='utf8'),ensure_ascii=False)
    # extra modules (images, boot) hook
    try:
        import extras; files.update(extras.build(W))
    except ImportError: pass
    if '--noiso' in sys.argv: return
    tmp=OUT+'.tmp'
    iso=isobuild.Iso(ORIG,tmp)
    for p,b in files.items(): print(p,len(b),iso.replace(p,b))
    iso.close(); os.replace(tmp,OUT); print('->',OUT)
if __name__=='__main__': main()
