"""
    Pass a tuple to the divmod() function and obtain the quotient and the remainder
"""
a=divmod(16,5)  #divmod(x,y) return the tuple which is like this:- (x//y,x%y)
print("the quotient and remainder is respectively:",a)
t=(16,5)
a=divmod(*t)
print("the quotient and remainder is respectively:",a)

"""
    write a program to perform the following operations:
    --pack first 10 multiples of 10 into a tuple
    --unpack the tuple into 10 variables,each holding 1 value
    --unpack the tuple such that first value gets stored in variable x, last value in y
        and all values in between into disposable variables__
    --unpack the tuple such that first value gets stored in variable i,last value in j
        and all values in between into a single disposal variable_
"""
#DISPOSAL variable( _ )is usally used when you do not wish to use the variable further, and is being used only as a place-holder
a=[]
for i in range(1,11):
    a.append(10*i)
tpl=(*a,)     #pack first 10 multiples of 10 into a tuple
print(tpl)
a,b,c,d,e,f,g,h,i,j=tpl     #unpack the tuple into 10 variables,each holding 1 value
print(a,b,c,d,e,f,g,h,i,j)
x,_,_,_,_,_,_,_,_,y=tpl     #unpack the tuple such that first value gets stored in variable x, last value in y and all values in between into disposable variables__
print(x,y,_)
i,*_,j=tpl              #unpack the tuple such that first value gets stored in variable i,last value in j and all values in between into a single disposal variable_
print(i,j,_)

"""
    A list contains names of boys and girls as its elements. Boys' names are stored as tuples. write a python program to find out number of boys and girls in the list
"""
lst=[('hibban','farhan','ashad','mannu','akif','yasar','saif','motiur rahman','aman','athar'),'Ramsha','Bushra','Rabiya','arfaana','Sufiya','madiha','sahista','monira']
print("the number of boys in this list is:",len(lst[0]))
print("the number of girls in this list is :",len(lst)-1)

lst=['Shubha','Nisha','Sudha',('Suresh',),('Rajesh',),'Radha']
lst=[('hibban',),('farhan',),('ashad',),('mannu',),('akif',),('yasar',),('saif',),('motiur rahman',),('aman',),('athar',),'Ramsha','Bushra','Rabiya','arfaana','Sufiya','madiha','sahista','monira']
boys=0
girls=0
for ele in lst:
    if isinstance(ele,tuple):   #isinstance() functions checks whether ele is an instance of tuple type.
                                #note that since the tuples contain a single element,it is followed by a comma.

        boys+=1
    else:
        girls+=1
print('Boys=',boys,'Girls=',girls)

"""
    A list contains tuples containning roll number,names and age of student.
    write a python program to gather all the names from this list into another list.
"""
lst=[('21btcs026hy','hibban','18'),('21btcs055hy','Ramsha','20'),('21btcs056hy','Bushra','22'),('21btcs054hy','Sabiha','19')]
lst1=[]
for ele in lst:
    if isinstance(ele,tuple):
        lst1.append(ele[1])
print(lst)
print(lst1)

"""
    Given the following tuple 
    ('F','I','a','b','b','e','r','g','a','s','t','e','d')

    write a python program to carry out the following operations:
    --add sn ! at the end of the tuple
    --convert a tuple to a string
    --Extract ('b','b') from the tuple
    --find out number of occurrences of 'e' in the tuple
    --check whether 'r' exists in the tuple
    --convert the tuple to a list
    --delete charecters 'b,'b','e','r' from the tuple
"""
tpl=('F','I','a','b','b','e','r','g','a','s','t','e','d')
#addition in the tuple is not possible because tuple is immutable
#so to add ! we need to create a new tuple and then make tpl and then make tpl refer to it 
tpl1=str(tpl)
print(tpl1) 
print(type(tpl1))
tpl=tpl+('!',)
print(tpl)

#convert tuple into string
tpl2=''.join(tpl)
print(tpl2)
print(type(tpl2))

#extract('b','b') from the tuple
t=tpl[3:5]
print(t)

#count number of 'e' in the tuple
count=tpl.count('e')
print('count=',count)

#check whether 'r' exists in the tuple 
print('r' in tpl)

#Convert the tuple to a list
lst=list(tpl)
print(lst)

#tuples are immutable,so we cannot remove elements from it
#we need to split the tuple,eliminate the unwanted element and then merge the tuples
tpl=tpl[:3]+tpl[7:]
print(tpl)


import math
a=math.pi
print(a)