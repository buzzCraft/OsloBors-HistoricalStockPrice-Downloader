# -*- coding: utf-8 -*-
"""
Created on Sun Oct 11 17:06:00 2020


"""


import os
import pandas as pd


def merge(stocks, saveFile=False):
    path = os.path.join(os.getcwd(), 'data')
    i=0
    for stock in stocks:
    
        df = stock.getData()
    
        
        df.iloc[:, 0]= pd.to_datetime(df.iloc[:, 0]) #Convert date to datetime
    
            
        if i == 0: #First run, keep a copy of the df as df2
            stack = df.copy()

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

