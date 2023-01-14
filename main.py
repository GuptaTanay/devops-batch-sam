# -*- coding: utf-8 -*-
"""
Created on Wed Jan 11 22:05:29 2023

@author: tanay
"""

# import pandas as pd

# df = pd.read_csv('a.csv')
# # print(df.head())
# # print(df.shape)
# # print(df.columns)

# # print(df.age)
# # print(df['age'])
# # print(df.dtypes)

# # print(df.month.unique())

# df2 = df.select_dtypes('O')
# df2.columns = df2.columns.str.upper()

# cols = df2.columns
# for col in cols:
#     df2[col] = df2[col].str.upper()
    
    
# h.w. --> 1. how to install pandas?  --pip  install pandas
# 2. check pandas version? -- pd.__version__
# 3. how to list all the functions in pandas module? -- dir()
# 4. how to print all the columns which are not object data type? -- cols = [i for i in cols if not df.select_dtyes('O)]
# ----------------------------------------------------------------------------------------
from reusable_pandas import read_file, convert_column_to_upper, convert_to_upper, convert_yes_no

df = read_file('a.csv', 'CSV')
df = convert_column_to_upper(df)
df2 = convert_to_upper(df, df.select_dtypes('O'))
df2 = convert_yes_no(df, 'DEFAULT')

print(df2.AGE.value_counts())
print(df2.AGE.min(), df2.AGE.max())
# ---------------------------------------------------------------------------------------
print(df2['MARITAL STATUS'].unique())

d= {'SINGLE':0, 'MARRIED':1, 'DIVORCED':2}
df['MARITAL STATUS'] = df['MARITAL STATUS'].map(d)

--------------------------------------------------------------------------------
# # h.w. : 
#     1. check how many months are there and there value? -- df2.Month.value_counts()
#     2. unique values in the age group? -->df2['AGE GROUP'].unique()


# -----------------------------------------------------------------