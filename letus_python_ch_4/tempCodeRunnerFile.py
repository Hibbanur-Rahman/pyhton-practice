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