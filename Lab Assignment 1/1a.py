#David Ziama - ClassID #3
#Lesson 1
#Lab Assignment 1a
#Check whether a number input by the user is even or odd

print("This program will check whether a number input by the user is even or odd")
print("\n")

number = int(input("Enter number: "))
if (number % 2) == 0:
   print("Number entered by user is even")
else:
   print("Number entered by user is odd")