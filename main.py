# -*- coding: utf-8 -*-
"""
Created on Wed Oct 14 16:03:19 2020

Usage:
    Import Ticks from ./Tick.csv
    Alter the file for fewer stocks
    
    To create stock obj, call stockClass.Stock(TICKER)
    To plot stockdata, call stock.plot()
    To merge all data to one dataframe, send a list of 
    stock obj to merger.merge(LIST)
    

"""


import merger
import os
import stockClass
# import pandas as pd


    
dir = os.path.join(os.path.join(os.getcwd(), 'data'))     #Make needed folder structure

if not os.path.exists(dir):
    os.mkdir(dir)
    os.mkdir(os.path.join(dir, 'comb'))

tickerList=[]
#Convert the Ticker CSV to  ticker list
with open('./Tick.csv', 'r') as f:
    liste = f.readlines()
    for item in liste:
        tickerList.append(item.rstrip("\n")) #Stripping newline in csv
        
print(tickerList)
stockList = []

for TICKER in tickerList:
    stockList.append(stockClass.Stock(TICKER))

# 

for stock in stockList:
    
    stock.downloadData()                                          #Download data
    stock.readData()                                              #Read downloaded data
    print(stock.data.head())                                      #Print first 5 rows of df



stock = stockList[1]                                             #Do operation on one stock
# # stock.plotData()
stock.plotRollingMean(10,20)                                     #Plot stock with rolling mean for x,y and z days
# print(stock.data.head())    
merger.merge(stockList, saveFile=True)                                    #Merge all stocks to one big df and save to csv

