def Decrpyt_KeyGen(e,Qn):
    d=1
    while True:
        k = e*d%Qn
        if(k==1 and d != e):
            break
        d = d+1
    return d
