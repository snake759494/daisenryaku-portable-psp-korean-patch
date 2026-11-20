"""Daisenryaku Portable *_ash.dat codec: u32 LE size + Okumura bit-LZSS (EI=14,EJ=4,MSB-first, flag1=literal, r=1, len=j+3)."""
import struct
N=1<<14; F=(1<<4)+2  # max len 18
def decompress(d):
    size,=struct.unpack_from('<I',d,0); p=4; mask=0; byte=0
    def bit():
        nonlocal p,mask,byte
        if mask==0: byte=d[p]; p+=1; mask=0x80
        b=1 if byte&mask else 0; mask>>=1; return b
    def bits(n):
        v=0
        for _ in range(n): v=(v<<1)|bit()
        return v
    buf=bytearray(N); r=1; out=bytearray()
    while len(out)<size:
        if bit():
            c=bits(8); out.append(c); buf[r]=c; r=(r+1)&(N-1)
        else:
            i=bits(14)
            if i==0: break
            j=bits(4)
            for k in range(j+3):
                c=buf[(i+k)&(N-1)]; out.append(c); buf[r]=c; r=(r+1)&(N-1)
                if len(out)>=size: break
    return bytes(out)
class BW:
    def __init__(s): s.o=bytearray(); s.m=0x80; s.c=0
    def put(s,v,n):
        for k in range(n-1,-1,-1):
            if (v>>k)&1: s.c|=s.m
            s.m>>=1
            if s.m==0: s.o.append(s.c); s.c=0; s.m=0x80
    def done(s):
        if s.m!=0x80: s.o.append(s.c)
        return bytes(s.o)
def compress(data):
    w=BW(); n=len(data); pos=0
    # hash chains on 3-byte prefixes; ring index of data pos p is (p+1)&(N-1)
    head={}; 
    while pos<n:
        bl=0; bp=0
        if pos+3<=n:
            key=data[pos:pos+3]
            for q in reversed(head.get(key,[])[-64:]):
                if pos-q>=N-F-1 or ((q+1)&(N-1))==0: continue
                L=0; mx=min(F,n-pos)
                while L<mx and data[q+L]==data[pos+L]: L+=1
                if L>bl:
                    bl=L; bp=q
                    if L==mx: break
        if bl>=3:
            w.put(0,1); w.put((bp+1)&(N-1),14); w.put(bl-3,4); adv=bl
        else:
            w.put(1,1); w.put(data[pos],8); adv=1
        for k in range(adv):
            if pos+k+3<=n: head.setdefault(data[pos+k:pos+k+3],[]).append(pos+k)
        pos+=adv
    w.put(0,1); w.put(0,14)
    return struct.pack('<I',n)+w.done()
