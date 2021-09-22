def subArrayDivision(s, d, m):
    count = 0
    for i in range(0, len(s)-m+1):
       if sum(s[i:i+m]) == d:
           count += 1

    print(count)


if __name__ == "__main__":

    s = [2, 2, 1, 3, 2]

    d = 4

    m = 2

    subArrayDivision(s, d, m)