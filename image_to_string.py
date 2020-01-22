# -*- coding: utf-8 -*-
"""
Created on Fri Jan 25 08:19:15 2019

@author: SankalpMishra
"""

import pytesseract as pyt
import numpy as np
import pandas as pd
from PIL import Image
#%%
pyt.pytesseract.tesseract_cmd = r"C:\Program Files (x86)\Tesseract-OCR\tesseract.exe"
def get_text(file):
    return pyt.image_to_string(file)
#%%
path = 'G:/DS Marzoli Spinning project/construction sheet images/Setup sheets files'
file_test = Image.open(path+'/image003.png')
file_test.show()
#%%
c= np.asarray(file_test)
i = Image.fromarray(c)
i.show()
#%%

test_text1 = get_text(file_test)
#%%
try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract

# If you don't have tesseract executable in your PATH, include the following:
pytesseract.pytesseract.tesseract_cmd = r'C:\\Users\\SankalpMishra\\AppData\\Local\\Continuum\\anaconda3\\lib\\site-packages\\pytesseract\\__init__.py'
# Example tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract'

# Simple image to string
print(pytesseract.image_to_string(Image.open('test.png')))
