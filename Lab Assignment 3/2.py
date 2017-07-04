# David Ziama
# Class ID 3
# Create a list of tuples. Sort the list by last element of tuple in increasing order.



def sorted_list(tuples):
  return sorted(tuples, key=list)

def list(n):
  return n[-1]

print(sorted_list([(1, 6), (1, 7), (4, 5), (2, 2), (1, 3)]))

