"""
    what are Dictionaries?
    --dictionary is a collection of key-value pairs
    --dictionaries are also known as maps or associative arrays
    --a dictionary contains comma separated key : value pairs enclosed within {}.
"""
d1={}   #empty dictionary
d2={
    'a210044':'hibban',
    'a210055':'Ramsha',
    'Raani':'Ramsha',
    'a210057':'bushra',
    'Baaji':'Bushra'
}
print(d2.values())
print(d2.keys())

#Dictionaries cannot be sliced using []
#Elements are not position indexed,but key indexed

d2={
    'a210044':'hibban',
    'a210055':'Ramsha',
    'Raani':'Ramsha',
    'a210057':'bushra',
    'Baaji':'Bushra'
}

#iterate over key-value pairs
for k,v in d2.items():
    print(k,v)

#iterate over keys
for k in d2.keys():
    print(k)

#iterate over values
for v in d2.values():
    print(v)

#iterate over keys 
for k in d2:
    print(k)

# n1=int(input("enter number:"))
# n2=int(input("enter number:"))
# n3=int(input("enter number:"))
# n4=int(input("enter number:"))
# if(n1>n2):
#     l1=n1
# else:
#     l1=n2
# if(n3>n4):
#     l2=n3
# else:
#     l2=n4
# if(l1>l2):
#     print(l1,"is gretest number")
# else:
#     print(l2,"is gretest number")

"""
    write a program to create a dictionary of hindi words with values as their english translation.provides user with an option to look it up!
"""
dict={
    'likho':'write',
    'padho':'read',
    'chalo':'walk',
    'pyaar':'love',
    'raani':'ramsha'
}

for k in dict.keys():
    print(k)
user=input("enter the key:")
for k,v in dict.items():
    if k==user:
        print(k,v)

"""

"""
dict={}
for i in range(0,4):
    name=input("enter the name of the friend:")
    subject=input("enter the subject:")
    dict[name]=subject
for k,v in dict.items():
    print(k,v)
