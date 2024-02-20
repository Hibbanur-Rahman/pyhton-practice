#Write a Python program to display a user-entered name followed by Good Afternoon using input() function
name=input("enter the name:")
print("Good Afternoon "+name)
#Write a program to fill in a letter template given below with name and date.
name=input("enter the name:")
print('''letter=\'\" Dear '''+name,'''
                        You are selected!
                        Date:14/10/22
''')
name=input("enter the name:")
print('''\'\" Dear '''+name,'\n\tYou are selected!\n\tDate:14/10/22')
#Write a program to detect double spaces in a string.
a=input("enter the any string:")
b=a.count("  ")
print("the double spaces in ",a," is ",b)
#Replace the double spaces from problem 3 with single spaces.
a.replace("  "," ")
print(a)
#Write a program to format the following letter using escape sequence characters
print("letter=","\"Dear "+name,"This python course in nice.Thanks!!\"")

a=[1,2,3,4,5,5]

a=str(a)
b=a.find("1")
print(b)