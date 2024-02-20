#write a program that makes use of trignometric functions available in math module
from math import degrees, radians,sin,cos,tan,sinh,cosh,tanh,acos,asin,hypot

#radian to degree
a=int(input("enter the angle in radian:"))#1radian=57.2957795 degrees
b=degrees(a)
print(a,"radian=",b)

#degree to radian
a=int(input("enter the angle in degree:"))
b=radians(a)
print(a,"degree=",b)

#sin(x) function
x=int(input("enter the angle in degree:"))
# y=sin((x)* 0.017453292519943295)#change the degree into radian
y=sin(radians(x))#change the degree into radian
print("sin(",x,")=",y)

#cos(x) function
x=int(input("enter the angle in degree:"))
y=cos(radians(x))#change the degree into radian
print("cos(",x,")=",y)

#tan(x) function
x=int(input("enter the angle in degree:"))
y=tan(radians(x))#change the degree into radian
print("tan(",x,")=",y)

#sinh(x) function #hyperbolic sine of x
x=int(input("enter the angle in degree:"))
y=sinh(radians(x))#change the degree into radian
print("sinh(",x,")=",y)

#cosh(x) function #hyperbolic cosine of x
x=int(input("enter the angle in degree:"))
y=cosh(radians(x))#change the degree into radian
print("cosh(",x,")=",y)

#tanh(x) function #hyperbolic tan of x
x=int(input("enter the angle in degree:"))
y=tanh(radians(x))#change the degree into radian
print("tanh(",x,")=",y)

#acos(x) #cos inverse of x in radians
x=float(input("enter the number(0 to 1) which the you want to reverse of cos:"))
y=degrees(acos(x))
print("acos(",x,")=",y)

#asin(x) #cos inverse of x in radians
x=float(input("enter the number(0 to 1) which the you want to reverse of cos:"))
y=degrees(asin(x))
print("acos(",x,")=",y)

#hypot(x,y) #sqrt(x*x+y*y)
x=int(input("enter the length of base:"))
y=int(input("enter the length of perpendicular:"))
z=hypot(x,y)
print("hypotense of base=",x,"and height=",y,"then hypotenes=",z)


