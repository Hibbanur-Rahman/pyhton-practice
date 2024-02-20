#we are taking the input from the user in x0,x1,x2 and x3 in the form of one by one 
x0=int(input("enter the value of x0:"))
x1=int(input("enter the value of x1:"))
x2=int(input("enter the value of x2:"))
x3=int(input("enter the value of x3:"))

arr=[] #this is the list which is easy for the traversing in the data
arr.append(x0)  #it the append the data in list arr
arr.append(x1)
arr.append(x2)
arr.append(x3)

#we are traversing the array or list in iterative form index 0 to len(arr)-1
for i in range(0,len(arr)-1):
    arr[i]=arr[i+1]
    # we are assinging the arr[i] to arr[i+1]
    # x0=x1 and further move x1=x2 and such that x2=x3
    #x3 is remain same we change the value of x3 in next step
arr[-1]=x0  #the x3 is data is assing in the arr[3] or arr[-1] if we are taking the reverse indexing
# and assign the x3 to x0
print(arr)
#we are printing the arr or x0,x1,x2 and x3