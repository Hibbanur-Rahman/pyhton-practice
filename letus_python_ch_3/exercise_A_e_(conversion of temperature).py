#assume a suitable value for temperature of a city in farenheit degrees.write a program to convert this temperature into centigrade degrees and print both temperatures.input
 
f=float(input("enter the temperature in farenheit:"))
c=(f-32)*(5/9)
print(f,"Farenheit=",c,"Degree")