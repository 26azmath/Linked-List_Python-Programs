#program to find biggest element and its position from the given Linked List

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

    def Biggest_Position(self):
        left =self.head
        x =0
        y =0
        while left !=None:
            if x<left.data:
                x = left.data
            y =y +1
            left =left.next
        print(x)
        print(y)
        
        
            

obj = LinkedList()
obj.create()
obj.display()
obj.Biggest_Position()

















        
