#write a program to recieve radius of a circle,and length and breadth of a rectangle in one call to input().calculate and print the circumference of circle and perimeter of rectangle

from cmath import pi
radius,length,breadth=[int(x) for x in input("enter the value of radius,length,breadth:").split()]
circumference=2*pi*radius
perimeter=2*(length+breadth)
print("the circumference={} and the perimeter={}".format(circumference,perimeter))
#the second method to print
print("the second method to print:")
print(f'the circumference={circumference} and the perimeter={perimeter}') 

# write a program to receive 3 integers using one call to input().the three integers signify starting value ,ending value and step value for a range.
# the program should use these values to print the number,its square and its cube,all properly right-aligned.also output the same values left-aligned 

start,end,step_value=[int(x) for x in input("enter the starting value,ending value and step value:").split()]
temp=start
print("the starting value ={} ,the ending value={} and the step value={}".format(start,end,step_value))
while start<end:
    print("{}\t{}\t{}".format(start,start**2,start**3))
    start+=step_value

#the second method is to solve the problem is :
#right aligned printing
for n in range(temp,end,step_value): #we using the temp variable because the star value is operated in the above problems so we cannot use the start value same as it
    print(f'{n:>5}{n**2:>7}{n**3:>8}')

print()
#left aligned printing 
for n in range(temp,end,step_value):
    print("{0:<5}{1:<7}{2:<8}".format(n,n**2,n**3))

#write a program to maintain names and cell numbers of 4 persons and then print systematically in a tabular form.
name=[]
cell_number=[]
y=int(input("enter the number of person which you want to display:"))
for x in range(0,y):
    name1,cell_number1=input("enter the name and cell number:").split()
    name.append(name1)
    cell_number.append(cell_number1)
for x in range(0,y):
    print(name[x],":",cell_number[x])

# in the above printing the name and cell number is in not formated form
print()
for x in range(0,y):
    print(f'{name[x]:15}:{cell_number[x]:10}')

print()
for x in range(0,y):
    print('{0:<15}:{1:<17}'.format(name[x],cell_number[x]))

#suppose there are 5 variables in a program-max,min,mean,sd and var, having some suitable values.writea program to print these variables properly aligned using multiple fstrings,but one call to print()

max,min,sd,var=input("enter the value  of max,min,sd and var:").split()
print(f'{"max":<10}:{max}\n'+f'{"min":<10}:{min}\n'+f'{"sd":<10}:{sd}\n'+f'{"var":<10}:{var}\n')

#Write a program that prints square root and cube root of numbers from 1 to 10, up to 3 decimal places. Ensure that the output is displayed in separate lines, with number center-justified and square and cube roots, right-justified.

from math import sqrt
print(f'{"number":^5}{"square root":{10}.{6}}{"cube root":{10}.{4}}')
for x in range(1,11):
    print(f'{x:<5}{x**(1/2):{10}.{4}}  {x**(1/3):{10}.{4}}')