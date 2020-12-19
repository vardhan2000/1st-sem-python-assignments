def diamond():
    row = 1
    n = 1

    while row <= 5:
        column = 1

	#printing the spaces before the stars in every row
        while column <= abs(3 - row):
            print("\b "),
            column += 1

        #printing the stars in every row
        column = 1
        while column <= 2 * n - 1:
            print("\b*"),
            column += 1

        print("\r")

        if row < 3: #no. of stars increase till 3rd row 
            n += 1

        elif row >= 3: #no. of stars decrease from 4th row onwards
            n = n - 1

        row += 1




