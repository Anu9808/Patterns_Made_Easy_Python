# Input = 5
# Output
'''
    *       *
   * *     * *
  *   *   *   *
 *     * *     *
*       *       *

'''

n=int(input("Enter number of rows"))

for row in range(1,n+1):
    for space in range(1,n-row+1):
        print(" ",end="")
    for col in range(1,2*row):
        if col == 1 or col == 2*row-1:
            print("*",end="")
        else:
            print(" ",end="")

    for space in range(1,2*(n-row)):
        print(" ",end="")
    
    if row < n:
        for col in range(1,2*row):
            if col == 1 or col == 2*row-1:
                print("*",end="")
            else:
                print(" ",end="") 
    else:
        for col in range(1,2*row-1):
            if col == 2*row-2:
                print("*",end="")
            else:
                print(" ",end="")

    print()
