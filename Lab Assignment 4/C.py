# David Ziama
# Class ID 3
# Write a Python program toget a comma separated sequence of words then the output should be sorted in comma separated manner.
# July 6, 2017


# Get list of words from users
user_input = input("Please enter your words seperated by commas: ")

# Print out the inputs so user can see them
print("Input: ", user_input)

# breakdown the string into a list of words
str = user_input.split(',')

# Sort and print sorted comma separated list
for word in str:
    sorted_words = (", ".join(sorted(set(str))))
print("Output: ", sorted_words)

