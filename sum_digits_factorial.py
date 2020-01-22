# -*- coding: utf-8 -*-
"""
Created on Wed Oct 31 15:48:38 2018

@author: mishr
"""

def sum_digits_factorial(n):
    product =1
    for i in range(1,n+1):
        product*=i
    l = str(product)
    sum_n = sum([int(x) for x in l])
    return sum_n