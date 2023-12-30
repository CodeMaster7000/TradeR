import time
import yfinance as y
from win10toast import ToastNotifier

stock_symbol = "XXXX" # Change stock symbol here
threshold_percentage = 0.005 # Change threshold percentage here
toaster = ToastNotifier()

initial_data = y.download(stock_symbol, period="1d")
initial_price = initial_data["Close"].iloc[0]

while True:
    try:
        current_data = y.download(stock_symbol, period="1d")
        current_price = current_data["Close"].iloc[-1]

        price_diff_percentage = ((current_price - initial_price) / initial_price) * 100
        if price_diff_percentage <= -threshold_percentage:
            message = f"Stock price for {stock_symbol} has decreased by {price_diff_percentage:.2f}%. Current Price: {current_price}"
            toaster.show_toast("Stock Alert", message, duration=10)
        time.sleep(360)

    except Exception as e:
        print("An error occurred:", str(e))
        break
