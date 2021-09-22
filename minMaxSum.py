def minMaxSum(arr):
    temp_arr = []
    for i in range(len(arr)):
        arr_copy = arr.copy()
        arr_copy.pop(arr.index(arr[i]))
        temp_arr.append(sum(arr_copy))
    
    return [min(temp_arr), max(temp_arr)]



if __name__ == "__main__":
    arr = [1, 2 ,3, 4, 5]

    a,b = minMaxSum(arr)

    print(a,b)