import yfinance as yf
import pandas as pd
import streamlit as st


st.write("""
# Apple Stock Price App
below is the stock price of apple.inc showing its **closing price** and ***Volume*** of the Apple stocks

""")
#Define specific stock symbol
ticker_symbol = 'AAPL'
#get data for this symbol
ticker_name = yf.Ticker(ticker_symbol)
#fetch historical data for the Ticker symbol
ticker_df = ticker_name.history(period='id', start='2021-11-18', end ='2022-06-19')

st.write("""
## Closing Price""")

st.line_chart(ticker_df.Close)

st.write("""
## Volume Price""")
st.line_chart(ticker_df.Volume)