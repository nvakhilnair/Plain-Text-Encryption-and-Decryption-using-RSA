def decrpytion(cipher,d,N):
    decipher = pow(cipher,d)%N
    return decipher
