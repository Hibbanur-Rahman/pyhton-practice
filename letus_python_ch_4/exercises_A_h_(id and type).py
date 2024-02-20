#what will be the output of the following code snippet?
#print(id('Imaginary'))
#print(type('Imaginary'))
print(id('Imaginary'))
print(type('Imaginary'))

s3='C:\\Users\\kantekar\\Documents'
print(s3)
print(s3.split('\\'))
print(s3.partition('\\'))

#what will thw output of the following code snippet?
s1=s2=s3="hibban"
print(id(s1),id(s2),id(s3)) #the output is same because the object is same but the class is different

s=12
n=5
arr=[1,2,3,7,5]
sum1=0
i=0
j=0
num=[]
for i in range(0,n):
    if sum1<s:
        sum1+=arr[i]
        i+=1
        print(sum1)
    elif sum1>s:
        while sum1<=s:
            sum1=sum1-arr[j]
            j+=1
            if sum1==s:
                num.append(j)
                num.append(i)
                print(num)
                break
    elif sum1==s:
        num.append(j)
        num.append(i)
        break
if len(num)==0:
    num.append(-1)
print(num)