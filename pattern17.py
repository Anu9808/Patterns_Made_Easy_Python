'''
Input = 5
Output

*****
*   *
*   *
*   *
*****

'''

n=int(input("Enter number of rows"))

for row in range(1,n+1):
    for col in range(1,n+1):
        if col == 1 or row == 1 or col == n or row == n:
            print("*",end="")
        else:
            print(" ",end="")
    print()