# -*- coding: utf-8 -*-
"""
Created on Tue Oct 16 10:24:29 2018

@author: mishr
"""

#%%
import math
def numtowords(n):
    c= 0
    l = 0
    k = 0 
    m = 0 
    num2words1 = {0 : '',1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five', \
            6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine', 10: 'Ten', \
            11: 'Eleven', 12: 'Twelve', 13: 'Thirteen', 14: 'Fourteen', \
            15: 'Fifteen', 16: 'Sixteen', 17: 'Seventeen', 18: 'Eighteen', 19: 'Nineteen'}
    num2words2 = ['','Ten','Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety']
    
    if 0<n<20:
        return num2words1[n]
    elif 19<n<100:
        c = math.floor(n/10)
        l = n%10
        return num2words2[c] + num2words1[l]
    elif 99<n<1000:
        k = math.floor(n/100)
        c = math.floor((n%100)/10)
        l = n%10
        if n%100 == 0:
            and_ =''
        else: 
            and_ = 'and'
        if 0<=(n%100)<20:
            return num2words1[k] + 'hundred'+ and_ + num2words1[(n%100)]
        elif 19<(n%100)<100:
            return num2words1[k] + 'hundred'+ and_ + num2words2[c] + num2words1[l]
    elif 999<n:
        m = math.floor(n/1000)
        k = math.floor((n%1000)/100)
        c = math.floor(((n%1000)%100)/10)
        l = n%10
        if n%1000 == 0:
            hundred_ = ''
        else: 
            hundred_ = 'hundred'
        if n%100 == 0:
            and_ =''
        else: 
            and_ = 'and'
        if 0<=(n%100)<20:
            return num2words1[m] + 'thousand' + num2words1[k] + hundred_+ and_ + num2words1[l]
        elif 19<(n%100)<100:
            return num2words1[m] + 'thousand' + num2words1[k] + hundred_+ and_ + num2words2[c] + num2words1[l]
        return num2words1[m] + 'thousand' + num2words1[k] + hundred_+ and_ + num2words2[c] + num2words1[l]
           
#%%
k= 0
for i in range(1,1001):
    print(numtowords(i))
    k+=len(list(numtowords(i)))
print(k)    






     