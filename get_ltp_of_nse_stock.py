import nsepy as nse
import time
def LTP(symbol):
    market = nse.get_quote(symbol = symbol)
    return market['data'][0]['lastPrice']
symbol = input('Enter stock symbol: ')
for _ in range(5):
    print(LTP(symbol))
    time.sleep(5)
