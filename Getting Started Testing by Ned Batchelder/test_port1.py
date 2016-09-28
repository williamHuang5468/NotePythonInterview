# test_port1.py

import unittest
from Portfolio import Portfolio


class PortfolioTest(unittest.TestCase):
    def test_buy_one_stock(self):
        p = Portfolio()
        p.buy("IBM", 100, 176.48)
        assert(p.cost() == 17648.0)
