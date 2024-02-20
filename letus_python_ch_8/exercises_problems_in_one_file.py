#part C
"""
    write a program to create a list of 5 odd integers.Replace the third element with a list of 4 even integers.Flatten,sort and print the list
"""
odd_list=[]
for i in range(1,11):
    if i%2!=0:
        odd_list.append(i)
print(odd_list)
even_list=[]
for i in range(1,11):
    if(i%2==0):
        if len(even_list)!=4:
            even_list.append(i)
        else:
            break
print(even_list)
odd_list.insert(3,even_list)
print("the new list is:",odd_list)

"""
    Suppose a list contains 20 integers generated randomly.Receive a number from the keyboard and report position of all occurrences of this number in the list.
"""
from random import randint
num=[]
for i in range(0,20):
    num.append(randint(0,100))
print(num)
target=int(input("enter the number:"))
i=0
print("the index of the",target,"is:")
for a in num:
    if a==target:
        print(i)
        print("using the index method:",num.index(a)) #this is the only one item index which is first in the list
    i+=1
"""
    Suppose a list has 20 numbers. write a program that removes all duplicates from this list.
"""
num=[10,20,30,40,10,20,30,10,40,50,60,70,30,40,10,30,40,40,50,70,70,70,60,60]
print(num)
print(len(num))
for a in num:
    if num.count(a)>=1:
        for i in range(1,num.count(a)):
            num.remove(a)
print(num)

"""
    Suppose a list contains positive and negative numbers.write a program to create two lists-one containing positive numbers and another
    containing negative numbers
"""
from random import randint
pos_neg=[]
for i in range(0,10):
    pos_neg.append(randint(-10,30))
print(pos_neg)
pos=[]
neg=[]
for a in pos_neg:
    if a<0:
        neg.append(a)
    else:
        pos.append(a)
print("the positive list is:",pos)
print("the negative list is:",neg)

"""
    suppose a list contains 5 strings.write a program to convert all these strings to uppercase
"""
lst=['hibban',"ramsha","bushra","mannu","farhan","ashad"]
for i in range(0,len(lst)):
    lst[i]=lst[i].upper()
print(lst)

"""
    write a program that converts list of temperatures in Farenheit degrees to equivalent Celsius degrees
"""
a=float(input("enter the temperatures in degree:"))
