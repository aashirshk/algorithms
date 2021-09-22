arr = [5, 4, 3, 8, 2, 1]

for i in range(len(arr)):
    # for j in reversed(range(i+1)):
    #     if j > 0 and arr[j-1] > arr[j]:
    #         arr[j], arr[j-1] = arr[j-1], arr[j]
    j = i

    while j > 0 and arr[j-1] > arr[j]:
        arr[j], arr[j-1] = arr[j-1], arr[j]
        j -= 1
    

print(arr)

