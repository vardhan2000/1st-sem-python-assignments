def sumDigits(n):
## Your code - begin
	if(n > 0):
		a = n % 10
		n = int(n / 10)
		return(a + sumDigits(n))

	else:
		return 0

## Your code - end

if __name__ == "__main__":
	n = input("Enter number: ")
	output = sumDigits(n)
	print output
