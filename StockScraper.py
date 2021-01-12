#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
This module scraps the data from yahoo finance and presents the stock data of the given company for today.
"""
import yfinance as yf
import datetime
import sys
from get_all_tickers import get_tickers as gt
import PySimpleGUI as gui

class PopWindow:
    def show_results(self, contents, title):
        """
            This method takes in two string: contents and title.
            A popup window will be presented to show the contents and the title.
        """
        gui.Popup(contents, title=title, font=("Helvetica", 20), line_width=300)


    def show_error(self, exceptionMessage):
        """
            This method takes in a string: exceptionMessage.
            A popup window will be presented to show the exception message.
        """
        gui.Popup(exceptionMessage, title="ERROR!", font=("Helvetica", 25))

class StockDataScraper:
    def __init__(self, tick):
        """
            The constructor takes in a stock tick symbol and 
            initialize the member variables if the symbol is valid.
            If the symbol is invalid, an exception will be raised.
        """
        tickerList = set(gt.get_tickers())
        if tick not in tickerList:
            errorMessage = "Invalid stock tick symbol {}, please double check.".format(tick)
            raise Exception(errorMessage)
        self.stock = yf.Ticker(tick)
        self.tick = tick



    def get_data_at_date(self, dateNow):
        """
            This method takes in a date dateNow
            and returns a dictionary containing the data of the stock self.tick.
            Specifically, the return dictionary includes the following keys:
            Date, Tick, Name, Open, Low, High, Close.
            If the data cannot be retrieved, an exception will be raised.
        """
        prices = self.stock.history('period=1day', start = dateNow) #start = datetime.datetime.today() - datetime.timedelta(days=2))
        if prices.empty:
            raise Exception("No data for today's prices is found.")
        #extract today's data
        dataDate = prices.index.to_pydatetime()
        if len(dataDate)==0:
            raise Exception("No data for today's prices is found.")
        result = {}
        #check whether the first date is today
        todayInStr = dateNow.strftime("%Y-%m-%d")
        dataDateInStr = dataDate[0].strftime("%Y-%m-%d")
        if dataDateInStr != todayInStr:
            pass
            #raise Exception("No data for today's prices is found.")
        #put the data into the result dict
        result['Date'] = dataDateInStr
        result['Tick'] = self.tick
        result['Name'] = self.stock.info['shortName']
        result['Open'] = format(float(prices['Open'][0]), '.2f')
        result['Low'] = format(float(prices['Low'][0]), '.2f')
        result['High'] = format(float(prices['High'][0]), '.2f')
        result['Close'] = format(float(prices['Close'][0]), '.2f') #what happens if the stock is not closed today yet?
        return result

    def get_string_from_data(self,stockData):
        """
            This method takes in a dictionary containing the following keys:
            Date, Tick, Name, Open, Low, High, Close.
            It returns a string contentStr formatted for printing or displaying
            and a string title including the stock tick symbol.
        """
        contentStr = 'Name        {} ({})\n'.format(stockData['Name'], stockData['Tick'])\
            +'Date        {}\n'.format(stockData['Date'])\
            +'High        ${}\n'.format(stockData['High'])\
            +'Low         ${}\n'.format(stockData['Low'])\
            +'Open        ${}\n'.format(stockData['Open'])\
            +'Close       ${}\n'.format(stockData['Close'])

        title = '{}'.format(stockData['Tick'])
        return (contentStr, title)



if __name__ == '__main__':
    #get the company id from the command line arguments
    stockId = 'ISRG'
    if len(sys.argv)>=2:
        stockId = sys.argv[1]
    UI = PopWindow()
    try:
        stockInfo = StockDataScraper(stockId)
        data = stockInfo.get_data_at_date(datetime.datetime.today())
        #data = stockInfo.get_data_at_date(datetime.datetime(2021, 1, 8))
        (content, title) = stockInfo.get_string_from_data(data)
        UI.show_results(content, title)
    except Exception as e:
        UI.show_error(e)
        exit(1)

