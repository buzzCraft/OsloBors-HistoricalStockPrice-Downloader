# -*- coding: utf-8 -*-
"""
Created on Wed Oct 14 16:03:19 2020


First run:
    You need to have a folder called /data/comb/
    in the same folder you have the python files in

Usage:
    downloader.stockDataDownloader() take save file path as argument, and download
    xlsx files from OsloBors, it then convert these files to csv and delete the xlsx files
    
    merger.merge() take the path of the saved csv's and merge them into one big df, if set to
    True, it also save a csv version of the df to /data/comb/. I find this usefull when doing
    quick checkups on the data.
    
Plans:
    Im planning to make a downloader class and a much more generic datawrangler class, and at the
    same time create a stock class.
    

"""


import merger
import os
import stockClass
import pandas as pd


    
dir = os.path.join(os.path.join(os.getcwd(), 'data'))

if not os.path.exists(dir):
    os.mkdir(dir)
    os.mkdir(os.path.join(dir, 'comb'))

tickerList=[]
#Convert the CSV to list
with open('./Tick.csv', 'r') as f:
    liste = f.readlines()
    for item in liste:
        tickerList.append(item.rstrip("\n")) #Stripping newline in csv
print(tickerList)
stockList = []
for TICKER in tickerList:
    stockList.append(stockClass.Stock(TICKER))
date = True
for stock in stockList:
    
    stock.downloadData(date)
    stock.readData()
    print(stock.data.head())
    stock.plotData()                                     #Time consuming!!
    date = False
    
merger.merge(stockList, True)
# data.downloadData()
# x = data.saveData()
# print(x)