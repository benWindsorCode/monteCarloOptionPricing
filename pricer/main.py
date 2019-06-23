from derivative.europeanCall import EuropeanCall
from derivative.lookbackCall import LookbackCall

def main():
    S0 = 150
    vol = 1
    drift = 1.5
    N = 40
    delta = 0.01
    strike = 153
    r=0.02
    option = EuropeanCall(S0, vol, drift, N, delta, r, strike)
    print("Price of european call is: %s" % option.price())
    
    option2 = LookbackCall(S0, vol, drift, N, delta, r)
    print("Price of lookback call is: %s" % option2.price())

if __name__ == '__main__':
    main()
