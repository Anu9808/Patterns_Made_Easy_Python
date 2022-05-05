'''

*****
 ****
  ***
   **
    *

'''

n = int(input("Enter numbe rof rows"))

for row in range(n+1):

    for space in range(row):
        print(" ",end="")

    for col in range(row,n):
        print("*",end="")

    
    print()