def bubble_sort(arr):
    #the first for loop run the number of passes
    for i in range(0,len(arr)-1):
        #the second loop bubble out the biggest one
        for j in range(0,len(arr)-1-i):
            #checking the elements and swapping the elements
            if arr[j]>arr[j+1]:
                #for swapping the two elements
                arr[j],arr[j+1]=arr[j+1],arr[j]
        #print the array after each passes
        print(arr)
    #print the array after sorting
    print("the sorted array is",arr) 

#we are taking the input from the user
#then user should kept in mind that the input is in the form 1 2 3 4 it means after every number you should space  not the press the enter
arr=list(map(int,input("enter the array: ").split()))

print("the unsorted array: ",arr)
#we call the bublle_sort() which take the parameter which is array which you want to sort
bubble_sort(arr)