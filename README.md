# OsloBors HistoricalStockPrice Downloader
 A simple script that downloads historical stock data from OsloBørs and save it in separate csv files


## Usage
    Run main.py. It will download all the files and convert them to a class obj and convert the files
    to csv in /data/
    You can then use merger.merge() and pass a list of obj to create a merged data set to be saved
    in data/comb/
    
    
## Issues:
	-Date come as duplicate in the combined dataset. Before just removing it I must find a way 
	to keep the dates from the last 5 yrs, since not all stocks have been on OBX for 5 years

## Plans:
	* Make a class for merged file to get easier access
	* Do some more data wrangeling before combining
	* Add more functions to stock class
	* and more...

## StockClass
	The StockClass is a class to download and manipulate stock data.
	It take TICKER as input ('XXL')

Methods

	name() - Returns the ticker

	downloadData() - Download a xlsx from Oslobors, converts it to csv and delete the xlsx file

	xlsxToCsv() - Helper method for downloadData()

	getData() - Returns a pandas dataframe with all data

	readData() - Read the data from a csv, convert date to datetime and sort
	the file with respect to accending date

	plotData() - Plot the stock closing price

	plotRollingMean(*argv) - Plot stock closing price and rollingMean for 
	the days passed in *argv: plotRollingMean(10,40,60) - will give a plot with four lines
	(the lines do not have labels atm)




## Disclaimer
The script will create some server traffic, and running it multiple times, might be
seen as a (poor) DDOS attack. Please use it responsibly

