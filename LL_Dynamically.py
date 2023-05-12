#Aim: To create and Display Linkrd list Dynamically
#author: Azmath Noorain
#date: 4-5-2023


#Declaration of a node
class Node:
    def __init__(self,data):

        self.data = data
        self.next = None
        
class LinkedList_1:
    def __init__(self):
        self.head = None

    def create(self):
        while(True):
            data = int(input("Enter the data, 0 to quit: "))
            if data == 0:
                break
            if (self.head == None):
                #create node
                self.head = Node(data)
                left = self.head
            else:
                right = Node(data)
                #to establish link btw left and right
                #by assigning the add of right to left.next
                left.next = right
                left = right
                
    def display(self):
         print("The elements of the Linked list")
         left = self.head
         while (left != None): 
                print(left.data,end = "->")
                left =left.next
         print("None")  
obj = LinkedList_1()
obj.create()
obj.display()





