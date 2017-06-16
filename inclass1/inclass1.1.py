
#Python program to reverse a number and print it
import math

num = int(input("Enter the number to be reveresed: "))
rev = 0
while (num > 0):
    rem = num % 10
    rev = (rev * 10) + rem
    num = num // 10

print("\n The reverse of the number entered is = %d" % rev)