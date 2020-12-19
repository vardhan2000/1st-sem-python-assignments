def diamond(n, c):
    
    if n % 2 != 0:
	a = n
	row = 1
	n = 1
	b = (a + 1) / 2 #b is the middle row

	while row <= a:
	    column = 1
		    
	    #printing the spaces before that number in every row
	    while column <= abs(b - row):
		print("\b "),
		column += 1

	    #printing the number in every row
	    column = 1
	    while column <= 2 * n - 1:
		print("\b" + c),
		column += 1

	    print("\r")

	    if row < b: #no. of elements increase till bth row
		n += 1

	    elif row >= b: #no. of elements decrease from (b + 1)th row onwards
		n = n - 1

	    row += 1


