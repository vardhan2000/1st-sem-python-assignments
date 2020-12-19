def even_elements(l):
## Your code - begin
	l1 = [i for i in l if i % 2 == 0]
	return l1

## Your code - end
  
if __name__ == "__main__":
  l = range(10)
  print "input = ", l
  print even_elements(l)
