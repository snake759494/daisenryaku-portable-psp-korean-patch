import capstone,sys,struct,os
sys.path.insert(0,os.path.dirname(__file__))
from elf import Boot,build_refs
B=Boot(os.path.join(os.path.dirname(__file__),'..','work','ext','PSP_GAME','SYSDIR','BOOT.BIN'))
md=capstone.Cs(capstone.CS_ARCH_MIPS,capstone.CS_MODE_MIPS32+capstone.CS_MODE_LITTLE_ENDIAN)
def dis(a,n):
    for i in md.disasm(bytes(B.b[a+0x80:a+0x80+4*n]),a): print('%06x: %s %s'%(i.address,i.mnemonic,i.op_str))
if __name__=='__main__':
    if sys.argv[1]=='ref':
        R=build_refs(B)
        for t in sys.argv[2:]:
            print(t,R.get(int(t,16)))
    else: dis(int(sys.argv[1],16),int(sys.argv[2]))
