from Q3input import *

# Your code - begin
b = list(inp)
dic = {}
d=0
l1 = []


l2 = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

for i in b: # making a list of letters in lowercase.
    if (i.lower()) in l2:
        l1.append(i.lower())

for j in l1: # making a dictionary with letters and its strength
    if j in dic.keys():
        dic[j] = dic[j] + 1

    else:
        dic[j] = 1

for k in dic.keys():
    if dic[k] != 1:
        d = 1
	break

if d == 1:
    output = "false"

else:
    output = "true" 


# Your code - end
print output
