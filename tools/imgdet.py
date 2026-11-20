import sys,json;sys.path.insert(0,'tools')
from imgtool import *
from scipy import ndimage
c,g=sys.argv[1],sys.argv[2]; mode=sys.argv[3] if len(sys.argv)>3 else 'wo'
d=open('work/dec/'+c.replace('/','__'),'rb').read()
it={n:(o,s) for n,o,s in cont.parse(d)}
o,s=it[g]; T=Tex(d[o:o+s]); R=T.rgba(); L=lum(R); A=R[...,3]
if mode=='wo':   # white text with dark outline
    wt=(L>215)&(A>200); dk=(L<80)&(A>150)
    m=wt&ndimage.binary_dilation(dk,iterations=2)
    m=ndimage.binary_dilation(m,iterations=1)|(dk&ndimage.binary_dilation(wt,iterations=2))
mm=ndimage.binary_closing(m,structure=np.ones((3,7)))
mm=ndimage.binary_dilation(mm,structure=np.ones((1,5)))
lab,n=ndimage.label(mm)
boxes=[]
for sl in ndimage.find_objects(lab):
    y0,y1,x0,x1=sl[0].start,sl[0].stop,sl[1].start,sl[1].stop
    if (y1-y0)>=8 and (x1-x0)>=8 and m[sl].sum()>30: boxes.append([x0,y0,x1-x0,y1-y0])
boxes.sort(key=lambda b:(b[1]//6,b[0]))
im=Image.fromarray(R.astype(np.uint8),'RGBA'); bg=Image.new('RGBA',im.size,(40,80,40,255)); bg.alpha_composite(im)
big=bg.convert('RGB').resize((T.w*2,T.h*2),Image.NEAREST); dr=ImageDraw.Draw(big); f=ImageFont.truetype('arial.ttf',12)
for i,(x,y,w,h) in enumerate(boxes):
    dr.rectangle([x*2,y*2,(x+w)*2-1,(y+h)*2-1],outline=(255,0,0)); dr.text((x*2,y*2-10),str(i),fill=(255,255,0),font=f)
big.save(SP+'det.png'); json.dump(boxes,open(SP+'det.json','w'))
for i,b in enumerate(boxes): print(i,b)
