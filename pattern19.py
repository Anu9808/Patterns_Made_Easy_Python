# input = 5
#output

'''

        * * * * * 
      *       *
    *       *
  *       *
* * * * *

'''
n=int(input("Enter number of rows "))

for row in range(1,n+1):

    for space in range(1,n-row+1):
        print(" ",end=" ")
    for col in range(1,n+1):
        if col == 1 or col == n or row == 1 or row == n:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()