#input = 5
#output
'''
* * * * *
 * * * *
  * * *
   * *
    *

'''
n=int(input("Enter number of rows"))
for row in range(n):

    for space in range(row):
        print(" ",end="")
    
    for col in range(2*(n-row)-1):
        print("*",end="") if col%2==0 else print(" ",end="")

    print()