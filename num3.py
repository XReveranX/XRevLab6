#12345?7?8
#23

def mas(d):
    slv={}
    for i in range(10):
        i1=str(i)
        for j in range(10):
            j1=str(j)
            k=int(("12345"+j1+"7"+i1+"8"))
            if (k%d)==0:
                slv[k]=k//d
    return slv

slv = mas(23)
for kl, zn in slv.items(): 
    print(kl, zn)
