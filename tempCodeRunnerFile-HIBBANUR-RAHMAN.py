import math
a=1000
c=[]
while a<=9999:
    b=math.sqrt(a)
    if int(b)==b:
        c.append(a)
print(c)