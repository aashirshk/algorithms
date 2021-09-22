def countApplesAndOranges(s, t, a, b, apples, oranges):
    appleCount = sum([1 for apple in apples if(a+apple) >= s and (a+apple) <= t])

    orangeCount = sum([1 for orange in oranges if(b+orange) >= s and (b+orange) <= t])

    print(f'{appleCount}\n{orangeCount}')

if __name__ == "__main__":

    s, t = 7, 10

    a, b = 4, 12

    m, n = 3, 3

    apples = [2, 3, -4]

    oranges = [3, -2, -4]

    countApplesAndOranges(s, t, a, b, apples, oranges)
