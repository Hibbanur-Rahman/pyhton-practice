animals=['zebra','tiger','lion','jackal','kangaroo']
#using while loop
i=0
while i<len(animals):
    print(animals[i],end='  ')
    i+=1
#using more convenient for loop
print()
for a in animals:
    print(a)
#using the enumerate() function

for index, a in enumerate(animals):
    print(index,a)

#list is mutable so the list is updated
animals=['zebra','tiger','lion','jackal','kangaroo']
ages=[25,26,25,27,26,28,25]
animals[2]='Rhinoceros'
ages[5]=31
ages[2:5]=[24,25,32]
ages[2:5]=[]
print(ages)
print(animals)

#identity :-wheter the two variables are referring to the same list can be checked using the is identity operator as shown below:

lst1=[10,20,30,40,50]
lst2=[10,20,30,40,50]
lst3=lst1
print(lst1 is lst2)
print(lst1 is lst3)
print(lst1 is not lst2)

#Concatenation:- one list can be concatenated(appended) at the end of another as shown below:

lst=[12,15,13,23,22,16,17]
lst=lst+[33,44,55]
print(lst)

# Merging :- two lists can be merged to create a new list.

s=[10,20,30]
t=[100,200,300]
z=s+t
print(z)

#Conversion :- A string/tuple/set can be converted into a list using the list() conversion function

l=list("Africa")
print(l)

# Aliasing:-on assinging one list to another ,both refer to the same list. changing one changes to other

lst1=[10,20,30,40]
lst2=lst1
print(lst1)
print(lst2)
lst1[0]=100
print(lst1[0],lst2[0])

#searching

lst=['h','i','b','b','a','n']
res='i' in lst #return True since 'i' is present in list
print(res)
res='u' in lst #return False since 'u' is not present in list
print(res)

#identity
lst1=[10,20,30,40,50]
lst2=[10,20,30,40,50] 
lst3=lst1
print(lst1 is lst2) #because the element is same but don't say that the list is also same 
print(lst3 is lst1)

#comparison:- Comparison is done item by item till there is a mismatch.

a=[1,2,3,4]
b=[1,2,5]
print(a>b)

#Emptiness:- we can check if a list is empty using not operator

lst=[1]
if not lst:
    print('Empty list')
else:
    print("the list is not empty")

