#though a list can store dissimilar data,it is commonly used for storing similar data.
#though a tuple can store similar data it is commonly used for storing dissimilar data.the tuple data is enclosed within ()
a=()     #empty tuple 
b=(10,)     #tuple with one item.,after 10 is necessary
c=('Sanjay',25,34555.50)    #tuple with dissimillar data
d=(10,20,30,40)             #tuple with similar data
print(a)
print(b)
print(c)
print(d)
c='hibban',10,10.54     #c is act as tuple
print(c)
print(type(c))
print(c.count(25))
print(c.index(10))
#items in a tuple can be repeated, i.e. tuple may contain duplicate items. However,unlike list,tuple elements cannot be repeated using a*.
tpl1=(10,)*5
tpl2=(10)*5
print(tpl1)
print(tpl2)

#Accessing Tuple Elements
#Entire tuple can be printed by just using the name of the tuple
tpl=('Sanjay',25,34555.50)
print(tpl)
"""
    Tuple is an ordered collection. So order of insertion of elements in a
    tuple is same as the order of access. So like a string and list, tuple
    items too can be accessed using indices, starting with 0.
"""
msg=('Handle','Exceptions','Like','a','boss')
print(msg[1],msg[3])
for i in range(0,len(msg)):
    print(msg[i],end=" ")
print()
for a in msg:
    print(a,end=" ")
i=0
print()
while i <len(msg):
    print(msg[i],end=" ")
    i+=1

#using the built-in enumerate() function
tpl=(10,20,30,40,50)
for index,n in enumerate(tpl):
    print(index,n)

#unlike a list,a tuple is immutable,i.e. it cannot be modified
msg=('Fall','in','line')
msg[0]='FALL'       #error
msg[1:3]=('Above','Mark')   #error
#though a tuple itself is immutable,it can contain mutable objects like lists.
#mutable lists,immutable string --all can belong to tuple
s=([1,2,3,4],[4,5],'Ocelot')
print(s)

#if a tuple contains a list,the list can be modified since list is a mutable object.
s=([1,2,3,4],[10,20],'Oynx')
s[1][1]=45  #changes first item  of first list, i.e. 20
print(s)    #print([1, 2, 3, 4], [10, 45], 'Oynx')

#one more way to change first item of first list
p=s[1]
p[1]=100
print(s)    #print ([1, 2, 3, 4], [10, 100], 'Oynx')

#it is possible to create a tuple of tuples
a=(1,3,5,7,9)
b=(2,4,6,8,10)
c=(a,b)
print(c[0][0],c[1][2]) #0th element of 0th tuple,2nd element of 1st tuple

records=(
    ('Priyanka',24,3455.50),('Shailesh',25,4555.50),
    ('Subhash',25,4505.50),('Sugandh',27,4455.55)
)
print(records[0][0],records[0][1],records[0][2])
print(records[1][0],records[1][1],records[1][2])
for n,a,s in records:
    print(n,a,s)

#a tuple may be embedded in another tuple
x=(1,2,3,4)
y=(10,20,x,30)
print(y)

# it is possible to unpack a tuple using the * operator
x=(1,2,3,4)
y=(10,20,*x,30)
print(y)

from random import randint
arr=[]
n=int(input("enter the number of element:"))
for i in range(0,n):
    arr.append(randint(0,100))
print(arr)
print(sum(arr))

n=int(input("enter the number of element:"))
arr=[]
for i in range(0,n):
    fruits=input("enter the name of fruits:")
    arr.append(fruits)
print(arr)

arr=[1,2,3,1,5]
print(arr.index(1))
print(arr.index(1))

arr=[1,0,0,1,2,2]
count_0=arr.count(0)
count_1=arr.count(1)
count_2=arr.count(2)
arr1=[]
for i in range(0,count_0):
    arr1.append(0)
for i in range(0,count_1):
    arr1.append(1)
for i in range(0,count_2):
    arr1.append(2)
print(arr1)

tup=("RAMSHA","BUSHRA","BAAJI","RAANI","5","8",2,2,1)
print(type(tup))
print (tup [0:3])
print (tup [2:5])
print (tup [::])
print (tup [::2])
print (tup [-4:-2])
print (tup [::-1])
print (tup [::-2])
print (tup [:5:1])
print (tup [0:4:2])

lst=[10,40,30,20,50]
lst .reverse()
print(lst)
lst.sort()
print(lst)
lst.sort(reverse=True)
print(lst)
lst=[10,2,0,50,4]
print(sorted(lst))
print(sorted(lst,reverse=True))
print(list(reversed(lst)))
lst=[10,20,30,3,4,2]
print(lst[::-2])
lst=[12,15,28,39,48,35,23]
lst.append(50)
print(lst)
print(lst.pop())
lst=[12,15,13,28,24,26,20,29]
lst.append(45)
print(lst)
lst.reverse()
print(lst)
lst.sort()
print(lst)
lst. sort(reverse=True)
print(lst)
lst.remove(24)
print(lst)
lst=[5,10,2,3,12,19,26,39]
print(lst.pop())
lst.insert(2,32)
print(lst)
print(lst.count(2))
idx=lst.index(2)
print(idx)


dict={}
n=int(input("Enter the number of student:"))
i=0
while i<n:
    name=input("Enter student name:")
    marks=input("Enter student marks:")
    dict[name]=marks
    i=i+1
print("Name of student","\t", "Marks")
for x in dict:
    print("\t", x,"\t", dict[x])

name=input("name:")
date=input("date:")
formatted_letter="\n\tName: "+name+"\n\tDate:28/10/2022\n"
print(formatted_letter)

s=input("Enter a string:")
print("The string is:",s)
print("Detect double space at index:",s.find('  '))

list=["RAMSHA","HIBBAN","BUSHRA","RAANI","BAAJI",9,10]
print(list)
list.insert(3,"RAANI")
print(list)
list.remove("BAAJI")
print(list)
list.append("Farhan")
print(list)
s=["HIBBAN",6,"RAMSHA",9,"BUSHRA"]
print(len(s))
print(s.pop())
print(s.clear())


d={"RAMSHA PARVEEN":"RAANI","BUSHRA PARVEEN":"BAAJI","Farhan":"BHAIJAN"}
print(d)
print(d.items())
print(d.get("RAMSHA PARVEEN"))
print(len(d))

tuple=('H','I','B','B','A','N')
print(tuple)
tuple=tuple+('R','A','H','M','A','N')
print(tuple)
print(len(tuple))
print('M'in tuple)

class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def display(self):
        print("Name:",self.name)
        print("Marks:",self.marks)
    def grade(self):
        if self.marks>=60:
            print("Pass")
        else:
            print("Fail")

n=int(input("Enter the number of students:"))
for i in range(n):
    name=input("Enter the name of the student:")
    marks=int(input("Enter the marks of the student:"))
    s=Student(name,marks)
    s.display()
s.grade()
