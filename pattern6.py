#input = 5
#output
'''
    *
   * *
  * * *
 * * * *
* * * * *

'''

n=int(input("Enter number of rows"))
for row in range(n):
    for space in range(n-row-1):
        print(" ",end="")

    for col in range(2*row+1):
        if col %2 !=0:
            print(" ",end="")
        else: 
            print("*",end="")
    
    print()