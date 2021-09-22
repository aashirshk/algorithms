def nonDivisibleSubSet(s, k):

    frequency = [0]*k

    for i in s:
        frequency[i%k] += 1
    
    res = min(frequency[0], 1)

    for i in range(1, k//2):

        if i != k-i:
            res += max(frequency[i], frequency[k-i])

        else:
            res += min(frequency[i], 1)
    
    return res



if __name__ == "__main__":

    s = [19, 10, 12, 10, 24, 25, 22]

    k = 4

    nonDivisibleSubSet(s, k)