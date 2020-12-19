def diamond(n):
    
    if n % 2 != 0:
	a = n
	row = 1
	n = 1
	b = (a + 1) / 2 #b is the middle row

	while row <= a:
	    column = 1
				
	    #printing the spaces before the stars in every row
	    while column <= abs(b - row):
		print("\b "),
		column += 1

	    #printing the stars in every row
	    column = 1
	    while column <= 2 * n - 1:
		print("\b*"),
		column += 1

	    print("\r")

	    if row < b: #no. of stars increase till bth row 
		n += 1

	    elif row >= b: #no. of stars decrease from (b + 1)th row onwards
	        n = n - 1

	    row += 1



