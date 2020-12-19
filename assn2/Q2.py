from Q2input import *

# Your code - begin
l1 = list(inp)

l2 = []

if l1[0] == '(' or l1[0] == '{' or l1[0] == '[':

    for i in l1:
        if i == '(' or i == '{' or i == '[':
            l2.append(i)

        elif i == ')' and l2[-1] == '(':
            l2.pop()

        elif i == '}' and l2[-1] == '{':
            l2.pop()

        elif i == ']' and l2[-1] == '[':
            l2.pop()

else :
    l2 = [1]

if l2 == []:
    output = "bounded"

else:
    output = "unbounded"


# Your code - end
print output
