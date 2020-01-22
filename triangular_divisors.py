# -*- coding: utf-8 -*-
"""
Created on Fri Sep 21 16:07:37 2018

@author: mishr
"""

def num_divisor(n):
    count= 0
    for i in range(1, int(n**0.5)+1):
        if n%i == 0:
            count +=1
            if i != n/i:
                count +=1
    return count

# istriangular not used for this prob. its inefficient then current method
def istriangular(n):
    a = int((2*n)**0.5)
    return 0.5*a*(a+1) == n

def lowesttriangular(n):
    i=1
    tri = 1
    while True:
         i+=1
         tri +=i
         if num_divisor(tri) >=n:
             return tri
             break
        
        
        


            