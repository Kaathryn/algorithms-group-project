import math
import random

def genKey():
    #Choose two distinct primes, p and q
    p = random.randint(1, 1000)
    q = random.randint(1, 1000)
    
    #Test if p and q are prime
    while not Fermat(p):
        if not Fermat(p):
            p = random.randint(1, 100)
    
    while not Fermat(q):
        if not Fermat(q):
            q = random.randint(1, 100)
            Fermat(q)
            
    #Compute n = pq
    n = p * q
    
    #Compute phi = (p-1)(q-1)
    phi = (p - 1) * (q - 1)
    
    #Choose e such that 1 < e < phi and e and phi are coprime
    
    
    #Find a d where ed is identical to 1 (mod phi)
    
def Fermat(p = 137):
    '''Test if p is prime with Fermat\'s little theorem\n'''
    t = True
    for i in range(1, p):
        if pow(i, p-1, p) != 1:
            t = False
            break
    if not t:
        return False
    else:
        return True

genKey()