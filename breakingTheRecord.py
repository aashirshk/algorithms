def breakingTheRecord(scores):

    maximum = scores[0]

    minimum = scores[0]

    maxCount = 0

    minCount = 0

    for score in scores:
        if score > maximum:
            maximum = score
            maxCount += 1
        elif score < minimum:
            minimum = score
            minCount += 1
    
    print(maxCount, minCount)


if __name__ == "__main__":
    scores = [3, 4, 21, 36, 10, 28, 35, 5, 24, 42]

    breakingTheRecord(scores)

