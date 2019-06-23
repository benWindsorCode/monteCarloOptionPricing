from derivative import Derivative

class LookbackCall(Derivative):
    def __init__(self, S0, vol, mean, N, delta, r):
        Derivative.__init__(self, S0, vol, mean, N, r, delta)

    def payoffFunction(self, stock):
        prices = stock.priceList()
        finalPrice = prices[-1]
        minPrice = min(prices)
        return max(finalPrice - minPrice, 0)
