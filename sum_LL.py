#program to create Linked List and display elements and add the elements

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def create(self):
        while(True):
            data =int(input("Enter no.,0 to quit"))
            if data == 0:
                break
            if self.head == None:
                self.head = Node(data)
                left =self.head
            else:
                right = Node(data)
                left.next = right
                left = right

    def display(self):
        left =self.head
        print("The elements of th LL are: ")
        while (left!= None):
            print(left.data,end = "->")
            left =left.next
        print("None")

    def sum(self):
        left =self.head
        sum =0
        print("The sum of th LL are: ")
        while left!= None:
            sum =sum + left.data
            left =left.next
        print(sum)
obj = LinkedList()
obj.create()
obj.display()
obj.sum()











        
              
        
