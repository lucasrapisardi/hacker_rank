def birthdayCakeCandles(candles):
    sorr = sorted(candles)
    high = sorr[-1]
    print(sorr.count(high))
    return


candles = [4, 4, 1, 3]
birthdayCakeCandles(candles)
