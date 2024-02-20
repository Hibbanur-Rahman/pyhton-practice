#given three sides a,b,c of a triangle,write a program to obtain and print the values of three angles rounded to the next integer.use the formula a^2=b^2+c^2-2bccosA 
from math import acos, degrees

a=int(input("enter the first side:"))
b=int(input("enter the second side:"))
c=int(input("enter the third side:"))

x=(b**2+c**2-a**2)/(2*b*c) #a^2=b^2+c^2-2bccosA #x=cosA
y=(a**2+c**2-b**2)/(2*a*c) #b^2=c^2+a^2-2cacosB #y=cosB
z=(a**2+b**2-c**2)/(2*a*b) #c^2=a^2+b^2-2bacosC #z=cosC

print("angle A=",degrees(acos(x)))
print("angle B=",degrees(acos(y)))
print("angle C=",degrees(acos(z)))