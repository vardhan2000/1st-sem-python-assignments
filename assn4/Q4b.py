def ndiamond(n):
    
    if n % 2 != 0:    
	a = n
	row = 1
	n = 1
	b = (a + 1) / 2 #b is the middle row

	while row <= a:
	    column = 1

	    #printing the spaces before the elements in every row
	    while column <= abs(b - row):
		print("\b "),
		column += 1

	    #printing the varying numbers in every row by the help of a variable 't'  
	    column = 1
	    t = 1
	    while column <= 2 * n - 1:
		print("\b" + str(t)),

		if column < n: #no. increase nth column
		    t += 1

		elif column >= n: #no. decrease from (n + 1)th column onwards
		    t = t - 1
		column += 1


	    print("\r")

	    if row < b: #no. of elements increase till bth row
		n += 1

	    elif row >= b: #no. of elements decrease from (b + 1)th row onwards
		n = n - 1

	    row += 1






