class Node:

    def __init__(self, data) -> None:
        self.data = data
        self.next = None
    
    def __repr__(self) -> str:
        return f'Node({self.data})'


class Hashing:

    def __init__(self, size) -> None:
        self.size = size
        self.hashTable = [None]*size

    def insert(self, value):

        node = Node(value)

        key = value % self.size

        if self.hashTable[key] == None:
            self.hashTable[key] = node
        else:
            
            temp = self.hashTable[key]

            while temp.next:
                temp = temp.next
            
            temp.next = node

    def search(self, value):

        key = value % self.size

        temp = self.hashTable[key]

        while temp:
            if temp.data == value:
                print(f'{value} exist in hash table {key} and in node {temp}')
            
            temp = temp.next
    
    def delete(self, value):

        key = value % self.size

        temp = self.hashTable[key]

        if temp.data == value:
            self.hashTable[key] = temp.next
        else:

            while temp.next:
                if temp.next.data == value:
                    temp.next = temp.next.next

                temp = temp.next
                    
    def __iter__(self):

        for i in range(self.size):
            temp = self.hashTable[i]
            print(f"hashTable[{i}] --> {i}")

            while temp:
                print(f'{temp.data} --> {temp.next}')
                temp = temp.next

h1 = Hashing(10)


h1.insert(2)

h1.insert(22)

h1.insert(32)

h1.insert(3)

print(h1.hashTable)

h1.__iter__()

h1.search(200)

h1.delete(22)

h1.__iter__()
