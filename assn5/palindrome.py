def recurse(n, i):
## Your code - begin
	n1 = [j.lower() for j in n] # converting each  of the element to lowercase
	if i == int((len(n1) - 1) / 2) and (n1[i] == n1[len(n1) - i - 1]):
		return True

	elif i <= int((len(n1) - 1) / 2) and (n1[i] != n1[len(n1) - i - 1]):
		return False

	else:
		return recurse(n, i + 1)
## Your code - end

def isPalindrome(n):
  return recurse(n, 0)
  
if __name__ == '__main__':
	n = raw_input("Enter string: ")
	output = isPalindrome(n)
	print output
