#write a program that generates the following output from the string 'Shenanigan'.

a='Shenanigan'

#extract S h
print(a[0],a[1])

#extract a n
print(a[4],a[3])

#extract enanigan
print(a[2:])

#extract Shenan
print(a[:6])
print(a[:-4])
print(a[-10:-4])

#extract Shenanigan
print(a[::])
print(a[0:])

#extract seaia
print(a[::2])

#extract snin
print(a[::3])

#extract saa
print(a[::4])

#extract ShenaniganType
print(a+"Type")

#extract ShenanWabbit
print(a+"Wabbit")