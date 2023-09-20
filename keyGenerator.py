import math
import random

def genKey():
    #Choose two distinct primes, p and q
    p = random.randint(2, 1000)
    q = random.randint(2, 1000)
    
    #Test if p and q are prime
    while not Fermat(p):
        if not Fermat(p):
            p = random.randint(2, 1000)
    
    while not Fermat(q):
        if not Fermat(q):
            q = random.randint(2, 1000)
            
    #Compute n = pq
    n = p * q
    
    #Compute phi = (p-1)(q-1)
    phi = (p - 1) * (q - 1)
    
    #Choose e such that 1 < e < phi and e and phi are coprime
    e = random.randint(2, phi - 1)
    while gcd(e, phi) != 1:
        if gcd(e, phi) != 1:
            e = random.randint(2, phi - 1)
    
    print(e)
    print(phi)
    print(gcd(e, phi))
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
    
def gcd(a=1, b=1):
    ''' The gcd function implements Euclid's
    GCD algorithm to find the greatest common
    divisor of two positive integers a and b'''
    
    if b == 0:
        return a
    else:
        return gcd(b, a%b)

genKey()