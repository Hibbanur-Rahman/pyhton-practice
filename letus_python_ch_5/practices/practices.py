a=40
b=30
#and operator evaluates all expressions.it returns last expression if all expressions evaluate to True.otherwise it returns first value that evaluates to False
x=65 and a>=20 and b<60 and 75 #assigns 35 to x
print(x)
y=-30 and a>=20 and b<15 and 35 #assign false to y
print(y)
z=-30 and a>=20 and 0 and 35 #assign 0 to z
print(z)

print(a<b<x) #checks whether b fallls between a and x
print(b<a<x) #checks whether a fallls between b and x

print(10!=20!=10) #evaluates to True,even though 10!=10 is False