#takes a list of words and returns the length of the longest one

text = input("Please input a list of words to use: ")
length = 0
for words in text.split():
 if len(words) > length:
    length = len(words)
    longest = words

print("The longest word is", longest, "with length", len(longest))