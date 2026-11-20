import jtable,struct,glob,os,sys
def runs(d,minlen=3):
    res=[];i=0;n=len(d)-1
    while i<n:
        j=i;cnt=0
        while j<n:
            c=d[j]|(d[j+1]<<8)
            if c in jtable.J and jtable.J[c]!='　' or c==0x80 or (c>=0x81 and c<=0x9f and c!=0x80): j+=2;cnt+=1
            else: break
        if cnt>=minlen: res.append((i,j)); i=j
        else: i+=2 if cnt else 1
    return res
if __name__=='__main__':
    for f in sys.argv[1:]:
        d=open(f,'rb').read(); r=runs(d)
        tot=sum((b-a)//2 for a,b in r)
        print('%-60s runs=%d chars=%d'%(os.path.basename(f),len(r),tot))
