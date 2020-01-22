# -*- coding: utf-8 -*-
"""
Created on Fri Sep 14 14:25:32 2018

@author: SankalpMishra
"""

def smallest_multiple(upper):
    primes = list(range(2,upper+1))
    for i in range(2,upper+1):
        for k in range(2,int(i**0.5)+1):
            if i%k == 0 and i in primes:
                primes.remove(i)
    l = []
    for c in primes:
        i=2
        while c**i <upper:
            primes.append(c**i)
            l.append(c**(i-1))
            i+=1              
    primes.sort()
    primes = set(primes)-set(l)
    product = 1
    for o in primes:
        product *= o
    return product