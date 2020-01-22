# -*- coding: utf-8 -*-
"""
Created on Wed Oct 31 13:44:35 2018

@author: mishr
"""
count =0
n=0
mon = [31,28,31,30,31,30,31,31,30,31,30,31]
next_i = 0
for yr in range(1901,2000):
    for month in range(12):
        n = mon[month]   
        if ((yr%4==0 and yr%100!=0) or yr%400 ==0) and month==1:
            n=n+1
        next_i = (next_i+n)%7
        if next_i == 6:
            count+=1
print(count)