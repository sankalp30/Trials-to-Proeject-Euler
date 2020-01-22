# -*- coding: utf-8 -*-
"""
Created on Wed Sep 12 16:16:42 2018

@author: SankalpMishra
"""
import time

#def largest_prime_factor(x):
#    factors = []
#    start = time.time()
#    l = []
#    for i in range(2,x):
#            if x%i==0: 
#                factors.append(i)
#                l.append(i)
#            #for k in range(2,i-1):
#             #   if i%k == 0 and i in factors:
#              #      factors.remove(i)
#    for m in l:
#        for k in l:
#            if m%k == 0 and m in factors and k<m:
#                factors.remove(m)
#                print(factors)
#    end = time.time()
#    print(end - start)  
#    return factors[-1]    
         
#%%
def find_smallest_factor(n,i):
    while n%i!=0 and i<n:
        i+=1
    return i

def is_prime(x):
    for i in range(2, int(x**0.5)+1):
        if x%i==0:
            return False
    return True 

def largest_prime_factor(x):
    smallest_factor = find_smallest_factor(x,2)
    while smallest_factor<x:
        largest_factor = x/smallest_factor
        if is_prime(largest_factor):
            return largest_factor
            break
        smallest_factor = find_smallest_factor(x,smallest_factor+1)
        
    