# David Ziama
# Class ID 3
# Write a function to replace dictionary values with their sum. Use a list which contains three dictionaries. For example [{},{},{}]. Then sum the values of the dictionaries if they are integer.
# July 6, 2017


# Our User Inout
user_input = [{'course': 'python', 'LastGPA' : 90, 'CurrentGPA' : 80},
{'course': 'python', 'LastGPA' : 95, 'CurrentGPA': 85},
{'course': 'python', 'LastGPA' : 100, 'CurrentGPA': 100}]

# define my fucntion
def gpa_avg(dict1):
    #loop through and find the average
    for x in dict1:
        x['LastGPA+CurrentGPA'] = (x.pop('LastGPA') +x.pop('CurrentGPA'))/2
    return dict1

# Print our input again
print(user_input)
# Print our output
print(gpa_avg(user_input))