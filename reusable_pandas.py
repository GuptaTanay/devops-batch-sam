# -*- coding: utf-8 -*-
"""
Created on Thu Jan 12 21:40:34 2023

@author: tanay
"""

import pandas as pd
import numpy as np



def read_file(filename, fileext='csv'):
    fileext = fileext.lower()
    if fileext == 'csv':
        return pd.read_csv(filename)
    elif (fileext == 'xls') or (fileext == 'xlsx'):
        return pd.read_excel(filename)
    elif fileext == 'json':
        return pd.read_json(filename)
    else:
        print('Please pass valid filename and file extension')
        
def convert_column_to_upper(df):
    df.columns = df.columns.str.upper()
    return  df

def convert_to_upper(df, cols):
    for col in cols:
        df[col] = df[col].str.upper()
    return df

def convert_yes_no(df, col):
    df[col] = np.where(df[col].str.upper() == 'YES', 1 ,0)
    return df
    