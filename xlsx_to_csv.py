# -*- coding: utf-8 -*-
"""
Created on Wed Oct 14 12:47:02 2020

@author: theoo
"""

import pandas as pd
import glob
import os
import sys

def XlsxToCsv(filepath, newfilepath=False):
    print(f'Converting {filename} to csv file')
    read_file = pd.read_excel (filename)
    read_file.to_csv (filename, index = None, header=True)

def getFileList(path, extension):
    filenames = []
    
    try:
        for file in [f for f in os.listdir(path) if f.endswith('.csv')]:
            filenames.append(os.path.join(path, file))
    except FileNotFoundError:
        print(f'File not foud, check the path: {path}')
    except:
        print("Unexpected error:", sys.exc_info()[0])
        # print("Error getting the files, check path")
    return filenames
    

path =r'D:\Programering\Prosjekter\AI\Stocks Data Mining\OsloBors-HistoricalStockPrice-Downloader\Stocks'

# filenames = os.path.join(path, "*.xlsx")

# dfs = []

# for filename in filenames:
#     print(f'Converting {filename} to csv file')
#     # read_file = pd.read_excel (filename)
#     # read_file.to_csv (filename, index = None, header=True)

## Take path ('c:\my\path') and file extension ('.csv') and return a list with files


filenames = getFileList(path, '.csv')
for file in filenames:
    # print(file)
    
    
    df = pd.read_csv(file, sep=',')
    print(df.head())
print("done")
