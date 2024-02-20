# C 
#c ka b 
num1=num2=(10,20,30,40,50)
print(id(num1),type(num2))
print(isinstance(num1,tuple))
print(num1 is num2)
print(num1 is not num2)
print(20 in num1)
print(30 not in num2)

#c ka c
"""
    suppose a date is represented as a tuple (d,m,y). Write a program to create two date tuples and find the number of days between the two dates 
"""
date1=(10,12,2022)
date2=(12,12,2022)
if (date1[0])>(date2[0]):
    differences=date1[0]-date2[0]
else:
    differences=date2[0]-date1[0]
print(differences)

#c ka d
"""
    create a list of tuples. Each tuple should contain an item and its price in float.
    Write a program to sort the tuples in descending order by price.Hint: Use operator.itemgetter().
"""
import operator
price=[]
n=int(input("enter the number of tuples:"))
for i in range(0,n):
    item=input("enter the item name:")
    price_of_item=float(input("enter the price of the item:"))
    price1=(item,price_of_item)
    price.append(price1)
price.sort()    #sort the list only the first element of tuple 
print(price)
print(sorted(price))
print(sorted(price,key= operator.itemgetter(1)))    #sort the element of list using the inserted the position in the operator.itemgetter() function