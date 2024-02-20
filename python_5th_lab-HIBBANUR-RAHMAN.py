"""write a python program to demonstrate dictonary"""
a={}    #empty dictionary
b={'a21004':'hibban','a21005':'ramsha','a21006':'bushra'}
print(b)


"""write a python program to demonstrate the string"""
a=input("enter the name:")
for i in range(0,len(a)):
    print(a[i],end=" ")
print()
b=input("enter the any string:")
print(a+b)

"""write a python program to demonstarte the list"""
from random import randint
a=[]
for i in range(0,10):
    a.append(randint(0,100))
print("the list is:",a)


"""write a python program to demonstarte operator
    1.assignment operator
    2.comaprison operator
    3.arithematic operator
    4.logical operator
"""
#1.assignment operator
a=5
b=6
a=b#assignment operator
print(a)
#2. comparison operator
a=5
b=6
print(a>b)
print(a<b)
print(a==b)
print(a>=b)
print(a<=b)
#3.arithmetic operator
a=5
b=6
print(a+b)
print(a-b)
print(a/b)
print(a//b)
print(a%b)
print(a*b)
print(a**b)
#4.logical operator
a=True
b=False
print(a and b)
print(a or b)
a=False
b=True
print(a and b)
print(a or b)

a=5
b=9
print(a|b)
arr=[0,1,0,1,0]
print(arr)
b=arr.count(0)
c=arr.count(1)
arr[0:b]=0
arr[b:c]=1
print(arr)

a=[1,2,3,4,5]
b=[1,2,3]
if b[1] in a:
    print("yes")

a="hibban"
print(a.find("bb"))

a=["ramsha","bushra","baaji","hibban","raani"]
print(min(a,key=len))


n=20
arr=[-1 ,-17 ,-12, 8, 16, -17, -13, -14, -3, -6, -5, -11, -10, -12, -5, 19, -17, -5, -1, 12]
arr.sort()
count=1
num=[]
if n==1:
    print(arr[-1])
if n==2:
    if arr[-1]==arr[-2]:
        print(0)
for i in range(0,n-1):
    if arr[i]!=arr[i+1]:
        if count==1:
            print(arr[i])
        count=1
    elif arr[i]==arr[i+1]:
        count+=1
if arr[-1]!=arr[-2]:
    print(arr[-1])
if len(num)==0:
    print(0)

for i in range(0,1000):
    print("next monday",end="  ")


m=12
m=bin(m)
print(m[-len(m)::1])
print(m)
print('{:032b}'.format(100))