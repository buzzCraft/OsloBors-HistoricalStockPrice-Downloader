# OsloBors HistoricalStockPrice Downloader
 A simple script that downloads historical stock data from OsloBørs and save it in separate csv files


## Usage
Run the script and it will start download csv files from https://www.oslobors.no/
Change the Tick.csv file if you need a smaller selection of stocks


### Usage:
    Run main.py. It will download all the files and convert them to a class obj and convert the files
    to csv in /data/
    You can then use merger.merge() and pass a list of obj to create a merged data set to be saved
    in data/comb/
    
    
## Issues:
	-The Stock.plotData() eats memory
	-The dates on Stock.plotData don't make sense in the plot (adjust xticks)

## Plans:
	* Make a class for merged file to get easier access
	* Do some more data wrangeling before combining
	* Add more functions to stock class
	* and more...

## Disclaimer
The script will create some server traffic, and running it multiple times, might be
seen as a (poor) DDOS attack. Please use it responsibly

