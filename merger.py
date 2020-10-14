# -*- coding: utf-8 -*-
"""
Created on Sun Oct 11 17:06:00 2020


"""


import os
import pandas as pd
import sys


# get data file names

def getFileList(path, extension):
    filenames = []
    
    try:
        for file in [f for f in os.listdir(path) if f.endswith('.csv')]:
            filenames.append(os.path.join(path, file))
            # print(os.path.join(path, file))
    except FileNotFoundError:
        print(f'File not foud, check the path: {path}')
    except:
        print("Unexpected error:", sys.exc_info()[0])
        # print("Error getting the files, check path")
    return filenames

basePath= os.getcwd()
path=os.path.join(basePath, 'data')
print(path)
filenames = getFileList(path, ".csv")

dfs = []

for filename in filenames:
    # print(filename)
    df = pd.read_csv(filename, sep=",")
    print(df.head())
    
    df.iloc[:, 0]= pd.to_datetime(df.iloc[:, 0]) #Convert date to datetime
    # df.drop(df.columns[0], axis=1, inplace=True)
    print(df.head())
    print(df.dtypes)
    # dfs.append(pd.read_csv(filename, sep=","))

# Concatenate all data into one DataFrame

# big_frame = pd.concat(dfs, ignore_index=True)

# print(big_frame.head(50))
# big_frame.to_csv(os.path.join(path, 'bigframe.csv'))

#combine all files in the list
