import sys
# put here the path to project on your computer
sys.path.append('/Users/ben/Documents/code/monteCarloOptionPricing/')
from pricer.stock.stock import Stock

class Derivative():
    def __init__(self, S0, vol, mean, N, delta):
        self.stock = Stock(S0, vol, mean, N, delta)

    def payoffFunction(self, stock):
        raise NotImplementedError

    def payoff(self):
        return self.payoffFunction(self.stock)
