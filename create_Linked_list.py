#Aim: To create and Display Linkrd list
#author: Azmath Noorain
#date: 4-5-2023

class Node:
    def __init__(self,data):

        self.data = data
        self.next = None
        
class LinkedList_1:
    def __init__(self):
        self.head = None

    def create(self):
        #create 1st node
        first = Node(1)
        #create 2nd node
        second = Node(2)
        #create 3rd node
        third = Node(3)
        #create 4th node
        fourth = Node(4)
        #create 5th node
        fifth = Node(5)
#establishing Links btw nodes
        self.head = first
        first.next = second
        second.next = third
        third.next = fourth
        fourth.next = fifth
    def display(self):   
        print("The elements of the Linked list")
        left = self.head
        while (left != None): 
                print(left.data,end = "->")
                left =left.next
        
        
        print("None")
#instantiate an object
obj = LinkedList_1()
obj.create()
obj.display()

        
        
        
obj = Node(10)
