import random
import sympy
def primeGen():
    primes = []
    for i in range(1,3):
        temp = []
        for j in range(1,3):
            temp.append(random.randint(60,120))
        primes.append(random.choice(list(sympy.primerange(min(temp), max(temp)))))
    p = min(primes)
    q = max(primes)
    return p,q
