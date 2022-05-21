'''
Input = 5
output

    *
   * *
  *   *
 *     *
*********

'''

#First Approach
'''
n = int(input("Enter number of rows"))
k=2*n
for row in range(1,n+1):
    for col in range(1,k):
        if col == (n+1)-row or col == (n-1)+row:
            print("*",end="")
        elif row == n:
            print("*",end="")
        else:
            print(" ",end="")
    
    print()
'''


#Second Approach
n=int(input("Enter number of rows"))

for row in range(1,n+1):

    for space in range(n-row):
        print(" ",end="")
    
    for col in range(2*row-1):
        if col == 0 or col == 2*row-2 or row == n:
            print("*",end="")
        else:
            print(" ",end="")
        # print("*",end="")

    print()

