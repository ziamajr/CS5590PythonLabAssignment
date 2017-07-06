# David Ziama
# Class ID 3
# Write a Python program to create a symmetric difference.
# July 6, 2017


# The symmetric difference of two sets is the set of elements that are unique to each set

# Get items list from user.
# In this case I decided to use a person an their friends three favorite countries

user1 = input("What is User 1 name: ")
user2 = input("what is User 2 name: ")
print("\n")
print("Welcome to my symmetric difference finder", user1, "and", user2, ".")
print("This program will ask each of you for your favorite countries and see if you have any in commom")
print("\n")
one = input("User 1, What is your first favorite country? ")
two = input("User 1, What is your second favorite country? ")
three = input("User 1, What is your third favorite country? ")
four = input("User 2, What is your first favorite country? ")
five = input("User 2, What is your second favorite country? ")
six = input("User 2, What is your third favorite country? ")

# Define the sets

user1_list = set([one, two, three])
user2_list = set([four, five, six])

# Set symmetric difference
sym_diff = user1_list ^ user2_list

# Print the symmetric difference
print("The Symmetric Diffrence of" , user1, "and", user2, "favorite countries is" ,sym_diff)