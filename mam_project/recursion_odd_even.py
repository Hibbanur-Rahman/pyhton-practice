#we are trying the write the python progam which is sum of all odd or even numbers sum 1 to n or 0 to n using recursion

#this function is taking the parameter num which is user is enter the number and sum the all odd or even based opoun the nuber 
def bad_sum(num):
    if num<=0:
        return 0 #if the numbeis zero the function is reurn the zero 
    # calling the function bad_sum(num-2) it self  which is called resursion
    # first a fall zero or 1 is added and the further the resursion is processesd
    return num+bad_sum(num-2)

#we taking the input which is number from  the user 
num=int(input("enter the number:"))
#we print the sum calling the bad_sum function
print("the sum of 0 to",num,"is ",bad_sum(num))
