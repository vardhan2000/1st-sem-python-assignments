#defining a function to print a greeting surrounded by stars 

def banner(m):
    n = list(m)
    k = 0 #variable for addressing the elements of the list made in the program
    row = 0
    while row < 3:
        column = 0

        while column < (len(n) + 4):
								            
			#printing stars in the 1st and the 3rd row			
            if row == 0 or row == 2:
                print("\b*"),
            
			#for the 2nd row
            else:

				#printing stars for extreme positions
                if column == 0 or column == len(n)+3:
                    print("\b*"),
            
				#printing spaces for 2nd most extreme positions
                elif column == 1 or column == len(n)+2:
                    print("\b "),
            
				#printing the greeting in the middle
                else:
                    print "\b{a}".format(a = n[k]),
                    k += 1
            
            column +=1
        
        row += 1
        
        print("\r")

       





