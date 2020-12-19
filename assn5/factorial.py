def factorial(n):
## Your code - begin
	if n > 0: #base case to exit recursion
		return(n * factorial(n - 1))

	else:
		return 1

## Your code - end

if __name__ == "__main__":
	n = input("Enter number: ")
	output = factorial(n)
	print output
