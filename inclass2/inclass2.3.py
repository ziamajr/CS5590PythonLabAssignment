string = input("Please enter the string to check: ")
digits=letters=0
for c in string:
    if c.isdigit():
        digits=digits+1
    elif c.isalpha():
        letters=letters+1
    else:
        pass
print(" There are", letters, "letters and", digits, "digits.")
