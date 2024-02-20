import datetime

timestamp = 1698324887.477289
date_time = datetime.datetime.utcfromtimestamp(timestamp)

print(date_time)



N=3
Dictionary=["WelcomeGeek",
"WelcomeToGeeksForGeeks","GeeksForGeeks"]
Pattern="WTG"
short=[]
for i in range(0,N):
    s=''
    s1=Dictionary[i]
    for j in range(0,len(s1)):
        print(s1[j])
        if ord(s1[j])>=65 and ord(s1[j])<=90:
            s=s+s1[j]
    short.append(s)
print(short)

name1='hi'
name2='hibban'
print(name1==name2)