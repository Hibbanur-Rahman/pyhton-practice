#if we wish to work with an individual word in the following string,how will you separate them out:
#'The difference between stupidity  and genius is that genius has its limits'
a='The difference between stupidity  and genius is that genius has its limits'
b=a.split(' ')
print(b)

N=int(input())
char1=[]
for i in range(65,65+27):
    char1.append(chr(i))
print(char1)
print(char1[-1])
excel=''
while N>26:
    c=N%26
    excel=char1[c-1]+excel
    N=N//26
excel=char1[N-1]+excel
print(excel)

print('n'=='ng')