n=int(input("enter the value of n:"))
for i in range(0,n+1):
    for j in range(0,n-i):
        print(" ",end='')
    for k in range(0,i):
        print("* ",end='')
    print('\n')
for i in range(0,n-1):
    for j in range(0,i+1):
        print(" ",end='')
    for k in range(0,n-i-1):
        print("* ",end='')
    print("\n")
