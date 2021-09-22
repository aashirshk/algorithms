def insertionSort(arr):

    for i in range(len(arr)):
        for j in reversed(range(i+1)):
            if arr[j] < arr[j-1] and j > 0:
                arr[j], arr[j-1] = arr[j-1], arr[j]

n = [1, 2, 3, 4, 5]

insertionSort(n)

print(n)