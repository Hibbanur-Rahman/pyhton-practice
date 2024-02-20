# Node class
class Node:
    #creating the nodes
    # Function to initialise the node object
    def __init__(self, data):
       self.data = data # Assign data
       self.next = None # Initialize next as null

# Linked List class contains a Node object 
class LinkedList:
    # Function to initialize head
    #creating the linkedlist
    def __init__(self):
        self.head = None
        self.last_node = None
 
    # This function is in LinkedList class. It inserts
    # a new node at the beginning of Linked List.
    def append(self, data):
        #append the data in nodes
        if self.last_node is None:
            self.head = Node(data)
            self.last_node = self.head
        else:
            self.last_node.next = Node(data)
            self.last_node = self.last_node.next

    #now we are display the linkedlist
    def display(self):
        current = self.head
        while current is not None:
            print(current.data, end = ' ')
            current = current.next
    #now we are count the number of data in linked list
    def count_number(self,key):
        count=0
        p1=self.head
        while p1!=None:
            if key==p1.data:
                count+=1
            p1=p1.next
        return count

#creating the linkedlist means the assign the object of class linkedlist 
a_llist = LinkedList()

#we are taking the input from the user using the map and the split function which is quite easy and reduce the number of code 
#please user is input the data in one line example 1 2 3 4 which means the 1,2,3,4 is in list
print("please enter the data in 1 2 3 4 manner not the enter manner")
arr=list(map(int,input("enter the element of linked_list: ").split()))
#we are appened the data in linked list
for data in arr:
    a_llist.append(data)
print('The linked list: ', end = '')
#display the linked list
a_llist.display()
print()

#the key is the data which user is want to count the data that how many the data is repeating
key = int(input('What data item would you like to count for? '))
print("the count of",key,"is",a_llist.count_number(key))