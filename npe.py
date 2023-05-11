import numpy as np
import yfinance as yf

msft = yf.Ticker("MSFT")
print(msft.history(period="1mo"))

x = [2, 3, 4, 5, 6]
nums = np.array([2, 3, 4, 5, 6])
num3 = nums * 2
print(num3)
