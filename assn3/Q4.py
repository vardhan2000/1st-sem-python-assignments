from Q4input import *

# Your code - begin

#first list comprehension is to make the list free from zeros while the second list comprehension is to add same no. of zeros at the end of list

output = [x for x in inp if x != 0] + [a for a in inp if a == 0]


# Your code - end
print output
