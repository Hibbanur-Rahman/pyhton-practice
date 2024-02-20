def fun():
    # name conflict. local a shadows out global a
    a=10
    # name conflict, use global b
    global b
    b=45

    # uses local a, global b and s
    # no need to define s as global,since it is not being changed
    print(a,b,s)

# global identifiers
a=12
b=13
s='hibban'
fun()
print(a,b,s)    # b has changed, a and s are unchanged



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
    
