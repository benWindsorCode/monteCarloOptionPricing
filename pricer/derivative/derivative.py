import sys
# put here the path to project on your computer
sys.path.append('/Users/ben/Documents/code/monteCarloOptionPricing/')
from pricer.stock.stock import Stock
import numpy as np

class Derivative():

    # number of iterations to run in monte carlo sim
    iter = 8000

    def __init__(self, S0, vol, mean, N, delta, r):
        self.r = r
        self.T = N*delta
        self.stock = Stock(S0, vol, mean, N, delta)

    # for each derivative child class to implement
    def payoffFunction(self, stock):
        raise NotImplementedError

    def payoff(self):
        return self.payoffFunction(self.stock)

    def price(self):
        payoffs = [self.payoff() for i in range(self.iter)]
        avg = np.sum(payoffs)/self.iter
        return np.exp(-1*self.r*self.T)*avg
