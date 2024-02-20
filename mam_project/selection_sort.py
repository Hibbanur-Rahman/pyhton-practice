def selection_sort(arr):
    #the first loop is run that the traversing the whole array and run as the number of passes
    for i in range(0,len(arr)-1):
        #declare the minimum to arr[i]
        min=arr[i]
        k=i
        #assign the k as i
        #second loop is finding the minimum in the remaining array and finding the position of minimum
        for j in range(i,len(arr)):
            if min>arr[j]:
                min=arr[j]
                k=j
        #swaping the arr[i] to the position of minimum and its value
        arr[i],arr[k]=arr[k],arr[i]
        #print the value after each passes
        print(arr)
    #print the array after the swaping
    print("the sorted array is: ",arr)


#we are taking the input from the user
#then user should kept in mind that the input is in the form 1 2 3 4 it means after every number you should space  not the press the enter
arr=list(map(int,input("enter the array: ").split()))
print("the unsorted array is: ",arr)

#call the selection_sort() function which take the parameter which is unsorted array and print the all passes 
selection_sort(arr)
