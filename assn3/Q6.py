from Q6input import *

# Your code - begin
inp = list(inp)
inp1 = []

# Enlisting the letters without spaces
for i in inp:
    if i != " ":
        inp1.append(i.lower())

dic = {}

# forming dictionary with letters as keys and their strength as the values
for j in inp1:
    if j in dic.keys():
        dic[j] = dic[j] + 1

    else:
        dic[j] = 1


l1 = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
l2 = []

# storing the values of dic in l2
for i in dic.values():
    l2.append(i)


l3 = list(set(l2))
l3.sort(reverse=True) #sorting in descending order

a = l3[N-1]


l4 = []
for k in dic.keys():
    if dic[k] == a:
        l4.append(l1.index(k))

b = min(l4)
output = l1[b]


# Your code - end
print output
