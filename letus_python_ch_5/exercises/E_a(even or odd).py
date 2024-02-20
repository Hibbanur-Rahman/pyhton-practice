#any integer is input through the keyboard.write a program to find out whether it is an odd or even number.

a=int(input("enter the number:"))
if a%2==0:
    print(a,"is even number")
else:
    print(a,"is odd number")

#any year is input through the keyboard . write a program to determine whether the year is a leap year or not.

year=int(input("enter the year:"))
if year%4==0:
    print(year,"is leap year")
else:
    print(year,"is not leap year")

#if ages of Ram,Shayam and ajay are input through the keyboard,write a program to determine the youngest of the three

Ram_age=float(input("enter the age of Ram:"))
Shayam_age=float(input("enter the age of Shayam :"))
Ajay_age=float(input("enter the age of Ajay:"))

if Ram_age<Shayam_age and Ram_age<Ajay_age:
    print("Ram is youngest")
elif Shayam_age<Ram_age and Shayam_age<Ajay_age:
    print("Shayam is youngest")
elif Ajay_age<Shayam_age and Ajay_age<Ram_age:
    print("Ajay is youngest")
else:
    print("you enterd the wrong ages")

#write a program to checkh whether a triangle is valid or not, when the three angles of the triangle are entered through the keyboard.

angle_A=float(input("enter the angle of first side:"))
angle_B=float(input("enter the angle of second side:"))
angle_C=float(input("enter the angle of third side:"))

if (angle_A==0 or angle_B==0 or angle_C==0):
    print(angle_A,",",angle_B,"and",angle_C,"are the the angles of invalid triangle")
elif (angle_A+angle_B+angle_C)==180:
    print(angle_A,",",angle_B,"and",angle_C,"are the the angles of valid triangle")
else:
    print(angle_A,",",angle_B,"and",angle_C,"are the the angles of invalid triangle")

#write a program to find the absolute value of a number entered through the keyboard

a=float(input("enter the number:"))
print("the absolute value of",a,"is",abs(a)) 

#given the length and breadth of a rectangle ,write a program to find whether the area of the rectangle is greater than its perimeter .

length=float(input("enter the length of the rectangle:"))
breadth=float(input("enter the breadth of the rectangle:"))
area=length*breadth
perimeter=2*(length+breadth)
 
if area>perimeter:
    print("the area of the rectangle with length=",length,"and breadth=",breadth,"is greater than its perimeter") 
else:
    print("the perimeter of the rectangle with length=",length,"and breadth=",breadth,"is greater than its area") 

#Given three points (x1,y1),(x2,y2) and (x3,y3),write a program to check if all the three points fall on one straight line

x1=float(input("enter the value of x1:"))
x2=float(input("enter the value of x2:"))
x3=float(input("enter the value of x3:"))
y1=float(input("enter the value of y1:"))
y2=float(input("enter the value of y2:"))
y3=float(input("enter the value of y3:"))

if x1==x2==x3 or y1==y2==y3:
    print("(",x1,",",y1,")",",","(",x2,",",y2,")","and","(",x3,",",y3,") are in same straight line")
else:
    print("(",x1,",",y1,")",",","(",x2,",",y2,")","and","(",x3,",",y3,") are not in the same straight line")

#given the coordinates (x,y) of center of a circle and its radius,write  a program that will determine whether a point lies inside the circle,on the circle or outside the circle.
import math
x=float(input("enter the x-coordinates of center:"))
y=float(input("enter the y-coordinate of center:"))
radius=float(input("enter the radius of circle:"))

x1=float(input("enter the x-coordinates of point:"))
y1=float(input("enter the y-coordinate of point:"))
y=(x1-x)*(x1-x)+(y1-y)*(y1-y)
distances=math.sqrt(y)
if distances>radius:
    print("the point (",x1,y1,") is outside of the circle")
elif distances==radius:
    print("the point (",x1,y1,") is on the circle")
else:
    print("the point (",x1,y1,") is inside of the circle")

# Given a point (x,y),write a program to find out if it lies on the x-axis,y-axis or on the origin

x=int(input("enter the x-coordinates:"))
y=int(input("enter the y-coordinates:"))

if x==0 and y>0 or y<0:
    print("(",x,",",y,") is lies on the x-axis")
elif y==0 and x>0 or x<0:
    print("(",x,",",y,") is lies on the y-axis")
elif x==0 and y==0:
    print("(",x,",",y,") is lies on the origin")
else:
    print("(",x,",",y,") is lies neither on x-axis nor the y-axis")


# A year is entered  through the keyboard, write a program to determine whether the year is leap or not.Use the logical operators 'and' and 'or'.

year=int(input("enter the year:"))
if year%4==0:
    print(year,"is leap year")
else:
    print(year,"is not leap year")

#if the three sides of a triangle are entered through the keyboard, write a program to check whether the triangle is valid or not.the triangle is valid if the sum of two sides is greater than the largest of the three sides.

side1=float(input("enter the length of first side:"))
side2=float(input("enter the length of second side:"))
side3=float(input("enter the length of third side:"))

if (side1+side2)>max(side1,side2,side3) and (side2+side3)>max(side1,side2,side3) and (side1+side3)>max(side1,side2,side3):
    print("the triangle of",side1,",",side2,",",side3,"is valid sides of triangle")
else:
    print("the triangle of",side1,",",side2,",",side3,"is invalid sides of triangle")

#if the three sides of a triangle are entered through the keyboard ,write a program to check whether the triangle is isosceles,equilateral,scalene or right angled triangle.

side1=float(input("enter the length of first side:"))
side2=float(input("enter the length of second side:"))
side3=float(input("enter the length of third side:"))

if (side1+side2)>max(side1,side2,side3) and (side2+side3)>max(side1,side2,side3) and (side1+side3)>max(side1,side2,side3):
    if side1**2+side2**2==max(side1,side2,side3)**2 or side2**2+side3**2==max(side1,side2,side3)**2 or side3**2+side1**2==max(side1,side2,side3):
        print("these",side1,",",side2,",",side3,"sides are right-angled triangles sides")
    elif side1==side2==side3:
        print("these",side1,",",side2,",",side3,"sides are equilateral triangles sides")
    elif (side1==side2 and side1!=side3) or (side2==side3 and side2!=side1) or (side1==side3 and side1!=side2):
        print("these",side1,",",side2,",",side3,"sides are isosceles triangles sides")
    else:
        print("these",side1,",",side2,",",side3,"sides are scalene triangles sides")
else:
    print("the triangle of",side1,",",side2,",",side3,"is invalid sides of triangle")

