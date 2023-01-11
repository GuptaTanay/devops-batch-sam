# -*- coding: utf-8 -*-
"""
Created on Wed Jan 11 22:05:29 2023

@author: tanay
"""

import pandas as pd

df = pd.read_csv('a.csv')
# print(df.head())
# print(df.shape)
# print(df.columns)

# print(df.age)
# print(df['age'])
# print(df.dtypes)

# print(df.month.unique())

df2 = df.select_dtypes('O')
df2.columns = df2.columns.str.upper()

cols = df2.columns
for col in cols:
    df2[col] = df2[col].str.upper()
    
    
# h.w. --> 1. how to install pandas?
# 2. check pandas version?
# 3. how to list all the functions in pandas module?
# 4. how to print all the columns which are not object data type?