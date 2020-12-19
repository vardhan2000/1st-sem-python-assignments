def ndiamond():
    row = 1
    n = 1

    while row <= 5:
        column = 1
        
        #printing the spaces before the elements in every row
        while column <= abs(3 - row):
            print("\b "),
            column += 1

        #printing the varying numbers in every row using a variable t
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

        if row < 3: #no. of elements increase till 3rd row
            n += 1

        elif row >= 3: #no. of elements decrease from 4th row onwards
            n = n - 1

        row += 1



