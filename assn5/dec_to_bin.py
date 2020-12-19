def recurse(ans, n):
## Your code - begin
	if n > 0: # (n > 0) is the base case to exit recursion
		a = n % 2 
		n = int(n / 2)
		ans = ans + str(a)
		return(recurse(ans, n))

	else:
		if ans:
			return(ans[::-1]) # returning the reverse of the string 'ans'.

		else:
			return "0" # if n = 0 and 'ans' liat is empty.

## Your code - end

def decToBin(n):
  return recurse("", n) 

if __name__ == "__main__":
  n = input("Enter number: ")
  output = decToBin(n)
  print output
