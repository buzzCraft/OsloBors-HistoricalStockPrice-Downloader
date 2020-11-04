# -*- coding: utf-8 -*-
"""
A class for handeling stocks

"""

import os
import pandas as pd
import requests
import matplotlib.pyplot as plt
import re
import json
import time as time
import numpy as np

class Stock():
    """ Init with ticker name. If a csv file with the same name as
    the ticker, that csv will be used, and you have to use downloadData() and 
    readData() to get fresh number"""

    def __init__(self, TICKER):

        
        self.TICKER = TICKER                                                   #Set the ticker for instance
        self.url = f'https://www.oslobors.no/ob/servlets/excel?type=history&columns=DATE%2C+CLOSE_CA%2C+BID_CA%2C+ASK_CA%2C+HIGH_CA%2C+LOW_CA%2C+TURNOVER_TOTAL%2C+VOLUME_TOTAL_CA%2C+TRADES_COUNT%2C+TRADES_COUNT_TOTAL%2C+VWAP_CA&format[DATE]=ddd.mm.YY&format[CLOSE_CA]=%23%2C%23%230.00%23%23%23&format[BID_CA]=%23%2C%23%230.00%23%23&format[ASK_CA]=%23%2C%23%230.00%23%23&format[HIGH_CA]=%23%2C%23%230.00%23%23%23&format[LOW_CA]=%23%2C%23%230.00%23%23%23&format[TURNOVER_TOTAL]=%23%2C%23%230&format[VOLUME_TOTAL_CA]=%23%2C%23%230&format[TRADES_COUNT]=%23%2C%23%230&format[TRADES_COUNT_TOTAL]=%23%2C%23%230&format[VWAP_CA]=%23%2C%23%230.00%23%23%23&header[DATE]={self.TICKER}&header[CLOSE_CA]=Siste&header[BID_CA]=Kj%C3%B8per&header[ASK_CA]=Selger&header[HIGH_CA]=H%C3%B8y&header[LOW_CA]=Lav&header[TURNOVER_TOTAL]=Totalt%20omsatt%20%28NOK%29&header[VOLUME_TOTAL_CA]=Totalt%20antall%20aksjer%20omsatt&header[TRADES_COUNT]=Antall%20off.%20handler&header[TRADES_COUNT_TOTAL]=Antall%20handler%20totalt&header[VWAP_CA]=VWAP&view=DELAYED&source=feed.ose.quotes.INSTRUMENTS&filter=ITEM_SECTOR%3D%3Ds{self.TICKER}.OSE%26%26DELETED!%3Dn1&stop=now&start=1441317600000&space=DAY&ascending=true&filename=data.xlsx'
        self.path = os.path.join(os.getcwd(), 'data')                          #Path, could be global?
        self.filepath =  os.path.join(self.path, f'{TICKER}.csv')                   
        if os.path.exists(self.filepath):                                      #Check if we have a csv file with tick name
            print("Data excists, using that file")
            self.readData()                                                    #Load that file
        else:                                                                  #If not, create an empty df, and wait for
            self.data = pd.DataFrame()                                         #downloadData to be called

    
       
    def name(self):
        """ Method to get TICKER name"""
        return self.TICKER

   
    def readData(self):
        """ Method to read data from csv file"""
        self.data = pd.read_csv(self.filepath, sep=",")

        self.data.iloc[:, 0]= pd.to_datetime(self.data.iloc[:, 0]) #Convert date to datetime
        self.data = self.data.sort_values(by='Date')               #Sorting date to get correct plots    
        self.data.set_index('Date',inplace=True)                   #Setting date as index
        self.data = self.data.rename(columns={'Open': f'{self.TICKER} Open'})


    def getData(self):
        """ Return a dataframe with all data"""
        return self.data

    def plotData(self):
        """Method to plot stock price""" 
        # try:                               
        plt.figure(figsize=(16,6))
        plt.plot(self.data['Close'])
        plt.xlabel("date")
        plt.ylabel("price (NOK)")
        plt.title(f"{self.TICKER}  Stock Price (NOK)")
        plt.show()
        # except:
        #     pass
    
    def plotRollingMean(self, *argv):
        """ Metod to plot rolling mean
        
        Take ints for rolling mean:
            stock.plotRollingMean(30,40)
        """

        self.data['Close'].plot(figsize=(16,6))
        for days in argv:
            # plt.plot(self.data.rolling(window=days).mean()[f'{self.TICKER} Last'])
            self.data.rolling(window=days).mean()['Close'].plot()
        plt.show()
        
    def downloadData(self, start_date, stop_date):
        """ Pass date as 'YYYY-MM-DD' """
        inicial = start_date
        final = stop_date
    
        start = int(time.mktime(time.strptime(str(inicial), '%Y-%m-%d'))) # convertir fechas
        end = int(time.mktime(time.strptime(str(final), '%Y-%m-%d')))
    
        data = self.downloadFromYahoo(self.TICKER,start,end)
        data = data.decode('utf-8')
        with open(os.path.join(self.path, f'{self.TICKER}.csv'), "w") as dataLine:
            dataLine.writelines(str(data))
       
    def downloadFromYahoo(self, symbol, start, end):
       ses = requests.session()
       resp = ses.get(
           f'https://finance.yahoo.com/quote/{self.TICKER}/history?period1={start}&period2={end}&interval=1d&filter=history&frequency=1d'
       )
       resp.raise_for_status()
       data = resp.content.decode('utf-8')
       crumb_m = re.search(r'"CrumbStore":\{"crumb":("[^"]+")\}', data)
       assert crumb_m
       crumb = json.loads(crumb_m.group(1))
       csvresp = ses.get(
           f'https://query1.finance.yahoo.com/v7/finance/download/{self.TICKER}?period1={start}&period2={end}&interval=1d&events=history&crumb={crumb}'
       )
       csvresp.raise_for_status()
       #print(type(csvresp))
       return csvresp.content 

    # def updateData(self):
    
    def showData(self):
        
        print(self.data['Close'])   
    
    def fixNa(self):
        

        self.data.replace("null", np.nan, inplace=True) #Replacing 0 with NaN
        self.data.fillna( method ='ffill', inplace = True) #Filling with data from next day
        
        # df.dropna(inplace=True)  #Dropping all columns with NaN


        
        
      #need to fix null values. Thinking about doing day_before + day_after / 2 or maybe just remove?      


if __name__ == "__main__":
    test = Stock("XXL.OL")
    #print(test.getTICKER())
    test.downloadData("2010-01-01", "2020-10-28")
    test.readData()
    test.fixNull()
    print(test.data.tail())
    test.showData()
    test.plotRollingMean(10,20,60)
    

