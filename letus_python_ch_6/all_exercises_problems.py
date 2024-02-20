for index in range(20,10,-3):
    print(index,end=' ')
lst=[10,60,70,80]

# B part g
i=1
while i<10:
    j=1
    while j<=5:
        print(i,j)
        j+=1
        break
    print(i,j)
    i+=1

#write a program to print first 25 odd numbers using range()
a=0
for i in range(0,25):
    a+=2
    print(a,end=' ')

#Rewrite the following program using for loop.

lst=['desert','dessert','to','lose','loose']
s='Mumbai'
i=0
while i<len(lst):
    if i>3:
        break
    else:
        print(i,lst[i],s[i])
        i+=1
print()
j=0
for x in range(len(lst)):
    if j>3:
        break
    else:
        print(j,lst[j],s[j])
        j+=1

print()
a=0
for x in lst:
    if a>3:
        break
    else:
        print(a,lst[a],s[a])
        a+=1

#write a program to find the factorial value of any number entered through the keyboard

num=int(input("enter the number:"))
fact=1
i=1
while i<=num:
    fact*=i
    i+=1
print(str(num)+"!="+str(fact))

#write a program to print out all Armstrong numbers between 1 and 500.if sum of cubes of each digit of the number is equal to the number itself,then the number is called  an Armstrong number.for example,153=(1*1*1)+(2*2*2)+(3*3*3)

# num=(input("enter the number:"))
# sum=0
# for x in num:
#     sum+=int(x)**3
# if sum==int(num):
#     print(num+" is armstrong number")
# else:
#     print(num+" is not a armstrong number")

for i in range(1,500):
    sum=0
    for x in str(i):
        sum+=int(x)**3
    if sum==int(i):
        print(i,"is armstrong number")


#write a program to print all prime number from 1 to 300

for x in range(1,300):
    j=2
    for i in range(2,x):
        if x%i==0:
            j=0
            break
        else:
            j=1
    if j==1:
        print(x,"is prime number")

# write a program to print the multiplication table of the number entered by the user.the table should get displayed in the following form:
#29*1=29
#29*2=58

num=int(input("enter the number:"))
for i in range(1,11):
    print(str(num)+"*"+str(i)+"=",num*i)

#when interest compounds q times per year at an annual rate of r% for n years,the principle p compounds to an amount a as per a=p(1+r/q)^nq
for z in range(0,2):
    p=int(input("enter the principle amount:"))
    q=int(input("enter the compounds times per year:"))
    r=float(input("enter the rate of intreset:"))
    n=int(input("enter the year:"))
    a=1
    for x in range(0,q):
        for y in range(0,n):
            a*=(1+r/q)
    a*=p
    print("the compound interest is ",a)

    
