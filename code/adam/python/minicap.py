# Mini-Capstone

import pandas as pd
import pandas_datareader as pdr
import pandas_datareader.data as web
import datetime
import matplotlib.pyplot as plt
# from secrets import fred_api_key

 #PAYEMS WPSFD4131 MEHOINUSA672N CPILFESL
# get economic data from Federal Reserve Economic Data api
def fred_get(start, end):
    series1 = input('Enter the series name for economic data: ').upper()
    df1 = pdr.DataReader(series1, 'fred', start, end)
    return df1

# get historical stock prices from yahoo of adjusted close price
def stock_get(start, end):
    stock_ticker = input('Enter the stock ticker to compare: ').upper()
    df_stk = web.DataReader(stock_ticker, 'yahoo', start, end)['Adj Close']
    return df_stk

# plot 2 graphs of data sets with shared time axis
def plot_graphs(df1, df_stk):
    fig, axes = plt.subplots(2,1,sharex=True)
    df1.plot(ax=axes[0])
    df_stk.plot(ax=axes[1])
    plt.show()

# plot single set of data across specified time
def plot_graph1(df):
    df.plot()
    plt.show()

# get start year and month of data from user
def get_time_start():
    start_year = int(input('Enter the start year: '))
    while True:
        if start_year < 1920 or start_year > 2022:
            start_year =int(input('Please enter a start year between 1920-2022: '))
        else:
            break
    start_month = int(input('Enter the start month (1-12): '))
    start = datetime.date (start_year, start_month, 1)
    return start
# get end year and month of data from user
def get_time_end():
    end_year = int(input('Enter the ending year: '))  
    end_month = int(input('Enter the end month (1-12): '))
    end = datetime.date (end_year, end_month, 1)
    while True:
        if end.year == start.year and end.month < start.month:
            print('End date must be after Start date')
            end_year = int(input(f'Please enter an end year after the start date "{start}": '))
            end_month = int(input(f'Please enter a month after the start date "{start}": '))
        if end.year < start.year:
            print('End date must be after Start date')
            end_year = int(input(f'Please enter an end year after the start date "{start}": '))
            end_month = int(input(f'Please enter a month after the start date "{start}": '))
        else:
            break
    return end

# df_stk = stock_get(start, end)
# df1 = fred_get(series1, start, end)
# plot_graphs(df1, df_stk)

# indv_fred = input('Would you like to see the FRED data by itself [y]es or [n]o: ').upper()
# if indv_fred == 'Y':
#     df1 = fred_get(start, end)
#     df1.plot()
#     plt.show()
# else:
#     print('Thank you.')

while True:
    q1 = input(f'''What types of data would you like to compare:
    Economic Data and Stock Price [1]
    Economic Data and Economic Date [2]
    Stock Price and Stock Price [3]
    Just Stock Price [4]
    Just Economic Data [5]
    [0] to quit
    : ''')
    if q1 == '0':
        break
    if q1 == '1':
        print('\nComparing Federal Economic Indicator Data with a Stock closing price:')
        start = get_time_start()
        end = get_time_end()
        df1 = fred_get(start, end)
        df_stk = stock_get(start, end)
        plot_graphs(df1, df_stk)
    if q1 == '2':
        print('\nComparing an Economic Indicator with another Economic Indicator:')
        start = get_time_start()
        end = get_time_end()
        df1 = fred_get(start, end)
        df2 = fred_get(start, end)
        plot_graphs(df1, df2)
    if q1 == '3':
        print('\nComparing an Stock closing price with another Stock closing price:')
        start = get_time_start()
        end = get_time_end()
        df_stk = stock_get(start, end)
        df_stk2 = stock_get(start, end)
        plot_graphs(df_stk, df_stk2)
    if q1 == '4':
        print('\nGraph of Stock Closing price over specified time:')
        start = get_time_start()
        end = get_time_end()
        df_stk = stock_get(start, end)
        plot_graph1(df_stk)
    if q1 == '5':
        print('\nGraph of Economic indicator over specified time:')
        start = get_time_start()
        end = get_time_end()
        df1 = fred_get(start, end)
        plot_graph1(df1)

        

## Collects 2 series using datareader and plots both series on same graph
# series1 = 'CPIAUCSL'
# series2 = 'CPILFESL'
# inflation = web.DataReader([series1, series2], 'fred', start, end)
# inflation.head()
# print(inflation)
# inflation.plot()
# plt.show()