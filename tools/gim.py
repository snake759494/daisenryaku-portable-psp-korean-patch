def unswizzle(data,wbytes,h):
    out=bytearray(len(data)); bw=wbytes//16; i=0
    for by in range(h//8):
        for bx in range(bw):
            for r in range(8):
                o=(by*8+r)*wbytes+bx*16
                out[o:o+16]=data[i:i+16]; i+=16
    return bytes(out)
def swizzle(data,wbytes,h):
    out=bytearray(len(data)); bw=wbytes//16; i=0
    for by in range(h//8):
        for bx in range(bw):
            for r in range(8):
                o=(by*8+r)*wbytes+bx*16
                out[i:i+16]=data[o:o+16]; i+=16
    return bytes(out)
