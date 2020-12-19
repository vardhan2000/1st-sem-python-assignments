from Q5input import *

# Your code - begin
l1 = list(set1)
l2 = list(set2)

sets = []


# Forming a list of all possible combinations of elements of sets1 and sets2

for i in l1:
    for j in l2:
        b = i + j
        sets.append(b)
l4 = []
print(sets)
c=0
d=0
l3 = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']


# checking the no.of complete strings in l4 list

for j in sets:
	for k in l3:
		if k not in list(j):
			c = 1
			break
		else:
			c = 0
	
	if c == 0:
		d += 1

output = d

# Your code - end
print output
