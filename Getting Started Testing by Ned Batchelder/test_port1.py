# test_port1.py

import unittest
from Portfolio import Portfolio


class PortfolioTest(unittest.TestCase):
    def test_empty(self):
        p = Portfolio()
        self.assertEqual(p.cost(), 0.0)

    def test_buy_one_stock(self):
        p = Portfolio()
        p.buy("IBM", 100, 176.48)
        self.assertEqual(p.cost(), 17648.0)

    def test_buy_two_stock(self):
        p = Portfolio()
        p.buy("IBM", 100, 176.48)
        self.assertEqual(p.cost(), 17648.0)

        p.buy("HPQ", 100, 36.15)
        self.assertEqual(p.cost(), 21263.0)

    def test_assert_exception(self):
        '''
        TypeError: buy() missing 2 required positional arguments: 'shares' and 'price'
        '''
        p = Portfolio()
        with self.assertRaises(TypeError):
            p.buy(p.cost())
