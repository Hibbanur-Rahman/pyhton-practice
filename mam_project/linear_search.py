#the python function for better_linear_search

#this function is taking the array as A and second parameter which is X for the searching in the array
def better_linear_search(A,X):
    #we assing the list which is counting the index of the data if the data is more than one time
    found=[]
    for i in range(0,len(A)):
        #we are checking the data in array
        if A[i]==X:
            #we are append the index if the data is found in the list
            found.append(i)
    #returning the found list which is containg the index of data in array
    return found

#this while is continue working if user is enter the 1 and if user is enter the 2 then the while is breaking
while(True):
    print("1.Better linear search\n2.exit\n")
    option=int(input("choose the option:"))
    if option==1:
        A=[]
        n=int(input("enter the number of element:"))
        for i in range(0,n):
            data=int(input("enter the array element: "))
            A.append(data)
        X=int(input("enter the data which you want to search: "))
        found1=better_linear_search(A,X)
        if len(found1)==0:
            print("the",X,"is not found")
        else:
            for i in range(0,len(found1)):
                print("the",X,"is found at",found1[i]+1,"th position")
    elif option==2:
        break
    else:
        print("!!you choose the wrong option !! \n!!please choose the correct option!!\n")