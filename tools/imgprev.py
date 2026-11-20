import sys;sys.path.insert(0,'tools')
from imgtool import *; from imgspec import SPEC
c,g=sys.argv[1],sys.argv[2]
d=open('work/dec/'+c.replace('/','__'),'rb').read()
it={n:(o,s) for n,o,s in cont.parse(d)}
o,s=it[g]; T=Tex(d[o:o+s])
for j in SPEC[(c,g)]: apply_job(T,j)
im=Image.fromarray(T.rgba().astype(np.uint8),'RGBA')
bg=Image.new('RGBA',im.size,(40,80,40,255)); bg.alpha_composite(im)
bg.convert('RGB').resize((T.w*2,T.h*2),Image.NEAREST).save(SP+'prev.png')
