#StockScraper
The application takes in a stock tick symbol and returns the stock's high, low, open and close prices today.

author: Guangli Dai

##Pre-requisites
The python version used is Python 3.8.
The following packages are required (also given in requirements.txt):

- certifi==2020.12.5
- chardet==4.0.0
- get-all-tickers==1.7
- idna==2.10
- lxml==4.6.2
- multitasking==0.0.9
- numpy==1.19.5
- pandas==1.2.0
- PySimpleGUI==4.33.0
- python-dateutil==2.8.1
- pytz==2020.5
- requests==2.25.1
- six==1.15.0
- urllib3==1.26.2
- yfinance==0.1.55


##Usage
To install the pre-requisites using requirements.txt:
```
pip install -r requirements.txt
```
A simple way to run the application and to run the unit tests:
```
python3 StockScraper.py ISRG
python3 UniTest.py #used to run the unit tests
```

##Architecture of the Application

The application is implemented in StockScraper.py, which includes two classes and a main function.

- Class StockDataScraper is used to scrape the data of a given date with a given stock tick symbol. It includes three methods.
		1. \_\_init\_\_(self, tick): The constructor takes in a stock tick symbol and initialize the member variables if the symbol is valid. If the symbol is invalid, an exception will be raised.
		2. get_data_at_date(self, dateNow): This method takes in a date dateNow and returns a dictionary containing the data of the stock self.tick. Specifically, the return dictionary includes the following keys: Date, Tick, Name, Open, Low, High, Close. If the data cannot be retrieved, an exception will be raised.
		3. get_string_from_data(self,stockData): This method takes in a dictionary containing the following keys: Date, Tick, Name, Open, Low, High, Close. It returns a string contentStr formatted for printing or displaying and a string title including the stock tick symbol.
	
- Class PopWindow is used to present the contents or error messages in a popup window. It includes two methods:
		1. show_results(self, contents, title): This method takes in two string: contents and title. A popup window will be presented to show the contents and the title.
		2. show_error(self, exceptionMessage): This method takes in a string: exceptionMessage. A popup window will be presented to show the exception message.

- The main function takes in the stock tick symbol from the command line arguments. If none is given, a default stock stick symbol, i.e., ISRG, will be used. It then retrieves the data for today with class StockDataScraper and presents it using class PopWindow.




###Inputs

- Inputs are given as command line arguments.
- The input should be a valid stock tick symbol (capital-sensitive).
- If no inputs are given, a default stock stick symbol, i.e., ISRG, will be used.

###Outputs

- The application presents the result or the error message in a popup window.
- Data presented includes the stock's high, low, open and close prices today.

###Exception Handling

The current version of StockScraper will show a popup window with warning messages regarding the following erros confronted:

- Invalid stock tick symbol.
- Cannot access the information for today's prices of the given stock. The reason may be that the network connection fails or that the stock information today is not available in the target database.


##Other files in the directory

- UniTest.py: This file includes the unit tests for the methods in StockScraper.py

- ArchitectureDiagram.png: The diagram shows the architecture of the application.


