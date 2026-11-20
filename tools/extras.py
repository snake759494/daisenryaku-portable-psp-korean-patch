import os,sys,hashlib
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
import cont,lzss
from imgtool import Tex,apply_job,expand_jobs,apply_fit,fit_jobs
import imgspec
def build(W):
    out={}
    groups={}
    for (c,g),jobs in imgspec.SPEC.items(): groups.setdefault(c,[]).append((g,jobs))
    for c,lst in groups.items():
        raw=c.endswith('.ofs')
        d=bytearray(open(W('work','ext','PSP_GAME','USRDIR',*c.split('/')) if raw else W('work','dec',c.replace('/','__')),'rb').read())
        it={n:(o,s) for n,o,s in cont.parse(bytes(d))}
        for g,jobs in lst:
            o,s=it[g]; T=Tex(bytes(d[o:o+s]))
            fit_jobs(T,expand_jobs(T,jobs))
            nb=T.save_back(); assert len(nb)==s; d[o:o+s]=nb
        if raw:
            out['PSP_GAME/USRDIR/'+c]=bytes(d); print('img',c,len(d)); continue
        h=hashlib.md5(d).hexdigest(); cp=W('work','out','cache_'+c.replace('/','__')+'_'+h)
        if os.path.exists(cp): z=open(cp,'rb').read()
        else:
            for f in os.listdir(W('work','out')):
                if f.startswith('cache_'+c.replace('/','__')): os.remove(W('work','out',f))
            z=lzss.compress(bytes(d)); assert lzss.decompress(z)==bytes(d); open(cp,'wb').write(z)
        out['PSP_GAME/USRDIR/'+c]=z
        print('img',c,len(z))
    try:
        import bootpatch; out.update(bootpatch.build(W))
    except ImportError: pass
    return out
