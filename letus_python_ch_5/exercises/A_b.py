x=3
y=3.0
if x==y:
    print(x,"and",y,"are equal")
else:
    print(x,"and",y,"are  not equal")

k=6
a=[76, 91, 3, 22, 79, 57, 83, 41, 9, 76, 47, 14]
a.sort()
print(a)

n=11
arr=[3, 3, 11, 15, 20, 11, 6, 5, 15, 1, 19]
n=6
arr=[20, 10, 15, 9, 1, 12]
n=13
arr=[3, 11, 18, 9, 4, 15, 13, 3, 8, 11, 10, 12, 19]
b=arr
# for a in arr:
#     b.append(a)
arr=[]
for i in range(0,n//2):
    c=min(b)
    d=max(b)
    arr.append(str(c))
    arr.append(str(d))
    b.remove(c)
    b.remove(d)
if len(b)!=0:
    arr.append(str(*b))
    print
print(arr)
# arr=str(arr)
# arr=arr[1:-1:2]
print(' '.join(arr[0:len(arr)-1]))
print(b)

n=6
arr=[20, 10, 15, 9, 1, 12]
b=arr
b.sort()
print(b)
arr=[]
i=0
j=n-1
while i<=j:
    arr.append(b[i])
    i+=1
    arr.append(b[j])
    j=j-1         
print(arr)
