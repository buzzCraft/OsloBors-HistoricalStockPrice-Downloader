# OsloBors HistoricalStockPrice Downloader
 A simple script that downloads historical stock data from OsloBørs and save it in separate csv files


## Usage
Run the script and it will start download csv files from https://www.oslobors.no/
Change the Tick.csv file if you need a smaller selection of stocks

### First run:
    You need to have a folder called /data/comb/
    in the same folder you have the python files in

### Usage:
    downloader.stockDataDownloader() take save file path as argument, and download
    xlsx files from OsloBors, it then convert these files to csv and delete the xlsx files
    
    merger.merge() take the path of the saved csv's and merge them into one big df, if set to
    True, it also save a csv version of the df to /data/comb/. I find this usefull when doing
    quick checkups on the data.
    
## Plans:
    Im planning to make a downloader class and a much more generic datawrangler class, and at the
    same time create a stock class.

## Disclaimer
The script will create some server traffic, and running it multiple times, might be
seen as a (poor) DDOS attack. Please use it responsibly



csv_url=f'https://www.oslobors.no/ob/servlets/excel?type=history&columns=DATE%2C+CLOSE_CA%2C+BID_CA%2C+ASK_CA%2C+HIGH_CA%2C+LOW_CA%2C+TURNOVER_TOTAL%2C+VOLUME_TOTAL_CA%2C+TRADES_COUNT%2C+TRADES_COUNT_TOTAL%2C+VWAP_CA&format[DATE]=ddd.mm.YY&format[CLOSE_CA]=%23%2C%23%230.00%23%23%23&format[BID_CA]=%23%2C%23%230.00%23%23&format[ASK_CA]=%23%2C%23%230.00%23%23&format[HIGH_CA]=%23%2C%23%230.00%23%23%23&format[LOW_CA]=%23%2C%23%230.00%23%23%23&format[TURNOVER_TOTAL]=%23%2C%23%230&format[VOLUME_TOTAL_CA]=%23%2C%23%230&format[TRADES_COUNT]=%23%2C%23%230&format[TRADES_COUNT_TOTAL]=%23%2C%23%230&format[VWAP_CA]=%23%2C%23%230.00%23%23%23&header[DATE]={TICKER}&header[CLOSE_CA]=Siste&header[BID_CA]=Kj%C3%B8per&header[ASK_CA]=Selger&header[HIGH_CA]=H%C3%B8y&header[LOW_CA]=Lav&header[TURNOVER_TOTAL]=Totalt%20omsatt%20%28NOK%29&header[VOLUME_TOTAL_CA]=Totalt%20antall%20aksjer%20omsatt&header[TRADES_COUNT]=Antall%20off.%20handler&header[TRADES_COUNT_TOTAL]=Antall%20handler%20totalt&header[VWAP_CA]=VWAP&view=DELAYED&source=feed.ose.quotes.INSTRUMENTS&filter=ITEM_SECTOR%3D%3Ds{TICKER}.OSE%26%26DELETED!%3Dn1&stop=now&start=1441317600000&space=DAY&ascending=true&filename=data.xlsx'