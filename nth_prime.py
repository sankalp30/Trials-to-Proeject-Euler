# -*- coding: utf-8 -*-
"""
Created on Fri Sep 14 15:57:28 2018

@author: SankalpMishra
"""
def is_prime(x):
    for i in range(2,int(x**0.5)+1):
        if x%i == 0:
            return False
    return True

def nth_prime(n):
    primecount = 0
    i = 2
    while primecount <n:
        if is_prime(i):
            primecount +=1
        i+=1
    return (i-1)       
        