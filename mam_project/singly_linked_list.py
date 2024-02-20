# Node class
class Node:
    # Function to initialise the node object
    def __init__(self, data):
       self.data = data # Assign data
       self.next = None # Initialize next as null
 
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
    #this function display the linked list
    def display(self):
        current = self.head
        while current is not None:
            print(current.data, end = ' ')
            current = current.next
    # this function find the data in the place index 
    def find_index(self, key):
        current = self.head
 
        index = 0
        while current:
            if current.data == key:
                return index
            current = current.next
            index = index + 1
        return -1

    # this function is find the length of the linked list
    def length(self):
        p1=self.head
        count1=0
        while p1!=None:
            count1+=1
            p1=p1.next
        return count1

a_llist = LinkedList()
arr=list(map(int,input("enter the array: ").split()))
for data in arr:
    a_llist.append(data)
print('The linked list: ', end = '')
a_llist.display()
print()
 
key = int(input('What data item would you like to search for? '))
index = a_llist.find_index(key)
if index == -1:
    print(str(key) + ' was not found.')
else:
    print(str(key) + ' is at index ' + str(index) + '.')

print("the length of list is",a_llist.length())
