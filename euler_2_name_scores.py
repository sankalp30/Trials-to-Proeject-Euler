# -*- coding: utf-8 -*-
"""
Created on Thu Nov  1 09:53:26 2018

@author: mishr
"""

f = open('G:/myfiles/p022_names.txt','r')
contents = f.read()
l = list(contents.split('","'))
l = [x.lower().strip('"') for x in l]
l = sorted(l)
#%%
alphabet ='a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z'
alph_list= list(alphabet.split(','))
#%%
sum_ = 0
for word in l:
    word_sum = 0
    k = list(word)
    for alph in k:
        word_sum += (alph_list.index(alph)+1)
    word_score = word_sum*(l.index(word)+1)
    sum_ += word_score
print(sum_)