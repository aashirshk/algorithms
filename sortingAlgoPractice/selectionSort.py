arr = [5, 4, 3, 2, 1]

for i in range(len(arr)):
    minimumNum = min(arr[i:])
    minimumNumIndex = arr.index(minimumNum)
    arr[i], arr[minimumNumIndex] = arr[minimumNumIndex], arr[i]


print(arr)