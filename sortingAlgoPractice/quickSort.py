def partition(arr, start, end):
    
    pivotIndex = start

    pivot = arr[end]

    for i in range(start, len(arr)):
        print(arr[i], pivot)
        if arr[i] < pivot:
            arr[i], arr[pivotIndex] = arr[pivotIndex], arr[i]
            pivotIndex += 1
    
    arr[end], arr[pivotIndex] = arr[pivotIndex], arr[end]
    print(arr)
    return pivotIndex

def quickSort(arr, start, end):
    
    if start < end:
        pivotIndex = partition(arr, start, end)

        quickSort(arr, start, pivotIndex-1)

        quickSort(arr, pivotIndex+1, end)


arr = [5, 4, 3, 2, 1]

quickSort(arr, 0, len(arr)-1)

print(arr)
