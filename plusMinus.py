def plusMinus(arr):
    totalCount = [1 if a > 0 else -1 if a < 0 else 0 for a in arr]

    print(totalCount)

    positiveCountRatio = totalCount.count(1)/len(totalCount)
    negativeCountRatio = totalCount.count(-1)/len(totalCount)
    zeroCountRatio = totalCount.count(0)/len(totalCount)

    print(f'{positiveCountRatio:.6f}\n{negativeCountRatio:.6f}\n{zeroCountRatio:.6f}')


if __name__ == "__main__":  
    arr = [-4, 3, -9, 0, 4, 1]

    plusMinus(arr)
