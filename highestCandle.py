def highestCandle(candles):
    maximumNumber = 0
    maximumNumberCount = 0

    for candle in candles:
        if candle > maximumNumber:
            maximumNumber = candle
    
    for candle in candles:
        if candle == maximumNumber:
            maximumNumberCount += 1

    print(maximumNumberCount)

if __name__ == "__main__":
    candles = [3, 2, 1, 3]

    highestCandle(candles)