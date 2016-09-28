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

    def sell(self, name, shares):
        for holding in self.stocks:
            if holding[0] == name:
                if holding[1] < shares:
                    raise ValueError("No enought shares")
                holding[1] -= shares
                break
        else:
            raise ValueError("You don't own that stock")
