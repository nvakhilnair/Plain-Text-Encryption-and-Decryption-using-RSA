def encrpytion(data,e,N):
    cipher = pow(data,int(e))%int(N)
    return cipher
