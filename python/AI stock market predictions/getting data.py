import yfinance as yf
import pandas as pd
#get S&P500 data
SPY = yf.Ticker("SPY")
hstory = SPY.history(period="MAX", interval="1d")
df = hstory.drop(columns=['Dividends', 'Stock Splits', 'Capital Gains'], axis=1)
df.to_csv('SPY.csv', encoding='utf-8')