#!/usr/bin/env python
# Initial testing to get stock quotes and whatnot

from yahoo_finance import Share

syms = ['NFLX', 'AMZN', 'DRYS', 'NOVN', 'UAA', 'F', 'AAPL']

class TickerInfo():
    def __init__(self, symbols):
        if isinstance(symbols, list): 
            self.stocks_that_matter = symbols
        else:
            raise TypeError
        self.stock_objects = []

        for stock in self.stocks_that_matter:
            stockObject = Share(stock)
            self.stock_objects.append(stockObject)

if __name__ == '__main__':
    t = TickerInfo(syms)
    if len(t.stock_objects) > 0:
        print '%-30s  %-9s' % ('Name', 'Price ($)')
        for sObj in t.stock_objects:
            print '%-30s  %-9s' % (sObj.get_name(), sObj.get_price())

