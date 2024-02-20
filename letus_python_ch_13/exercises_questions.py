"""Write a program that defines a function count_lower_upper( ) that
accepts a string and calculates the number of uppercase and
lowercase alphabets in it.it should return these values as a dictionary.call this function for some sample strings"""

def count_lower_upper(s):
    upper_count=0
    lower_count=0
    for i in range(0,len(s)):
        if s[i].isupper():
            upper_count+=1
        elif s[i].islower():
            lower_count+=1
    count=[]
    count.append(upper_count)
    count.append(lower_count)
    return count

#this is main function
s=input("enter the string: ")
count1=count_lower_upper(s)
print("the uppercase letter in the "+s+" is",count1[0])
print("the lowercase letter in the "+s+" is",count1[1])


"""
Write a program that defines a function compute( ) that calculates
the value of n + nn + nnn + nnnn, where n is digit received by the
function. Test the function for digits 4 and 7
"""

def compute(n):
    n1=str(n)
    n2=n1+n1
    n3=n1+n1+n1
    n4=n1+n1+n1+n1
    sum=int(n1)+int(n2)+int(n3)+int(n4)
    return sum

#this is main function
n=int(input("enter the only one digit: "))
print("the sum of n + nn + nnn + nnnn is ",compute(n))


"""
    Write a program that defines a function create_array( ) to create
    and return a 3D array whose dimensions are passed to the function.
    Also initialize each element of this array to a value passed to the
    function.
"""
