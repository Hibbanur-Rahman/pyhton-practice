#write a program to convert the following string 'Visit ykanetaker.com for online courses in programming' into 'Visit Ykanetaker.com For Online Courses In Programming'
a="Visit ykanetaker.com for online courses in programming"
print(a.title())
#write a program  to convert the following  string 'Light travels faster than sound.This is why some people appear bright until you hear them speak.' into 'LIGHT travels faster than SOUND.This is why some people appear bright until you hear them speak.'
a="Light travels faster than sound.This is why some people appear bright until you hear them speak."
b=a.replace('Light',"LIGHT")
c=b.replace('sound','SOUND')
print(c)