#David Ziama - ClassID #3
#Lesson 1
#InClass 2b
#Write a python program to Take radius of a circle as input from user and calculate area , circumference and print it.



import math
print("This program will take the radius of a circle as input from a user and calculate the Area and Circumferense.")
num = float(input("What is the radius: "))
area = math.pi * num * num
cir = 2 * math.pi * num

print ("The area is %d" %area, "and the circumference is %d" %cir)