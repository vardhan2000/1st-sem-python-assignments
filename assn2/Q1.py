from Q1input import *

# Your code - begin
inputs = list(inp) #converting string input into list of characters
list1 = [] #list for storing various characters and their corresponding strength
output=""
while inputs:  #This loop will run until inputs list becomes empty
  a = inputs.pop(0)
  list2 = []

  while inputs[0] == a: #loop for creating list of same types of characters
    list2.append(inputs.pop(0))
    if len(inputs) < 1:
          break

  b = (len(list2) + 1)       
  list1.append(b)
  list1.append(a)
  
for m in list1 : #printing the elements of list1
  output=output+str(m)



# Your code - end

print output
