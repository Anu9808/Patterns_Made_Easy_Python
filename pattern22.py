#input = 5
#output
'''
Point1

* * * * * * * * * 
  *           *
    *       *
      *   *
        *
      *   *
    *       *
  *           *
* * * * * * * * *

point2

* * * * * * * * * 
* *           * *
*   *       *   *
*     *   *     *
*       *       *
*     *   *     *
*   *       *   *
* *           * *
* * * * * * * * *

'''

n=int(input("Enter number of rows "))
k=2*n
for row in range(1,k):
    for col in range(1,k):
        # point 1
        if row == 1 or row == k-1 or col == row or col == k-row:
        # point 2
        # if row == 1 or row == k-1 or col == row or col == k-row \
        #     or col == 1 or col == k-1 :
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
