# write a program to store seven fruits in a list entered by the user.

b=[]
for x in range(0,7):
    a=input("enter the fruits name:")
    b.append(a)
print("the list is:")
print(b)

# write a program to accept marks of 6 students and display them in a sorted manner
marks=[]
for x in range(0,6):
    print("enter the marks of",x+1,"th student:")
    a=input()
    marks.append(a)
list.sort(marks)
marks.reverse()
print(marks)

#check that a tuple cannot be changed in python

#write a program to sum a list with 4 numbers
number=[]
sum=0
print("enter the numbers:")
for x in range(0,4):
    a=int(input())
    number.append(a)
    sum=sum+number[x]
print("the sum of",number,"is ",sum)

#write a program to count the number of zeroes in the following tuple
a=(7,0,8,0,0,9)
b=a.count(0)
print("the number in the tupple ",a,"is",b)