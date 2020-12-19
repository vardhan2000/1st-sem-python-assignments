from Q6input import *

# Your code - begin
l2 = []

while len(l) > 1:
    a = min(l)
    l2.append(a)
    l.remove(a)

l2.append(l.pop(0))
print(l2)

if (len(l2) % 2) != 0:
    p = (len(l2) + 1) / 2
    p = int(p)
    median =  l2[p - 1]
    output = median

elif (len(l2) % 2) == 0:
    p = len(l2) / 2
    p = int(p)
    median1 = l2[p - 1]
    median2 = l2[p]
    output = (median1 + median2) / 2.0


# Your code - end
print output
