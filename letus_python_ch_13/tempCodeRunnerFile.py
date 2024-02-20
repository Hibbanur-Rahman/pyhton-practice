a=28
b=28
while(True):
    c=b%a
    if c==0:
        break
    b=a
    a=c
print(a)