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