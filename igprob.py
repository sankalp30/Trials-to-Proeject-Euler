# -*- coding: utf-8 -*-
"""
Created on Fri Aug  2 10:21:39 2019

@author: mishr
"""

import numpy as np
import pandas as pd
from datetime import datetime
#%%

t_start = datetime.now()
path_ig = 'G:/myfiles/'

df_ig = pd.read_excel(path_ig + 'ig_prob' + '.xlsx')

#%%
cols = ['Material', 'new_ig_ap', 'new_ig_eni', 'new_ig_eu', 'newbuy_ap', 'newbuy_eni', 'newbuy_eu']
summary_list = []
for i, row in df_ig.iterrows():
    material = df_ig.iloc[i]['Material']
    new_buy = df_ig.iloc[i]['total_newbuy']
    ig_ap = df_ig.iloc[i]['ig_dc_ap']
    ig_eni = df_ig.iloc[i]['ig_dc_eni']
    ig_eu = df_ig.iloc[i]['ig_dc_eu']
    newbuy_ap = 0
    newbuy_eni = 0
    newbuy_eu = 0
    
    list_dci = [['ap',ig_ap, newbuy_ap],['eni',ig_eni, newbuy_eni], ['eu',ig_eu, newbuy_eu]]
    
    while new_buy > 0:
        list_dci.sort(key = lambda x: x[1], reverse = True)
        list_dci[0][1] -=1
        list_dci[0][2] +=1
        new_buy -=1
        print(new_buy)
        print(list_dci)
        
    X = pd.DataFrame([[material, list_dci[list_dci[0]== 'ap'][1], list_dci[list_dci[0]== 'eni'][1], list_dci[list_dci[0]== 'eu'][1], \
                       list_dci[list_dci[0]== 'ap'][2], list_dci[list_dci[0]== 'eni'][2], list_dci[list_dci[0]== 'eu'][2]]])
    summary_list.append(X)

df_sum = pd.concat(summary_list)

df_out  = pd.merge(df_ig, df_sum, on = 'Material')
    
        
#%%
out_path = 'H:\costing_automation\ds_drawing_summary.xlsx'
writer = pd.ExcelWriter(out_path , engine='xlsxwriter')
df.to_excel(writer, sheet_name = 'Sheet1', index = False)        


t_stop= datetime.now()
print(t_stop- t_start)