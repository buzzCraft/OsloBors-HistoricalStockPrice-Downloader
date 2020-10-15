# -*- coding: utf-8 -*-
"""
A class for handeling stocks

"""

import os
import pandas as pd
import requests
import matplotlib.pyplot as plt

class Stock():
    """ Init with ticker name. If a csv file with the same name as
    the ticker, that csv will be used, and you have to use downloadData() and 
    readData() to get fresh number"""

    def __init__(self, TICKER):

        
        self.TICKER = TICKER                                                   #Set the ticker for instance
        self.url = f'https://www.oslobors.no/ob/servlets/excel?type=history&columns=DATE%2C+CLOSE_CA%2C+BID_CA%2C+ASK_CA%2C+HIGH_CA%2C+LOW_CA%2C+TURNOVER_TOTAL%2C+VOLUME_TOTAL_CA%2C+TRADES_COUNT%2C+TRADES_COUNT_TOTAL%2C+VWAP_CA&format[DATE]=ddd.mm.YY&format[CLOSE_CA]=%23%2C%23%230.00%23%23%23&format[BID_CA]=%23%2C%23%230.00%23%23&format[ASK_CA]=%23%2C%23%230.00%23%23&format[HIGH_CA]=%23%2C%23%230.00%23%23%23&format[LOW_CA]=%23%2C%23%230.00%23%23%23&format[TURNOVER_TOTAL]=%23%2C%23%230&format[VOLUME_TOTAL_CA]=%23%2C%23%230&format[TRADES_COUNT]=%23%2C%23%230&format[TRADES_COUNT_TOTAL]=%23%2C%23%230&format[VWAP_CA]=%23%2C%23%230.00%23%23%23&header[DATE]={self.TICKER}&header[CLOSE_CA]=Siste&header[BID_CA]=Kj%C3%B8per&header[ASK_CA]=Selger&header[HIGH_CA]=H%C3%B8y&header[LOW_CA]=Lav&header[TURNOVER_TOTAL]=Totalt%20omsatt%20%28NOK%29&header[VOLUME_TOTAL_CA]=Totalt%20antall%20aksjer%20omsatt&header[TRADES_COUNT]=Antall%20off.%20handler&header[TRADES_COUNT_TOTAL]=Antall%20handler%20totalt&header[VWAP_CA]=VWAP&view=DELAYED&source=feed.ose.quotes.INSTRUMENTS&filter=ITEM_SECTOR%3D%3Ds{self.TICKER}.OSE%26%26DELETED!%3Dn1&stop=now&start=1441317600000&space=DAY&ascending=true&filename=data.xlsx'
        self.path = os.path.join(os.getcwd(), 'data')                          #Path, could be global?
        self.filepath =  os.path.join(self.path, f'{TICKER}.csv') 
        self.date = False                    
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
        if self.date:
            self.data.iloc[:, 0]= pd.to_datetime(self.data.iloc[:, 0]) #Convert date to datetime
            self.data.info()
    def getData(self):
        """ Return a dataframe with all data"""
        return self.data

    def plotData(self):
        """Method to plot stock price""" 
        try:                               
            plt.figure(figsize=(10,10))
            plt.plot(self.data["Date"], self.data[f'{self.TICKER} Last'])
            plt.xlabel("date")
            plt.ylabel("price (NOK)")
            plt.title(f"{self.TICKER}  Stock Price (NOK)")
            plt.show()
        except:
            pass



    def downloadData(self, date=True):                                        #Set date = True for one file that have 5 yr of data                                      
        """Method to download data if needed"""
        self.date=date
        req = requests.get(self.url)                                           #Request the dataset from url
        	        
        url_content = req.content                                              #Get the xlsx
        	        
        xlsx_file = open(os.path.join(self.path, f'{self.TICKER}.xlsx'), 'wb') #Path to save xlsx
        xlsx_file.write(url_content)                                           #Write data to file
        xlsx_file.close()                                                      #Close the file
        

        self.xlsxToCsv() #Converting from xlsx to csv
        print(f'Historical data for {self.TICKER} downloaded')
        os.remove(os.path.join(self.path, f'{self.TICKER}.xlsx'))              #Deleting the xlsx file
        

    def xlsxToCsv(self):  
        """Method to convert from xlsx to csv"""
        xfile = os.path.join(self.path, f'{self.TICKER}.xlsx')                 #Path to original xlsx file
        cfile = os.path.join(self.path, f'{self.TICKER}.csv')                  #Path to save csv file
        print(f'Converting {xfile} to csv file')                               #Output                         
        read_file = pd.read_excel(xfile)                                       #Read xlsx file
                                                                               #Rename columns
        read_file.rename(columns={'Siste': f'{self.TICKER} Last', 'Kjøper': 'Buy', 'Selger' : 'Sell', 'Høy' : 'High', 'Lav' : 'Low', 'Totalt omsatt(NOK)' : 'Total traded(NOK)', 'Totalt antall aksjer omsatt' : 'Volume', 'Antall off. handler' : 'Public trades', 'Antall handler totalt' : 'All trades'}, inplace=True)
        if not self.date:                                                           #Drop the date column if date=False
            read_file.drop(read_file.columns[0], axis=1, inplace=True)
        else:
            read_file.rename(columns={f'{self.TICKER}': 'Date'}, inplace=True) #Rename and keep date if date=True   
        read_file.to_csv (cfile, index = None, header=True)

if __name__ == "__main__":
    test = Stock("XXL")
    print(test.getTICKER())
    # test.downloadData()
    test.readData()
    print(test.data.tail())
    test.plotData()
    

