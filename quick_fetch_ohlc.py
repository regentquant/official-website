import yfinance as yf
from datetime import datetime, timedelta

# Define the ticker symbol
ticker_symbol = input("Ticker:")
start_date = "2023-01-03"
end_date_str = "2023-11-10"
# Add one day
end_date_str = (datetime.strptime(end_date_str, "%Y-%m-%d") + timedelta(days=1)).strftime("%Y-%m-%d")
# Get data on this ticker
ticker_data = yf.Ticker(ticker_symbol)

# Get the historical prices for this ticker
ticker_df = ticker_data.history(period='1d', start=start_date, end=end_date_str)

# Extract and save dates and OHLC data to separate lists
dates = ticker_df.index.tolist()
open_prices = ticker_df['Open'].tolist()
high_prices = ticker_df['High'].tolist()
low_prices = ticker_df['Low'].tolist()
close_prices = ticker_df['Close'].tolist()

fs = ''

for o,h,l,c in zip(open_prices,high_prices,low_prices,close_prices):
  fs = f"{fs}{round(o,2)}\t{round(h,2)}\t{round(l,2)}\t{round(c,2)}\n"


import pyperclip
pyperclip.copy(fs)
