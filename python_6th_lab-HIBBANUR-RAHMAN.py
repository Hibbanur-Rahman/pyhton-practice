"""
    write a  python program using replace keyword in string where in replace date and time in a leave application
"""
from_name=input("enter the your name:")
to_name=input("enter the Recipient’s name:")
date=input("enter the date:")
from_date=("enter the starting date:")
to_date=("enter the ending date:")
application="""
Subject: Application for Casual Leave
DATE:<|date|>
Dear Mr./Mrs. {Recipient’s Name},

I am writing to you to let you know that I have an important personal matter to attend at my hometown due to which I will not be able to come to the office from {start date} to {end date}.

I have discussed and delegated my tasks to {person's name} & have instructed them to call me for any help during my absence.

I will be obliged if you consider my application for approval.

Yours Sincerely,
{Your Name}

"""

application=application.replace('{Recipient’s Name}',from_name)
application=application.replace("{Your Name}",to_name)
application=application.replace("<|date|>",date)
application=application.replace("{start date}",from_date)
application=application.replace("{end date}",to_date)
print(application)

a=input("enter the string:")
b=a.find(' ')
print(b)

"""
    write a python program to describe modifying operation in a list 
"""
from random import randint 
num=[]
n=int(input("enter the number of element:"))
for i in range(0,n):
    num.append(randint(0,100))
print(num)
num[0]=100
num[-1]=200
print(num)
num.sort()
print(num)
num.reverse()
print(num)

"""
    write a python program to describe the list slicing 
"""
print(num[0:3])


#define and describe the dictionary in python program 
mydict={
    'a210044':"Hibban",
    'a210055':"Ramsha",
    'a210056':"Bushra",
    'a210051':"Raani",
    "marks":[1,90,67,98]
}

print(mydict['a210044'])
print(mydict['a210055'])
print(mydict['a210056'])
print(mydict['a210051'])
print(mydict['marks'])
mydict['marks']=[1,2,3,5]
print(mydict['marks'])



s=input("enter the string: ")
num=[]
string=[]
new=''
for i in range(0,len(s)):
    if ord(s[i])>47 and ord(s[i])<58:
        num.append(s[i])
    else:
        string.append(s[i])
 
for i in range(0,len(string)):
    for j in range(0,int(num[i])):
        new=new+string[i]
print(new)

S='45+'
arr=[]
sum1=0
for i in range(0,len(S)):
    if S[i].isdigit():
        arr.append(int(S[i]))
    else:
        if S[i]=='+':
            sum1=arr[-1]+arr[-2]
            arr.pop(-1)
            arr.pop(-1)
            arr.append(sum1)
        elif S[i]=='-':
            sum1=arr[-2]-arr[-1]
            arr.pop(-1)
            arr.pop(-1)
            arr.append(sum1)
        elif S[i]=='*':
            sum1=arr[-1]*arr[-2]
            arr.pop(-1)
            arr.pop(-1)
            arr.append(sum1)
        elif S[i]=='/':
            sum1=arr[-2]/arr[-1]
            arr.pop(-1)
            arr.pop(-1)
            arr.append(sum1)
print(arr[0])