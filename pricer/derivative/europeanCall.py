from derivative import Derivative

class EuropeanCall(Derivative):
    def __init__(self, S0, vol, mean, N, delta, strike):
        Derivative.__init__(self, S0, vol, mean, N, delta)
        self.strike = strike

    def payoffFunction(self, stock):
        finalPrice = stock.endPrice()
        print(finalPrice)
        return max(finalPrice - self.strike, 0)
