# -*- coding: utf-8 -*-
"""
Created on Thu Sep 13 16:08:45 2018

@author: SankalpMishra
"""


def largest_pallindrome(lower, upper):
    for i in range(upper**2,lower**2,-1):
        stri = str(i)
        lista = list(stri)
        listb = lista[::-1]
        if lista == listb:
            for k in range(lower,upper):
                c= i/k
                if lower<=c<=upper and c - int(c) == 0:
                    return [i, c, k]
                    break
    return 0
            