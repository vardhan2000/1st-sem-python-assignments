from Q3input import *

# Your code - begin
l1 = []

p = 0
while p < len(m1):
    l1.append(0)
    p += 1

q = 0
l2 = []
while q < len(m1[0]):
    l2.append(l1[:])
    q += 1

for i in range(len(l2)):
    for j in range(len(l2[0])):
        p = i
        q = j
        l2[i][j] = m1[q][p]

output = l2

# Your code - end
print output
