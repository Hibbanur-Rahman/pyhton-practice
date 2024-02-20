#A company insures its drivers in the following cases:
#if the driver is married 
#if the driver is unmarried,male & above 30 years of age.
#if the driver is unmarried,female &above 25 years of age.
#in all other cases,the driver is not insured.if the maritial status,sex and age of the driver are the inputs,
# write a program to determine whether the driver should be insured or not.

maritial_status=input("enter the maritial status married or unmarried:")
sex=input("enter the sex(male or female):")
age=int(input("enter the age :"))
if(maritial_status=="married"):
    print("the driver is insured")
elif(maritial_status=="unmarried" and sex=="male" and age>=25):
    print("the driver is insured")
elif(maritial_status=="unmarried" and sex=="female" and age>=30):
    print("the driver is insured")
else:
    print("the driver is not insured")