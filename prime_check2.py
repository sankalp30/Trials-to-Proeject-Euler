# -*- coding: utf-8 -*-
"""
Created on Sat Oct 27 12:48:13 2018

@author: mishr
"""

def is_prime(n):
    is_prime = True
    i= 2
    while i<n-1:
        i+=1
        if n%i == 0:
            is_prime = False
            break
    return is_prime    
    