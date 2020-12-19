# Array printing utility function. Feel free to use.
def printArr(arr, k): 
  for i in range(k): 
    print(str(arr[i]) + " "), 
  print
  
def printSeqUtil(n, k, len1, arr):  
## Your code - begin
	# 'len1' helps in addressing the index we want to insert element into. (len1 - 1) represents the current index.
	# 'arr' is the temporary list to store the sequences. It will store one sequence at a time. 
	# Jobs of 'n' and 'k' are already mentioned in the question


	# if len1 = k then (len - 1) is at the last index of the list. Hence, elements need to be printed now. 
	if (len1 == k): 
		printArr(arr, k) 
		return 

	# i stores the value to be inserted at the current index.
	# if len1 = 0 then the value of i should be assreted to 1. Otherwise increase the value of previous element by 1 and store it in i. 
	if(len1 == 0):
		i = 1

	else:
		i = arr[len1 - 1] + 1


	# Increasing len1 by 1 and hence 'the index that is needed to be addressed' by 1. 
	len1 += 1; 

	# putting all the numbers greater than the previous element at the new index
	while (i <= n): 
		arr[len1 - 1] = i; 
		printSeqUtil(n, k, len1, arr); 
		i += 1;
## Your code - end
  
def printSeq(n, k): 
    arr = [0] * k  
    len1 = 0
    printSeqUtil(n, k, len1, arr) 

if __name__ == "__main__":
  n = input("Enter n: ")
  k = input("Enter k: ")
  printSeq(n, k)
