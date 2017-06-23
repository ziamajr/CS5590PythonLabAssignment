#David Ziama - ClassID #3
#Task 2:  - Write a Python program to check if a string contains all letters of the alphabet
#June 22, 2017

#Print out description of program with a space
print("This program will check if a string contains all letters of the alphabet")
print("\n")

#Ask user to enter their string
usr_str = (input("Please enter your string to be evaluated: "))

#compare the user's string to letter of the alphabet using is alpha
#isalpha() is used to return true if all characters in the string are alphabetic and there is at least one character, false otherwise.
if usr_str.isalpha():
    print("Your string contains all letters of the alphabet")
else:
    print("Your string does not contain all letters of the alphabet")



#David Ziama - ClassID #3
#Task 3:  - Write a Python program to find those numbers which are divisible by 7 and multiple of 5, between 1500 and 2700
#June 22, 2017

#using conditional loop we find the those numbers within the range
num = [i for i in range(1500,2701) if i%7==0 and i%5==0]
#we then print out what our program is doing plus those numbers
print("The numbers that are divisible by 7 and multiple of 5, between 1500 and 2700 are:", num)
