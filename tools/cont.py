import struct
def parse(d):
    n,=struct.unpack_from('<I',d,0); r=[]
    for i in range(n):
        o,s,no=struct.unpack_from('<III',d,4+12*i)
        nm=d[no:d.index(b'\0',no)].decode('latin1')
        r.append((nm,o,s))
    return r
def build(items):
    """items: list of (name, bytes) -> container bytes (16-byte aligned data, names at end)"""
    n=len(items); hdr=4+12*n; off=(hdr+15)//16*16
    body=bytearray(); ents=[]
    for nm,b in items:
        ents.append((off+len(body),len(b))); body+=b
        body+=b'\0'*((-len(body))%16)
    nameoff=off+len(body); names=bytearray(); nofs=[]
    for nm,b in items: nofs.append(nameoff+len(names)); names+=nm.encode('latin1')+b'\0'
    out=bytearray(struct.pack('<I',n))
    for (o,s),no in zip(ents,nofs): out+=struct.pack('<III',o,s,no)
    out+=b'\0'*(off-len(out)); out+=body+names
    return bytes(out)
