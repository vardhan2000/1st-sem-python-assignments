from Q6input import *

# Your code - begin
l2 = []

while len(l) > 1:
    a = min(l)
    l2.append(a)
    l.remove(a)

l2.append(l.pop(0))

mean = float(sum(l2)) / len(l2)

output = mean

# Your code - end
print output
