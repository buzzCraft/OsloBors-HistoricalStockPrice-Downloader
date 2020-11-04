# -*- coding: utf-8 -*-
"""
Created on Sun Oct 11 17:06:00 2020


"""


import os
import pandas as pd
import numpy as np


def merge(stocks, saveFile=False):
    path = os.path.join(os.getcwd(), 'data')
    first=True
    for stock in stocks:
    
        df = stock.getData() #Call the object for the dataframe    
        print(stock.name())    
        if first: #First run, keep a copy of the df as df2
            stack = df.copy()
            first = False

        else: #After that, just add the new df's to the combined frame
            stack = pd.concat([stack, df], axis=1)

        
            
    
    stack.replace("", np.nan, inplace=True)
    if saveFile:
        stack.to_csv(os.path.join(path, 'comb', 'bigframe.csv'), sep=";")
    
    return stack

if __name__ == "__main__":

    basePath= os.getcwd()
    path=os.path.join(basePath, 'data')
    merge(path, True)

