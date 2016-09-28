class Portfolio(object):
    def __init__(self):
        self.stocks = []

    def buy(self, name, shares, price):
        self.stocks.append([name, shares, price])

    def cost(self):
        amt = 0.0
        for name, share, price in self.stocks:
            amt += share * price
        return amt

if __name__ == '__main__':
    p = Portfolio()
    assert(p.cost() == 0)

    p.buy("IBM", 100, 176.48)
    assert(p.cost() == 17648.0)

    p.buy("HPQ", 100, 36.15)
    assert(p.cost() == 21263.0)
