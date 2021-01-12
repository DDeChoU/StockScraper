#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
This file includes differents tests of classes in StockScraper.py
"""
from StockScraper import StockDataScraper
from StockScraper import PopWindow
import datetime

def test_init():
    try:
        #Test two stock tick symbol: 'A' and 'ISRG'. Both are valid and the initialization should succeed.
        stockA = StockDataScraper('A')
        assert stockA, "The initialization using stock tick symbol 'A' fails and no exception is raised."
        stockISRG = StockDataScraper('ISRG')
        assert stockISRG, "The initialization using stock tick symbol 'ISRG' fails and no exception is raised."
        
        #'I' is not a valid stock tick symbol, should cause an exception.
        stockInvalid = StockDataScraper('I')
        assert True, "The invalid stock tick symbol does not cause an exception as expected."
    except Exception as e:  
        targetErrorString = "Invalid stock tick symbol I"
        assert targetErrorString in str(e),\
            "Exception message different from the expectation. The exception message is: {}"\
            .format(str(e))
    print('Initialization Test Passed.')

def test_get_data():
    try:
        stockISRG = StockDataScraper('ISRG')
        #check teh price at 2020-Jan-8th. The value should be the same as expected.
        result = stockISRG.get_data_at_date(datetime.datetime(2021, 1, 8))
        assert result['Date']=='2021-01-08', 'Date of data retrieved is wrong.'
        assert result['High']=='825.39', 'High price retrieved is wrong.'
        assert result['Low']=='804.06', 'Low price retrieved is wrong.'
        assert result['Open']=='804.22', 'Open price retrieved is wrong.'
        assert result['Close']=='818.75', 'Close price retrieved is wrong.'
        assert result['Name']=='Intuitive Surgical, Inc.', 'Company name retrieved is wrong.'

        #check the data at 2020-Jan-9th. Should throw an exception because it is Saturday.
        result = stockISRG.get_data_at_date(datetime.datetime(2021, 1, 9))
        assert True, 'The attempt to get prices at invalid dates do not throw exception as expected.'
    except Exception as e:
        targetErrorString = "No data for today's prices is found."
        assert targetErrorString in str(e),\
            "Exception message different from the expectation. The exception message is: {}"\
            .format(str(e))
    print('Get Data Test Passed.')

def test_pop_windows():
    #should see two UI showing testing information
    testWindow = PopWindow()
    testWindow.show_results('Test Contents.', 'Test Title')
    testWindow.show_error('Test Exception Message.')
    print('Pop Window Test Passed.')

if __name__ =='__main__':
    try:
        test_init()
        test_get_data()
        test_pop_windows()
    except AssertionError as e:
        print(e)
        print("Test Case Failed.")
