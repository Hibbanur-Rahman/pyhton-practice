#percentage marks obtained by a student are input through the keyboard.the student gets a division as per the following rules:
# percentage above or equal to 60-first division
#percentage between 50 and 59-second division
#percentage between 40 to 49  -third division
#percentage less than 40-fail
#write a program to calculate the division obtained by the student
marks=int(input("enter the percantage of marks:"))
if marks>=60 and marks<=100:
    print("First Division")
elif marks>=50 and marks<=59:
    print("second division")
elif marks>=40 and marks<=49:
    print("third division")
elif marks<40 and marks>=0:
    print("Fail")
else:
    print("you entered the wrong percentage")
