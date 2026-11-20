"""Korean font builder for STRING/font_ash.dat (512x512 idx8 swizzled GIM, 12x12 cells, 42x42 grid)."""
import unicodedata, numpy as np, os
from PIL import Image, ImageDraw, ImageFont
import gim, jtable
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FONT=os.path.join(ROOT,'fonts','Galmuri11.ttf')
def is_jp(ch):
    o=ord(ch)
    return 0x3040<=o<=0x30ff or 0x4e00<=o<=0x9fff or ch in '々'
def free_slots():
    s=[]
    for r in range(42):
        for c in range(42):
            code=(r<<8)|c
            ch=jtable.J.get(code)
            if (ch and is_jp(ch)) or r>=29: s.append(code)
    return s
# ASCII / symbol -> existing glyph code
def _rc(r,c): return (r<<8)|c
SYM={}
for code,ch in jtable.J.items():
    if not is_jp(ch): SYM.setdefault(ch,code)
# fullwidth map for ASCII
for o in range(0x21,0x7f):
    fw=chr(o+0xfee0)
    if fw in SYM: SYM.setdefault(chr(o),SYM[fw])
# 0x80+n = row0 glyph n drawn half-width (6px); 0x9A.. = blank half-width
SYM[' ']=0x9A; SYM['-']=0x80; SYM['/']=0x81; SYM['.']=0x82; SYM['(']=0x83; SYM[')']=0x84; SYM[',']=0x8B; SYM[':']=0x92; SYM[';']=0x93; SYM['+']=0x96; SYM['*']=0x95; SYM['=']=0x94
SYM['~']=SYM['～']; SYM['·']=0x87; SYM['…']=SYM['…']; SYM['?']=SYM['？']; SYM['!']=SYM['！']
def assign(chars):
    free=free_slots(); need=sorted(c for c in set(chars) if c not in SYM)
    assert len(need)<=len(free), (len(need),len(free))
    return dict(zip(need,free))
def render_cell(ch,font):
    im=Image.new('L',(12,12),0); dr=ImageDraw.Draw(im)
    dr.text((0,-1),ch,font=font,fill=255)   # Galmuri11: 12px em; glyph rows 1..11
    return np.asarray(im)
def build(orig_gim,cmap):
    from gimfile import info
    d=bytearray(orig_gim); I=info(d)['img']; p=I['pix']
    px=np.frombuffer(gim.unswizzle(bytes(d[p:p+512*512]),512,512),np.uint8).reshape(512,512).copy()
    font=ImageFont.truetype(FONT,12)
    for code in free_slots():
        r,c=code>>8,code&0xff; px[r*12:r*12+12,c*12:c*12+12]=0xe1
    for ch,code in cmap.items():
        r,c=code>>8,code&0xff
        a=render_cell(ch,font)
        lv=np.round(a/255*15).astype(np.uint8)
        px[r*12:r*12+12,c*12:c*12+12]=0xe1+2*lv
    d[p:p+512*512]=gim.swizzle(px.tobytes(),512,512)
    return bytes(d)
