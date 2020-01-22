# -*- coding: utf-8 -*-
"""
Created on Tue Sep 18 16:04:47 2018

@author: mishr
"""
import numpy

def largest_product_adjacent(n,i):
    strn = list(str(n))
    print(strn)
    x=0
    hp = 0
    prev = 0
    while x+i<=len(strn):
        new = 1
        print(strn[x:(x+i)])
        num_list = [int(j) for j in strn[x:(x+i)]]
        print(num_list)
        for l in num_list:
            new *=l
            print(new)
        if new> prev:
            prev = new
        x+=1
    return prev
        
        
        
        
    