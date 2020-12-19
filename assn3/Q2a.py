from Q2input import *

# Your code - begin
output = {}

#Appending the key,value pair to the output dictionary
for i in Dic1.keys():
    if Dic1[i] not in Dic2.keys():
        output[i] = Dic1[i]
for j in Dic2.keys():
    if Dic2[j] not in Dic1.keys():
        output[j] = Dic2[j]


#Adding the 2 values with same key and then appending it to output dictionary 
for k in Dic1.keys():
    if k in Dic2.keys():
        output[k] = Dic1[k] + Dic2[k]


# Your code - end
print output
