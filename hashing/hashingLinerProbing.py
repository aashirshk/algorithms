size = 10

arr = [-1]*size

def insert(value):

    hashKey = value % size

    key = hashKey

    index = 1

    while arr[key] != -1:

        key = (hashKey + index) % size

        if key == hashKey:
            print("Hash table is full")
            return 0
        
        index += 1
    arr[key] = value

def delete(value):

    hashKey = value % size

    key = hashKey

    index = 1

    while arr[key] != value:

        key = (hashKey + index) % size

        if key == hashKey:
            print("Element not in hashtable.")
            return 0
    
        index += 1
    
    arr[key] = -1

def search(value):

    hashKey = value % size

    key = hashKey

    index = 1

    while arr[key] != value:

        key = (hashKey + index) % size

        if key == hashKey:
            print("Element not in hashtable.")
            return 0
        index += 1

    return arr[key]

insert(5)

insert(5)

insert(10)

insert(9)

insert(19)

delete(9)

res = search(19)

print("Search res is: ", res)

print(arr)

