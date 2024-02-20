def insertion_sort(arr):
    #the first loop run the number of times of passes and the partition is going one is sorted and another is unsorted
    for i in range(1,len(arr)):
        #the key which is unsorted first element
        key=arr[i]
        #second loop is work that the key is placed at proper place in sorted array which
        for j in range(i,-1,-1):
            #we compare the key in sorted array and update the array 
            if key<arr[j]:
                arr[j],arr[j+1]=key,arr[j]
        #we print the array after every passes
        print(arr)
    #print the array after sorting the array
    print("\nthe sorted array is :",arr)


#we are taking the input from the user
#then user should kept in mind that the input is in the form 1 2 3 4 it means after every number you should space  not the press the enter
arr=list(map(int,input("enter the array: ").split()))
print("the unsorted array is: ",arr)
#we call the insertion_sort() which take the parameter as array and print the sorting passes
insertion_sort(arr)