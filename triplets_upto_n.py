# -*- coding: utf-8 -*-
"""
Created on Wed Sep 19 15:12:57 2018

@author: mishr
"""

def find_triplet(n):
    triplet = []
    for a in range(1, n-2):
        for b in range(a+1,n-1):
            c = n-(a+b)
            if ((a**2) + (b**2)) == (c**2):
                triplet.append([a,b,c])
    return triplet
                    