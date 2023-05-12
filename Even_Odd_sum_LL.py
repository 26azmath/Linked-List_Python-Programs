#program to find sum of odd nos. and even nos. separately

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def create(self):
        while(True):
            data = int(input("Enter no. ,0 to quit"))
            if data == 0:
                break
            if self.head ==None:
                self.head = Node(data)
                left =self.head

            else:
                right =Node(data)
                left.next = right
                left =right

    def display(self):
        left = self.head
        print("Elements of the List: ")
        while left != None:
            print(left.data,end ="->")
            left = left.next
        print("None")

    def Even_Odd_sum(self):
        left = self.head
        E_sum =O_sum = 0
        while left !=None:
            if left.data %2 ==0:
                E_sum = E_sum + left.data
            else:
                O_sum = O_sum + left.data
            left =left.next
        print("The sum of even nos. = ",E_sum)
        print("The sum of odd nos. = ",O_sum)


obj = LinkedList()
obj.create()
obj.display()
obj.Even_Odd_sum()
        
 












        
