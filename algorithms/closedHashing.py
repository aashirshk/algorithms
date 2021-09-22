class closedHashing:

    def __init__(self, size) -> None:
        self.size = size
        self.arr = [-1]*self.size

    def insert(self, value):
        
        hashKey = value % self.size

        key = hashKey

        i = 1

        while self.arr[key] != -1:

            key = (hashKey + i) % self.size

            if key == hashKey:
                print("Hash table is full.")
                return 0

            i += 1

        self.arr[key] = value
    


    def delete(self, value):
        
        hashKey = value % self.size

        key = hashKey

        i = 1

        while self.arr[key] != value:

            key = (hashKey + i) % self.size

            if key == hashKey:

                print("Value doesnot exist in hashtable.")

                return 0

            i += 1

        self.arr[key] = -1



    def search(self, value):

        hashKey 


    def __repr__(self) -> str:
        print(self.arr)

    

h1 = closedHashing(10)

h1.insert(2)

h1.insert(22)

h1.delete(24)

h1.__repr__()