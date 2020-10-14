# -*- coding: utf-8 -*-
"""
Created on Sun Oct 11 17:06:00 2020

@author: theoo
"""

import glob

import pandas as pd

# get data file names

path =r'D:\Programering\Prosjekter\AI\Stocks Data Mining\OsloBors-HistoricalStockPrice-Downloader\Stocks'

filenames = glob.glob(path + "/*.csv")

dfs = []

for filename in filenames:
    print(filename)

    dfs.append(pd.read_csv(filename, sep=";"))

# Concatenate all data into one DataFrame

big_frame = pd.concat(dfs, ignore_index=True)