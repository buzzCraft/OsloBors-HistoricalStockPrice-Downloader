# -*- coding: utf-8 -*-
"""
Created on Wed Oct 14 16:03:19 2020


"""

import downloader
import merger
import os



    



basePath= os.getcwd()
path=os.path.join(basePath, 'data')

#downloader.stockDataDownloader(path)    #Download data


df = merger.merge(path) #Merge data, set (path, True)to save combined df as csv

print(df.head())