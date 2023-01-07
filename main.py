import pandas as pd
import pandas_datareader.data as web
import matplotlib.pyplot as plt
import numpy as np
import pprint as p


# plt.bar(up.index,up.close-up.open,bottom=up.open,color)
# “up” dataframe will store the stock_prices when the closing stock price is greater than or equal to the opening stock prices
# plt.bar(down.index,down.close-down.open,bottom=down.open,color)
# “down” dataframe will store the stock_prices when the closing stock price is lesser than the opening stock prices




start = '2022-12-06'
end = "2023-01-06"
stock = 'GLYC'
s = web.DataReader(stock, 'stooq', start=start, end=end)
# s.to_csv(f"{stock}.csv")
# stock_prices = pd.read_csv('GLYC.csv')
stock_prices = pd.DataFrame(s)


# dates = stock_prices['Date']
close = stock_prices['Close']
opening = stock_prices['Open']
volume = stock_prices['Volume']

plt.figure()

up = stock_prices[close >= opening]
down = stock_prices[close < opening]

col1 = 'red'
col2 = 'green'

width = 0.3
width2 = 0.03
def bar_chart():
    plt.bar(up.index, up.Close-up.Open, width, bottom=up.Open, color=col1)
    plt.bar(up.index, up.High-up.Close, width2, bottom=up.Close, color=col1)
    plt.bar(up.index, up.Low-up.Open, width2, bottom=up.Open, color=col1)

    plt.bar(down.index, down.Close-down.Open, width, bottom=down.Open, color=col2)
    plt.bar(down.index, down.High-down.Open, width2, bottom=down.Open, color=col2)
    plt.bar(down.index, down.Low-down.Close, width2, bottom=down.Close, color=col2)
    plt.xticks(rotation=30, ha='right')
    

bar_chart()

plt.show()




