def compute_lcm(a, b=0):

    if (a > b):
        higher = a
    else:
        higher = b

    value = higher

    while True:
        if (higher%a == 0) and (higher%b == 0 ):
            return higher
        else:
            higher += value

def compute_gcm(a, b=0):

    if b == 0:
        return a
    else:
        return compute_gcm(b, b%a)

def betweenTwoSets(x, y):

    a = x[0]

    b = x[1]

    c = y[0]

    d = y[1]

    lcm = compute_lcm(a, b)

    for i in range(2, len(x)):
        lcm = compute_lcm(lcm, x[i])

    gcd = compute_gcm(c, d)

    for i in range(2, len(y)):
        gcd = compute_gcm(gcd, y[i])

    count = 0
    for i in range(int(lcm), int(gcd+1), int(lcm)):
        if int(gcd) % i == 0:
            count += 1
            
    

if __name__ == "__main__":

    a = [12, 15, 10, 75]

    b = [24, 36, 40]

    betweenTwoSets(a, b)
