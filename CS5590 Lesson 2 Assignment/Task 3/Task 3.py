#David Ziama - ClassID #3
#Task 3:  - Write a Python program to find those numbers which are divisible by 7 and multiple of 5, between 1500 and 2700
#June 22, 2017

#using conditional loop we find the those numbers within the range
num = [i for i in range(1500,2701) if i%7==0 and i%5==0]
#we then print out what our program is doing plus those numbers
print("The numbers that are divisible by 7 and multiple of 5, between 1500 and 2700 are:", num)
