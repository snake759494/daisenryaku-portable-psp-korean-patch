import struct
def parse(d):
    n,=struct.unpack_from('<I',d,0); secs=[]
    for i in range(n):
        off,sz=struct.unpack_from('<II',d,4+8*i)
        cnt,=struct.unpack_from('<I',d,off); ents=[]
        for k in range(cnt):
            o,l=struct.unpack_from('<II',d,off+4+8*k)
            ents.append(list(struct.unpack_from('<%dH'%(l//2),d,off+o)))
        secs.append(ents)
    return secs
def pad(codes):
    codes=list(codes)
    if len(codes)%2: codes.append(0xff)
    return codes
def build(secs):
    n=len(secs); hdr=4+8*n; off=(hdr+15)//16*16
    out=bytearray(off); struct.pack_into('<I',out,0,n)
    for i,ents in enumerate(secs):
        cnt=len(ents); t=4+8*cnt
        sec=bytearray(t); struct.pack_into('<I',sec,0,cnt)
        for k,e in enumerate(ents):
            b=struct.pack('<%dH'%len(e),*e)
            struct.pack_into('<II',sec,4+8*k,len(sec),len(b)); sec+=b
        sec+=b'\0'*((-len(sec))%16)
        struct.pack_into('<II',out,4+8*i,len(out),len(sec)); out+=sec
    return bytes(out)
