#write the python program which the user is enter the radius and show the the area of circle

#this function is taking the parameter which is radius
def area_of_circle(radius):
    #returning the area of circle taking pi=3.14
    return 3.143*radius*radius

#we are taking the radius of circle from the user 
radius=int(input("enter the radius of circle:"))
#print the area of circle which is returning from the function area_of_circle()
print("the area of circle is ",area_of_circle(radius))


s='a1s^'
print(s[0].isalnum())
s=s.upper()
print(s)