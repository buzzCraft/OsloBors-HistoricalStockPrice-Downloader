# -*- coding: utf-8 -*-
"""
Created on Wed Oct 14 18:23:10 2020

@author: theoo
"""
import os
import pandas as pd
import requests
import sys

class OsloBorsData():
    def __init__(self):
        self.path = os.path.join(os.getcwd(), 'data')
        self.stack = pd.DataFrame()
        

        

    def xlsxToCsv(self, file, newfilepath):  
    
        print(f'Converting {file} to csv file')
        read_file = pd.read_excel (file)
        read_file.to_csv (newfilepath, index = None, header=True)
    
    def stockDataDownloader(self, tickFile='./Tick.csv'):
        TICKER_LIST=[]
        #Convert the CSV to list
        with open(tickFile, 'r') as f:
            liste = f.readlines()
            for item in liste:
                TICKER_LIST.append(item.rstrip("\n")) #Stripping newline in csv
        
        
        for TICKER in TICKER_LIST:
         	#Download from oslo bors, using f string and {TICKER}
    
            csv_url=f'https://www.oslobors.no/ob/servlets/excel?type=history&columns=DATE%2C+CLOSE_CA%2C+BID_CA%2C+ASK_CA%2C+HIGH_CA%2C+LOW_CA%2C+TURNOVER_TOTAL%2C+VOLUME_TOTAL_CA%2C+TRADES_COUNT%2C+TRADES_COUNT_TOTAL%2C+VWAP_CA&format[DATE]=ddd.mm.YY&format[CLOSE_CA]=%23%2C%23%230.00%23%23%23&format[BID_CA]=%23%2C%23%230.00%23%23&format[ASK_CA]=%23%2C%23%230.00%23%23&format[HIGH_CA]=%23%2C%23%230.00%23%23%23&format[LOW_CA]=%23%2C%23%230.00%23%23%23&format[TURNOVER_TOTAL]=%23%2C%23%230&format[VOLUME_TOTAL_CA]=%23%2C%23%230&format[TRADES_COUNT]=%23%2C%23%230&format[TRADES_COUNT_TOTAL]=%23%2C%23%230&format[VWAP_CA]=%23%2C%23%230.00%23%23%23&header[DATE]={TICKER}&header[CLOSE_CA]=Siste&header[BID_CA]=Kj%C3%B8per&header[ASK_CA]=Selger&header[HIGH_CA]=H%C3%B8y&header[LOW_CA]=Lav&header[TURNOVER_TOTAL]=Totalt%20omsatt%20%28NOK%29&header[VOLUME_TOTAL_CA]=Totalt%20antall%20aksjer%20omsatt&header[TRADES_COUNT]=Antall%20off.%20handler&header[TRADES_COUNT_TOTAL]=Antall%20handler%20totalt&header[VWAP_CA]=VWAP&view=DELAYED&source=feed.ose.quotes.INSTRUMENTS&filter=ITEM_SECTOR%3D%3Ds{TICKER}.OSE%26%26DELETED!%3Dn1&stop=now&start=1441317600000&space=DAY&ascending=true&filename=data.xlsx'
    
            req = requests.get(csv_url) 
            	        
            url_content = req.content #Get the csv
            	        
            csv_file = open(os.path.join(self.path, f'{TICKER}.xlsx'), 'wb') #Path to save xlsx
            	        
            	        
            csv_file.write(url_content)
            	        
            csv_file.close()
            self.xlsxToCsv(os.path.join(self.path, f'{TICKER}.xlsx'),os.path.join(self.path, f'{TICKER}.csv')) #Converting from xlsx to csv
            print(f'Historical data for {TICKER} downloaded')
            os.remove(os.path.join(self.path, f'{TICKER}.xlsx')) #Deleting the xlsx file
            
    def getFileList(self, extension):
        filenames = []
        
        try:
            for file in [f for f in os.listdir(self.path) if f.endswith('.csv')]:
                filenames.append(os.path.join(self.path, file))
                # print(os.path.join(path, file))
        except FileNotFoundError:
            print(f'File not foud, check the path: {self.path}')
        except:
            print("Unexpected error:", sys.exc_info()[0])
            # print("Error getting the files, check path")
        return filenames
    

    def merge(self, saveFile=False):
    
        print(self.path)
        filenames = self.getFileList(".csv")
        
        # dfs = []
        i=0
        for filename in filenames:
        
            df = pd.read_csv(filename, sep=",") #Read the csv
        
            
            df.iloc[:, 0]= pd.to_datetime(df.iloc[:, 0]) #Convert date to datetime
        
                
            if i == 0: #First run, keep a copy of the df as df2
                df2 = df.copy()
            elif i == 1: #Second run merge df2 with df
                self.stack = pd.concat([df2, df], axis=1)
            else: #After that, just add the new df's to the combined frame
                self.stack = pd.concat([self.stack, df], axis=1)
            i+=1
                
        
        # print(stack.head(5))
        if saveFile:
            self.stack.to_csv(os.path.join(self.path, 'comb', 'bigframe.csv'), sep=";")
        
        
    
    def setPath(self, path):  #To alter the filepath from standar
        self.path = path
    
    def getPath(self):        #Returns the filepath
        return self.path
    
    def downloadData(self):   #Download and save csv files
        # try:
        self.stockDataDownloader(self.path)

        # except:
            # print("Unexpected error:", sys.exc_info()[0])
            # return False
        
    def getData(self):       #Merge all csv's to one df
        try:
            self.merge()
            return self.stack
        except:
            print("Unexpected error:", sys.exc_info()[0])
            return False
        
    def saveData(self):      #Save the df as a csv
        # try:
        self.merge(True)
        return self.stack
        # except:
        #     print("Unexpected error:", sys.exc_info()[0])
        #     return False
    
