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

## Disclaimer
The script will create some server traffic, and running it multiple times, might be
seen as a (poor) DDOS attack. Please use it responsibly

