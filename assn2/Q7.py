from Q7input import *

# Your code - begin
ans = []

for i in l2:
    l1.append(i)

while len(l1) > 1:
    a = min(l1)
    ans.append(a)
    l1.remove(a)

ans.append(l1[0])

output = ans


# Your code - end
print output
