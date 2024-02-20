#B part a
i,j,k=4,-1,0
w=i or j or k
x= i and j and k
y= i or j and k
z= i and j or k
print(w,x,y,z)

#B part b
a=10
a=not not a
print(a)

#B part c
x=int(input("enter the value of x:"))
y=int(input("enter the value of y:"))
z=int(input("enter the value of z:"))
if x>y and x>z:
    print("biggest is:",x)
elif y>x and y>z:
    print("biggest is:",y)
else:
    print("biggest is:",z)

#B part d
num=30
k=100 if num<=10 else 500
print(k)

#B part e
a=10
b=60
if a and b>20:
    print("hello")
else:
    print("hi")

#B part f
a=10
b=60
if a>20 and b>20:
    print("hello")
else:
    print("hi")

#B part g
a=10
a = 30 or 40 or 60
if a:
    print("hello")
else:
    print("hi")

#B part h
a=10
a = 30 or a==40 or a==60
if a:
    print("hello")
else:
    print("hi")

#B part i
a=10
if a in (30,40,50):
    print("Hello")
else:
    print("hi")