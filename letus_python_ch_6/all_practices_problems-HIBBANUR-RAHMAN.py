#write a program that receives 3 sets of values of p,n and r and calculates simple interest for each
i=1
while i<=3:
    p=float(input("enter the principle amount:"))
    n=float(input("enter the time in year:"))
    r=float(input("enter the rate of interest:"))
    si=p*n*r/100
    print("the simple interest of principle amount="+str(p),",time="+str(n),"and rate="+str(r),"% \is",str(si))
    i=i+1

#write a program that prints numbers from 1 to 10 using an infinite loop.all numbers should printed in the same line

i=1
a=[]
while 1:
    print(i,end=' ')
    if i==10:
        break
    i=i+1

# write the programs to print the all unique combinations of 1,2 and 3
i=1
while i<=3:
    j=1
    while j<=3:
        k=1
        while k<=3:
            if i==j or j==k or i==k:
                k+=1
                continue
            else:
                print(i,j,k)
            k+=1
        j+=1
    i+=1
    
# write a program that obtains decimal value of a binary numeric string 
#For example ,decimal value of '1111' is 15

a=input("enter the binary number:")
b=len(a)
i=1
j=0
sum=0
while i<=b:
    c=int(a[j])*(2**(b-i))
    sum=sum+c
    i+=1
    j+=1
print("the decimal number is",sum)

#the second method of binary to decimal conversion is 
b=input("enter the binary number:")
i=0
while b:
    i=i*2+(ord(b[0])-ord('0'))
    b=b[1:]
print('Decimal value='+str(i))

#write a program that generates the following output using a for loop:
#A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z,z,y,x,w,v,u,t,s,r,q,p,o,n,m,l,k,j,i,h,g,f,e,d,c,b,a,
for alpha in range(65,91):
    print(chr(alpha),end=',')
for alpha in range(122,96,-1):
    print(chr(alpha),end=',')