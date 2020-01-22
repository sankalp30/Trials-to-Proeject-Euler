# -*- coding: utf-8 -*-
"""
Created on Wed Oct 10 10:05:44 2018

@author: mishr
"""
import time
def seq(n):
    l = []
    nextn = 0
    while n != 1:
        l.append(n)
        if n%2 == 0 :
            nextn = int(n)/2
            n= nextn
        else:
            nextn = 3*n+1
            n = nextn
    return len(l)

def long_seq(n):
    start = time.time()
    
    k = 0
    p=0
    for i in range(n,1,-1):
        r   = seq(i)
        if r>k:
            k=r
            p=i
    finish = time.time()
    return k,p , (finish - start)
    
    