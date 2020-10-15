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

import downloader
import merger
import os
import dlClass
import pandas as pd


    



basePath= os.getcwd()  #Get path that main.py is saved in
path=os.path.join(basePath, 'data') #In

#downloader.stockDataDownloader(path)    #Download data


df = merger.merge(path) #Merge data, set (path, True)to save combined df as csv

print(df.head())

# data = dlClass.OsloBorsData()
# data.downloadData()
# x = data.saveData()
# print(x)