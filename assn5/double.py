def double(l):
## Your code - begin
	l1 = [(2 * i) for i in l]
	return(l1)

## Your code - end
  
if __name__ == "__main__":
  l = [1, 2, 3]
  print "input = ", l
  print double([1, 2, 3])
