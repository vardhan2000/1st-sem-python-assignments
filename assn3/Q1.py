from Q1input import *

# Your code - begin

#To iterate over the elements of the list and make a dictionary which contains the keys as the elements and their count as the value of the key.

output = {}

for i in inp:
    if i in output.keys():
        output[i] = output[i] + 1 

    else:
        output[i] = 1

# Your code - end

print output
