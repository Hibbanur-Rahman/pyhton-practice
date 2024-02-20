N=int(input("enter the number of line:"))
for i in range(1,N+1):
    for j in range(0,N-i):
        print(" ",end='')
    for k in range(0,i):
        print("*",end='')
    if i>1:
        for l in range(0,i-1):
            print("*",end='')
    print()