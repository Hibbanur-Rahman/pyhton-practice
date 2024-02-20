#variable time
a=34
b=34.67
c=a+b
#addition of two number
print(a+b)
print(c)
#remainder of any number
a=int(input("enter the number:"))
print("the remainder is",a%2)
#type of variable
a=input("enter the any thing:")
print(type(a))
#checking the operators condition
a=int(input("enter the first number:"))
b=int(input("enter the second number:"))
if a>b:
    print(a,"is greater than",b)
elif a==b:
    print(a,"is equal to",b)
else:
    print(a,"is less than ",b)
#average of two numbers
a=int(input("enter the first number:"))
b=int(input("enter the second number:"))
print("the average of",a,"and",b,"is",(a+b)/2)
#square of the number
a=int(input("enter the number:"))
print("the square of",a,"is",a**2)

a='A'
print(ord(a))

a=list(map(int,input().split()))
if (a[0]+a[1]+a[2])%2==0 and a[0]>0 and a[1]>0 and a[2]>0:
    print("YES")
else:
    print("NO")

a1,a2,a3=map(int,input().split())
print(a1+a2+a3)

