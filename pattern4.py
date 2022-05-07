'''

     *
    **
   ***
  ****
 *****

'''
n=int(input("Enter number of rows"))

for row in range(n):

    for space in range(n-row):
        print(" ",end="")

    for col in range(row+1):
        print("*",end="")
    
    print()