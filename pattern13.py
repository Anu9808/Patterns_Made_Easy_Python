'''
*        *
**      **
***    ***
****  ****
**********
****  ****
***    ***
**      **
*        *

'''

n=int(input("Enter number of rows"))
k=2*n

for row in range(1,k+1):
    c = row if row < n else k-row
    for col in range(c):
        print("*",end="")

    for space in range(k-(2*c)):
        print(" ",end="")

    for col in range(c):
        print("*",end="")
    
    print()