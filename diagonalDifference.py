def diagonalDifference(arr):
    
    leftDiagonal = sum([arr[i][i] for i in range(len(arr))])

    rightDiagonal = sum([arr[i][len(arr)-i-1] for i in range(len(arr))])

    difference = abs(leftDiagonal - rightDiagonal)

    return difference


if __name__ == "__main__":

    rows = int(input("Enter the number of rows: ").rstrip().strip())

    arr = []

    for _ in range(rows):
        row_number = list(map(int, input("Enter the numbers: ").split()))
        arr.append(row_number)
    
    result = diagonalDifference(arr)

    print(result)
        

