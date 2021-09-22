class Sort:

    def __init__(self, arr=None) -> None:
        self.arr = arr
    

    def bubbleSort(self):

        for i in range(len(self.arr)):

            for j in range(len(self.arr)-i-1):

                if self.arr[j] > self.arr[j+1]:

                    self.arr[j], self.arr[j+1] = self.arr[j+1], self.arr[j]
    

    def insertionSort(self):

        for i in range(len(self.arr)):

            for j in reversed(range(i+1)):

                if self.arr[j] < self.arr[j-1]:

                    self.arr[j], self.arr[j-1] = self.arr[j-1], self.arr[j]
    

    def selectionSort(self):

        for i in range(len(self.arr)):

            minNumber = min(self.arr[i:])

            minNumberIndex = self.arr.index(minNumber)

            self.arr[i], self.arr[minNumberIndex] = self.arr[minNumberIndex], self.arr[i]

    
    def merge(self, start, end, mid):

        temp = [0]*len(self.arr)
        
        i = start

        j = mid + 1

        k = 0

        while i <= mid and j <= end:

            if  self.arr[i] < self.arr[j]:
                temp[k] = self.arr[i]
                i += 1
                k += 1
            else:
                temp[k] = self.arr[j]
                j += 1
                k += 1
        
        while i <= mid:

            temp[k] = self.arr[i]

            i += 1

            k += 1
        
        while j <= end:

            temp[k] = self.arr[j]

            j += 1

            k += 1

        k = 0

        for i in range(start, end+1):
            self.arr[i] = temp[k]
            k += 1
    

    def mergeSort(self, start, end):
        
        if start < end:

            mid = (start + end)//2

            self.mergeSort(start, mid)

            self.mergeSort(mid + 1, end)

            self.merge(start, end, mid)


    def partition(self, start, end):
        
        pIndex = start

        pivot = self.arr[end]

        for i in range(start, len(self.arr)):
            if self.arr[i] < pivot:
                self.arr[i], self.arr[pIndex] = self.arr[pIndex], self.arr[i]
                pIndex += 1
        
        self.arr[end], self.arr[pIndex] = self.arr[pIndex], self.arr[end]

        return pIndex


    def quickSort(self, start, end):
        
        if start < end:

            pIndex = self.partition(start, end)

            print("Pindex is: ", pIndex)

            self.quickSort(start, pIndex-1)

            self.quickSort(pIndex+1, end)


arr = [10, 4, 3, 2, 8]

s1 = Sort(arr)

s1.quickSort(0, len(arr)-1)

print(arr)

