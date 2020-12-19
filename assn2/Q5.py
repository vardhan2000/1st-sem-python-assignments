from Q5input import *

# Your code - begin
output = l[:]

a = 0

while a <= (len(l) - 1):
    if a + n <= (len(l) - 1):
        output[a] = l[a + n]

    else:
        output[a] = l[a + n - (len(l))]

    a = a + 1


# Your code - end
print output
