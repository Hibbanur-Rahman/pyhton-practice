#what will be the output of the following program?
s='HumptyDumpty'
print('s=',s)
print(s.isalpha())
print(s.isdigit())
print(s.isalnum())
print(s.isupper())
print(s.islower())
print(s.startswith('Hump'))
print(s.endswith('Dump'))



def stringComparsion(s1, s2):
    i=0
    count=0
    while(True):
        if s1[i]==s2[i] and s1[i]!='n' and s2[i]!='n':
            count+=1
            i+=1
        if s1[i]!=s2[i]:
            if s1[i]>s2[i]:
                return 1
            if s1[i]<s2[i]:
                return -1
        if s1[i]==s2[i] and s1[i]=='n' and s2[i]=='n':
            if s1[i:].startswith('ng') and s2[i:].startswith('ng')==False:
                return 1
            if s1[i:].startswith('ng')==False and s2[i:].startswith('ng'):
                return -1
            if s1[i:].startswith('ng') and s2[i:].startswith('ng'):
                count+=2
                i+=2
            if s1[i:].startswith('n') and s2[i:].startswith('n'):
                count+=1
                i+=1
        if count==len(s1):
            return 0

s1 = "abcno"
s2 = "abcnk"
print(stringComparsion(s1,s2))
