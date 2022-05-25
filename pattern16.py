'''
Input = 5
Output

*********
 *     *
  *   *
   * *
    *

'''
n=int(input("Enter number of rows"))

for row in range(1,n+1):

    for space in range(row-1):
        print(" ",end="")
    
    for col in range(2*(n-row)+1):
        if row == 1 or col == 0 or col == (n-row)*2:
            print("*",end="")
        else:
            print(" ",end="")
            
    print()