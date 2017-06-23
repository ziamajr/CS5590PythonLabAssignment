#David Ziama - ClassID #3
#Task 1:  - Write a python program that prints the first letter of your name with stars
#June 22, 2017

#Print out a statemet that tells them what the program does
print("This program will print the first letter of your name with stars ")
print("\n")

#row of stars
across = 7

#columns of stars
down = 7

across = 5
down = 5
bottom = 4

for i in range(1, down + 1):
    for j in range(1, across + 1):
        if (i == 1):
            print("*", end='')
        elif (j == 1 or j == 5):
            print("*", end='')
        elif (j != 6):
            print(" ", end='')
    for j in range(1, bottom + 1):
        if (i == 5):
            print("*", end='')
    print("\n")
