#program to create Linkd List with ID Name total

class Node:
    def __init__(self,id,name,total):
        self.id = id
        self.name =name
        self.total = total
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def create(self):
        while(True):
            id = int(input("Enter id, 0 to quit"))
            if id == 0:
                break
            name = input("Enter Name")
            total = int(input("Enter total"))
            if self.head == None:
                self.head = Node(id,name,total)
                left = self.head
            else:
                right = Node(id,name,total)
                #establish link b/w &right Node
                left.next = right
                left = right

    def display(self):
            left = self.head
            print("The elements of the Linked List: ")
            while(left != None):
                print(left.id," ",left.name," ",left.total,end ='->')
                left = left.next
            print(None)

obj = LinkedList()
obj.create()
obj.display()



    
        
