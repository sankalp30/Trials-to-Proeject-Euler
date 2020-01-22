# -*- coding: utf-8 -*-
"""
Created on Wed Sep 19 15:57:42 2018

@author: mishr
"""

def is_prime(x):
    for i in range(2,int(x**0.5)+1):
        if x%i == 0:
            return False
    return True
def sum_of_prime(n):
    sum = 0
    for k in range(2,n):
        if is_prime(k):
            sum +=k
    return sum
