#David Ziama - ClassID #3
#Lesson 1
#Lab Assignment 1c
#This is a number guess exercise.
# First pick a random digit via program i.e 0,1,2,3,4,5,6,7,8,9
# Ask the user to guess the digit randomly picked by your program.
# Then print whether the number guess by the user is perfect or below the random
# number or above the random number. Also your program should explain the rules
# of this number guess game to the user.


print("Ask the user to guess the digit randomly picked by your program.")
print("Then print whether the number guess by the user is perfect or below the random number or above the random number.")
print("\n")


import random
prog_guess = random.randrange(0,9)
print("A random number has been generated by the program.\n")

usr_guess = int(input("Guess the digit: "))
print("\n")

if usr_guess == prog_guess:
    print("Your answer is PERFECT!! Congratulations!!")
elif usr_guess > prog_guess:
    print("Your answer is high than required")
elif usr_guess < prog_guess:
    print("Your answer is low than required")

print("\n")
print("The program guessed", prog_guess,". Thank you for playing")