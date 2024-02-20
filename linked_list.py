class Node:
    def __init__(self,data):
        self.data=data
        self.ref=None

class LinkedList:
    def __init__(self):
        self.head=None

    def print_ll(self):
        if self.head==None:
            print("linked list is empty!")
        else:
            ptr1=self.head
            while ptr1!=None:
                print(ptr1.data,end=' ')
                ptr1=ptr1.ref
    def add_begin(self,data):
        new_node=Node(data)
        new_node.ref=self.head
        self.head=new_node

    def add_end(self,data):
        new_node=Node(data)
        ptr=self.head
        while ptr.ref!=None:
            ptr=ptr.ref
        ptr.ref=new_node
    def del_end(self):
        ptr=self.head
        ptr1=self.head
        ptr1=ptr1.ref
        while ptr1.ref!=None:
            ptr=ptr.ref
            ptr1=ptr1.ref
        ptr=None
        return self.head
ll1=LinkedList()

first=Node(10)
second=Node(13)
third=Node(15)

first.ref=second
second.ref=third
third.ref=None
ll1.head=first
ll1.print_ll()
ll1.add_begin(20)
print("\nthe updated: ")
ll1.print_ll()

ll1.add_end(55)
print("\nthe updated linked list: ")
ll1.print_ll()

ll1.del_end()
print("\nthe updated linked list: ")
ll1.print_ll()