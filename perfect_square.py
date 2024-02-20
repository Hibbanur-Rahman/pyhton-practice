import math
a=1000
c=[]
while a<=9999:
    b=math.sqrt(a)
    if int(b)==b:
        c.append(a)
    a+=1
print(c)
d=[]
for x in c:
    x=str(x)
    y=int(x[:2])
    z=int(x[2:])
    if int(math.sqrt(y))==(math.sqrt(y)) and int(math.sqrt(z))==(math.sqrt(z)):
        d.append(x)
print(d)
