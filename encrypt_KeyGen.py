def encrypt_KeyGen(Qn,N):
    temp = list(range(2,Qn))
    for i in temp:
        if(N%i != 0 and Qn%i != 0):
            e = i
    return e
