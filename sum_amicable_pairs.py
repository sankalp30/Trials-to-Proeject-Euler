# -*- coding: utf-8 -*-
"""
Created on Thu Nov  1 08:26:12 2018

@author: mishr
"""

def proper_divisors(n):
    divs =[1]
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
           divs.append(i) 
           if i != n/i:
               divs.append(n/i)
    return divs

def sum_amicable_pairs(n): #all numbers under n -_-
    l=[]
    for i in range(2,n):
        k = sum(proper_divisors(i))
        if sum(proper_divisors(k))==i and k!=i:
            l.append(i)
    return sum(l)