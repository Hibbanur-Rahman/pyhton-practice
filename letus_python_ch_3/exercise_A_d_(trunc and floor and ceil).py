#use trunc(),floor() and ceil() for numbers -2.8,-0.5,0.2,1.5 and 2.9 to understand the difference between these functions clearly
from math import trunc,floor,ceil

a=float(input("enter the float value:"))
print("truncate of",a,"is :",trunc(a)) #truncate to integer
print("floor of",a,"is:",floor(a)) #largest integer<=x
print("ceil of",a,"is:",ceil(a))  #smallest >=x

a=-2.8
print("\nfor value",a,":-")
print("truncate of",a,"is :",trunc(a)) #truncate to integer
print("floor of",a,"is:",floor(a)) #largest integer<=x
print("ceil of",a,"is:",ceil(a))  #smallest >=x

a=-0.5
print("\nfor value",a,":-")
print("truncate of",a,"is :",trunc(a)) #truncate to integer
print("floor of",a,"is:",floor(a)) #largest integer<=x
print("ceil of",a,"is:",ceil(a))  #smallest >=x

a=0.2
print("\nfor value",a,":-")
print("truncate of",a,"is :",trunc(a)) #truncate to integer
print("floor of",a,"is:",floor(a)) #largest integer<=x
print("ceil of",a,"is:",ceil(a))  #smallest >=x

a=1.5
print("\nfor value",a,":-")
print("truncate of",a,"is :",trunc(a)) #truncate to integer
print("floor of",a,"is:",floor(a)) #largest integer<=x
print("ceil of",a,"is:",ceil(a))  #smallest >=x

a=2.9
print("\nfor value",a,":-")
print("truncate of",a,"is :",trunc(a)) #truncate to integer
print("floor of",a,"is:",floor(a)) #largest integer<=x
print("ceil of",a,"is:",ceil(a))  #smallest >=x