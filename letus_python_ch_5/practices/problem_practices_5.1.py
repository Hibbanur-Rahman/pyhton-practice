#while purchasing certain items,a discount of 10% is offered if the quantity purchased is more than 1000.if quantity and price per item are input through the keyboard,write a program to calculate the total expenses
quantity=int(input("enter the quantity:"))
price=float(input("enter the price of items:"))
total=quantity*price
if(total>1000):
    total=total-(total*10/100)
    print("the total expense is:",total)
else:
    print("the total expense is:",total)