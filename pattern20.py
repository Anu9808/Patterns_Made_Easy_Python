'''

Input = 5
output

    *
   * *
  *   *
 *     *
*       *
 *     *
  *   *
   * *
    *

'''

n = int(input("Enter number of rows"))
k = 2*n
for row in range(1,k):
    c= row if row<=n else k-row
    for space in range(n-c):
        print(" ",end="")

    for col in range(2*c-1):
        print("*",end="") if col == 0 or col == 2 *c-2 else print(" ",end="")
    print()
    