#write a program that generates 5 random numbers in the range 10 to 50.use a seed value of 6 .make a provision to change this seed value every time you execute the program by associating it with time of execution?
from random import randint,random #,seed
# from datetime import time
y=0
# seed(time()) #if we seed the random number generation logic with current time,we get different random numbers on each execution of the program
print("using for loop")
for x in range(5):
    print(randint(10,50))  #generate the random integer in the range
print("using while loop")
while y<5:
    print(randint(10,50)) #generate the random integer in the range 
    y=y+1
print("using the random function")
for x in range(5):
    print(random())     #generate the rondom float number in between 0 to 1