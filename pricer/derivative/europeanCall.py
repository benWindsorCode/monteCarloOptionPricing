from derivative import Derivative

class EuropeanCall(Derivative):
    def __init__(self, S0, vol, mean, N, delta, r, strike):
        Derivative.__init__(self, S0, vol, mean, N, delta, r)
        self.strike = strike

    def payoffFunction(self, stock):
        finalPrice = stock.endPrice()
        return max(finalPrice - self.strike, 0)
