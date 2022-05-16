#input=5
#output
'''
By using line 45
Without Gap

*********
 *******
  *****
   ***
    *
   ***
  *****
 *******
*********

By line 48
With Gap

* * * * *
 * * * *
  * * *
   * *
    *
   * *
  * * *
 * * * *
* * * * *

'''

n=int(input("Enter number of rows"))
k=2*n

for row in range(1,k+1):

    c= row if row <=n else k-row

    for space in range(c-1):
        print(" ",end="")

    for col in range(2*(n-c)+1):

        #Without gap
        print("*",end="")

        #with gap
        #print("*",end="") if col %2==0 else print(" ",end="")
        
    print()