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

def merge(path, saveFile=False):

    print(path)
    filenames = getFileList(path, ".csv")
    
    # dfs = []
    i=0
    for filename in filenames:
    
        df = pd.read_csv(filename, sep=",") #Read the csv
    
        
        df.iloc[:, 0]= pd.to_datetime(df.iloc[:, 0]) #Convert date to datetime
    
            
        if i == 0: #First run, keep a copy of the df as df2
            stack = df.copy()
        # elif i == 1: #Second run merge df2 with df
        #     stack = pd.concat([df2, df], axis=1)
        else: #After that, just add the new df's to the combined frame
            stack = pd.concat([stack, df], axis=1)
        i+=1
            
    
    # print(stack.head(5))
    if saveFile:
        stack.to_csv(os.path.join(path, 'comb', 'bigframe.csv'), sep=";")
    return stack

if __name__ == "__main__":

    basePath= os.getcwd()
    path=os.path.join(basePath, 'data')
    merge(path, True)

