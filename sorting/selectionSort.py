def selectionSort(arr):
    
    for i in range(len(arr)):
        minElement = min(arr[i:])
        minElementIndex = arr.index(minElement)
        arr[i], arr[minElementIndex] = arr[minElementIndex], arr[i]


n = [5, 4, 3, 2, 1]

selectionSort(n)

print(n)