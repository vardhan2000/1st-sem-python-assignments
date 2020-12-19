from Q3input import *

# Your code - begin
if len(m1[0]) == len(m2):
    
    l1 = []
    p=0
    while p < len(m2[0]):
        l1.append(0)
        p = p + 1

    q = 0
    result = []
    while q < len(m1):
        result.append(l1[:])
        q += 1
    
    for i in range(len(m1)):
        for j in range(len(m2[0])):
            for k in range(len(m2)):
                result[i][j] += m1[i][k] * m2[k][j]

    output = result

else:
    output = "Invalid input"

# Your code - end

print(output)
