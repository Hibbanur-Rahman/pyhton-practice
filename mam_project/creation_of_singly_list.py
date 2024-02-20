#creating the node using the constructor
class Node:
    # Function to initialise the node object
    def __init__(self, data):
       self.data = data # Assign data
       self.next = None # Initialize next as null
 
#creating the linked list and function the append and display
# Linked List class contains a Node object
class LinkedList:
    # Function to initialize head
    def __init__(self):
        self.head = None
        self.last_node = None
    
    # This function is in LinkedList class. It inserts
    # a new node at the beginning of Linked List.
    def append(self, data):
        if self.last_node is None:
            self.head = Node(data)
            self.last_node = self.head
        else:
            self.last_node.next = Node(data)
            self.last_node = self.last_node.next
 
    def display(self):
        current = self.head
        while current is not None:
            print(current.data, end = ' ')
            current = current.next

#we are assinging the object of class linkedlist
a_llist = LinkedList()

#we are taking the input from the user using the map and the split function which is quite easy and reduce the number of code 
#please user is input the data in one line example 1 2 3 4 which means the 1,2,3,4 is in list
print("please enter the data in 1 2 3 4 manner not the enter manner")
arr=list(map(int,input("enter the linked_list element: ").split()))

#we are appened the data in linked list
for data in arr:
    a_llist.append(data)
print('The linked list: ', end = '')
#we are display the linked list
a_llist.display() 