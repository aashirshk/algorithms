class Node:

    def __init__(self, data, next_=None) -> None:
        self.data = data
        self.next_ = next_

    def __repr__(self) -> str:
        return f'{Node(self.data)}'


class LinkedList:
    
    def __init__(self) -> str:
        self.head = None

    
    def __itr__(self):
        node = self.head
        while node:
            yield node.data
            node = node.next_
    
    def insertAtBeginning(self, data):
        
        node = Node(data)

        if self.head is None:
            self.head = node
        
        else:
            node.next_ = self.head
            self.head = node
    
    def insertAtNth(self, data, index):
        
        if index == 0:
            self.insertAtBeginning(data)
        else:
            new_node = Node(data)
            node = self.head
            for _ in range(index-1):
                node = node.next_
            
            new_node.next_ = node.next_
            node.next_ = new_node


l1 = LinkedList()

# l1.insertAtBeginning(1)
# l1.insertAtBeginning(2)
l1.insertAtNth(5,0)

print(list(l1.__itr__()))
