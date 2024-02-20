"""in a company an employee is paid as under:
if his basic salary is less than Rs.1500,then HRA=10% of basic salary and DA=90% of basic salary.
if his salary is either equal to or above Rs.1500 ,then HRA=Rs.500 and DA=98% of basic salary.if the 
employee's salary is input through the keyboard write a program to find his gross salary
"""
salary=float(input("enter the salary:"))
if(salary<1500):
    HRA=10
    DA=90
    gross_salary=salary+(salary*HRA/100)+(salary*DA/100)
elif(salary>=1500):
    HRA=500
    DA=98
    gross_salary=salary+(HRA)+(salary*DA/100)
print("the gross salary is Rs",gross_salary)
