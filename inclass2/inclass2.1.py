#Calculate character frequency in a string
def freq(line):
    letter = {}
    for n in line:
        keys = letter.keys()
        if n in keys:
            letter[n] += 1
        else:
            letter[n] = 1
    return letter
print(freq('hello'))