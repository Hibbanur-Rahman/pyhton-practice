"""
    perform the following operations on a list of names.
    --create a list of 5 names:-'Anil','Amol','Aditya','Avi','Alka'
    --insert a name 'Anuj' before 'Aditya'
    --Append a name 'Zulu'
    --Delete 'Avi' from the list
    --Replace 'Anil' with 'AnilKumar'
    --Sort all the names in the list
    --Print reversed sorted list
"""
lst=['Anil','Amol','Aditya','Avi','Alka']
print(lst)
for i in range(len(lst)):
    if lst[i]=='Aditya':
        lst.insert(i,'Anuj')    #insert 'Anuj' at ith position 
        break
print(lst)
lst.append('Zulu')
print(lst)
lst.remove('Avi')
print(lst)
ind=lst.index('Anil')
lst.insert(ind,'Anilkumar')
lst.remove('Anil')
print(lst)
lst.sort()
print(lst)
lst.reverse()
print(lst)

"""
    perform the following operations on alist of numbers.
    --create a list of 5 odd numbers
    --create a list of 5 even numbers
    --combine the two lists
    --add prime numbers 11,17,29 at the beginning of the combined list
    --report how amny elements are present in the list 
    --replace last 3 numbers in the list with 100,200,300
    --Delete all the numbers in the list
    --Delete the list
"""
lst_odd=[]
lst_even=[]
for i in range(0,10):
    if(i%2!=0):
        lst_odd.append(i)
    else:
        lst_even.append(i)
    if len(lst_odd)==5 and len(lst_even)==5:
        break
print("list of even numbers:",lst_even)
print("list of odd numbers:",lst_odd)
new_list=lst_odd+lst_even
print("the combined list befoe the sort:",new_list)
new_list.sort()
print("the combined list befoe the sort:",new_list)
new_list.insert(0,29)
new_list.insert(0,17)
new_list.insert(0,11)
print(new_list)
length=len(new_list)
print("the length of the combined list and the updated list is ",length)
new_list.remove(new_list[-3])
new_list.remove(new_list[-2])
new_list.remove(new_list[-1])
new_list.append(100)
new_list.append(200)
new_list.append(300)
print(new_list)
new_list=[]
print(new_list)

"""
    write a program to implement a stack data structure.stack is a last in first out (LIFO) list in which addition and deletion takes place at the same end
"""
stack=[]
ch=-1
while ch!=4:
    print("1.push\n2.pop\n3.display\n4.exit")
    ch=int(input("choose the option:"))
    if(ch==1):
        data=int(input("enter the data:"))
        stack.append(data)
    elif(ch==2):
        print("the poped element is:",stack[-1])
        stack.remove(stack[-1])
    elif(ch==3):
        print("the stack element is:",stack)
    elif(ch==4):
        print("!!we exit the program!!")
        break
    else:
        print("!!enter the corect option!!")
    
"""
    write a program to implement a Queue data structure. Queue is a first in First Out(FIFO) list ,in which addition takes place at the rear end of the queue and deletion takes place at the front end of the queue. 
"""
queue=[]
ch=-1
while ch!=4:
    print("1.ENQUEUE\n2.DEQUEUE\n3.DISPLAY QUEUE\n4.EXIT")
    ch=int(input("choose the option:"))
    if ch==1:
        data=int(input("which element do you want to ENQUEUE:"))
        queue.append(data)
    elif ch==2:
        print("the dequeued element is:",queue[0])
        queue.remove(queue[0])
    elif ch==3:
        print("the queue elements is:",queue)
    elif ch==4:
        print("!!we exit the program!!")
        break
    else:
        print("!!you entered the wrong option please choose the correct option!!")

"""
    write a program to generate and store in a list 20 random numbers in the range 10 to 100.from this list delete all those entries which have value between 20 and 50.print the remaining list.
"""    
from random import randint
num=[]
num1=[] #for the duplicate the list when we delete the element which is greater than 20 and less than 50
for i in range(0,20):
    num.append(randint(10,100))
    a=num[i]
    num1.append(a)
print(num)
#first method h ye dusra isse bhi aasan h
for j in range(0,20):
    #num1 nahi banate toh hame out of range of index error milta kyuke ham jab delete the karte h toh element jo h woh ghat jaata
    if(20<=num1[j] and num1[j]<=50):
        num.remove(num1[j])
print(num)

#second method is
for a in num1:#num1 is liye liya kyuke num toh first method se hi sahi hogaya tha is liye num1 list mei kuch bhi nahi hua tha remove
    if a>=20 and a<=50:
        num1.remove(a)
print(num1)

"""
    write a program to add two 3 x 4
"""
print("enter the first array")
arr=[]
matrix1=[]
for i in range(0,3):
    arr=[]
    for j in range(0,3):
        arr.append(int(input()))
    matrix1.append(arr)
for i in range(0,3):
    for j in range(0,3):
        print(matrix1[i][j],end="  ")
    print()
print("enter the second matrix")
arr=[]
matrix2=[]
for i in range(0,3):
    arr=[]
    for j in range(0,3):
        arr.append(int(input()))
    matrix2.append(arr)
for i in range(0,3):
    for j in range(0,3):
        print(matrix2[i][j],end="  ")
    print()
print("the addition of two matrix is:")
for i in range(0,3):
    for j in range(0,3):
        print(matrix1[i][j]+matrix2[i][j],end="  ")
    print()

"""
    write a program to obtain a median value of a list of numbers,without disturbing the order of the numbers in the list 
"""
from random import randint
n=int(input("how many numbers which you want to see in list:"))
num=[]
for i in range(0,n):
    num.append(randint(0,100))
print(num)
num1=sorted(num)
print("first to sort the element and then find the median")
if n%2==0:
    print("the median is:",(num1[(n//2)-1]+num1[(n//2)])/2)
elif n%2!=0:
    print("the median is:",(num[n//2]))

"""a list contains only positive and negative integers. write a program to obtain the numbers of negative numbers present in the list"""
from random import randint
a=[]
for  i in range(0,20):
    a.append(randint(-100,100))
print("the list is:",a) 
for b in a:
    if b>=0:
        a.remove(b)
print("the negative numbers is:",a)
 
"""suppose  a list contains several words. write a program to create another list that contains first character of each word present in the first list"""
a=[]
for i in range(0,5):
    b=input("enter the name:")
    a.append(b)
print(a)
b=[]
for c in a:
    b.append(c[0])
print(b)

"""a list contains 10 numbers .write a program to eliminate all duplicates from the list"""
# from random import randint
num=[10,20,30,40,50,10,20,30,30,40]
for a in num:
    if num.count(a)>1:
        for i in range(1,num.count(a)):
            num.remove(a)
print(num)

"""write a program to find the mean,median and mode of a list of 10 numbers"""
from random import randint
num=[]
for i in range(0,10):
    num.append(randint(0,100))
print("the numbers list is:",num)
sum=0
for i in range(0,len(num)):
    sum=sum+num[i]
num.sort()
print("the mean is:",sum/len(num))
print(num)
if len(num)%2==0:
    print("the median is:",(num[(len(num)//2)-1]+num[(len(num)//2)])/2)
elif len(num)%2!=0:
    print("the median is:",(num[len(num)//2]))
# b_count=[]
max=1
for a in num:
    # b_count.append(num.count(a))
    if max<=num.count(a):
        max=num.count(a)
        b_count=a
if max==1:
    print("the mode is 0")
else:
    print("the mode is:",(b_count))


a=[-3,3,-2,2]
b=[]
for a1 in a:
    if a1<0:
        b.append(a1)
        a.remove(a1)
a=b+a
print(a)

N=9
n=N**0.5
n1=int(n)
if n>n1:
    print(n1)
else:
    print(n1-1)

n=3
n1=3.4

print(n1==n)