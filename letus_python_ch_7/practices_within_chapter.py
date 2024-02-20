#recieve full name 
name=input("enter full name:")
#separate first name,middle name and surname
fname,mname,sname=input("Enter the full name:").split()
print(fname,mname,sname)

r,l,b=1.5678,10.5,12.66
print(f'radius={b}')
print(f'length={l} breadth={b} radius={r}')

name='Sushant Ajay Raje'
for n in name.split():
    print(f'{n:10}')

n1,n2,n3=input("enter three values:").split()
n1,n2,n3=int(n1),int(n2),int(n3)
print(n1+10,n2+20,n3+30)

n1,n2,n3=[int(n) for n in input('enter three values:').split()]
print(n1+10,n2+20,n3+30)

numbers=[int(x) for x in input("enter the values:").split()]
for n in numbers:
    print(n+10)

data=input("enter the names,age,salary:").split()
name=data[0]
age=int(data[1])
salary=float(data[2])
print("name=",name,"age=",age,"salary=",salary)

"""using format() method of string object:"""

r,l,b=1.5678,10.5,12.66
name,age,salary='Rakshita',30,53000.556

# print in order by position of variable using empty{}
print('radius={} length={} breadth={}'.format(r,l,b))
print('name={} age={} salary={}'.format(name,age,salary))

# print in any desired order
print('radius={2} length={1} breadth={0}'.format(r,l,b))
print('name={1} age={2} salary={0}'.format(name,age,salary))

# print name in 15 columns,salary in 10 columns
print("name={0:15} salary={1:10}".format(name,salary))

# print radius in 10 columns,with 2 digits after decimal point 
print('radius={0:5.2f}'.format(salary))