def partition(arr, start, end):
    
    pIndex = start

    pivot = arr[end]

    for i in range(start, len(arr)):
        if arr[i] < pivot:
            arr[i], arr[pIndex] = arr[pIndex], arr[i]
            pIndex += 1
    
    arr[end], arr[pIndex] = arr[pIndex], arr[end]

    return pIndex

def quickSort(arr, start, end):
    
    if start < end:

        pIndex = partition(arr, start, end)

        print(pIndex)

        quickSort(arr, start, pIndex-1)

        quickSort(arr, pIndex+1, end)


if __name__ == "__main__":

    arr = [1, 2, 3, 4, 5]

    quickSort(arr, 0, len(arr)-1)

    print(arr)