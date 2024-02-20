#we are trying to write a python progrom to perform the power of num of x using recursion

#this function is taking the two parameter one is number which is base and the second is power of the  number
def power_number(num,x):
    if x>1:
        x=x-1
        #we call the function power_number() itself and the number is decrement by one
        num=num*power_number(num,x)  
    #return the data num-1
    return num

#we taking the number from the user
num=int(input("enter the base number:"))
x=int(input("enter the power number:"))
if x==0:
    print(num,"**",x,"=",1)
else:
    #we call the function power_number()
     print(num,"**",x,"=",power_number(num,x))
