import yfinance as yf
import streamlit as st
import pandas as pd

st.write("""
# Simple Stock Price App
Shown are the stock **closing price** and **volume** of Google!
""")

#define the ticker symbol
tickerSymbol = 'GOOGL'

#Get data from this ticker
tickerData = yf.Ticker(tickerSymbol)

#Get the historical prices for this ticker
tickerDf = tickerData.history(period='1d', start='2023-01-16', end='2024-01-16')

#Open High Low Close Volume Dividends Stock Splits

st.write("""
## Closing Price
""")
st.line_chart(tickerDf.Close)

st.write("""
## Volume Price
""")
st.line_chart(tickerDf.Volume)