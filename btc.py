import numpy as np
import numpy_financial as npf
import matplotlib.pyplot as plt
import yfinance as yf

#price for 2018-2021
#bitcoin = [3869.47, 7188.46, 22203.31, 29391.78]

#print(np.std(bitcoin))


#birr = [-5000, 386.947, 718.846, 2220.331, 2939.178]

#print (np.irr(birr))


#xbtc = 1000 / bitcoin[0]
#bbtc = np.multiply(bitcoin, xbtc)


#year=[2018,2019,2020,2021]
#plt.plot(year,bbtc)
#plt.savefig('plot.png')


data = yf.Ticker('BTC-USD')
x = data.history(start='2020-10-12',end='2021-10-12')['Close']
start = 1000 / x[0]
y = np.multiply(start, x)
plt.plot(y)
plt.savefig('plot.png')

z = data.history('1y')['Close']
ret = z
zrisk = np.std(ret) * np.sqrt(252)
zsharp = (np.mean(ret) / np.std(ret))*np.sqrt(252)

print("Risk", zrisk)
print("Sharpe", zsharp)
