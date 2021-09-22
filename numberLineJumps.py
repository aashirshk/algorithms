x1 = 2

v1 = 1

x2 = 1

v2 = 2

if v1 > v2 or x1 > x2:
    remainder = (x1-x2)%(v2-v1)

    if remainder == 0:
        print("Yes")
    else:
        print("No")

else:
    print("No")
        