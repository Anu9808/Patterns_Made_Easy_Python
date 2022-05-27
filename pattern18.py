#Imput=7
#Output
'''

Enter number of rows 5
Choose from 1 to 4, other integer for exit
Enter your choice 1
You choose Left Side Triangle
*
* *       
*   *     
*     *   
* * * * * 
Choose from 1 to 4, other integer for exit
Enter your choice 2
You choose Left Side Inverted Triangle
* * * * *
*     *
*   *
* *
*
Choose from 1 to 4, other integer for exit
Enter your choice 3
You choose Right Side Triangle
        *
      * *
    *   *
  *     *
* * * * *
Choose from 1 to 4, other integer for exit
Enter your choice 4
You choose Right Side Inverted Triangle
* * * * *
  *     *
    *   *
      * *
        *
Choose from 1 to 4, other integer for exit
Enter your choice t
Please Enter Integer value
Choose from 1 to 4, other integer for exit
Enter your choice 7
exit


'''

n=int(input("Enter number of rows "))
while(True):

    choice = 0
    print("Choose from 1 to 4, other integer for exit")

    try:
        choice = int(input("Enter your choice "))

    except ValueError:
        print("Please Enter Integer value")
        continue

    except :
        print("Something happend!")

    if choice == 1:
        print("You choose Left Side Triangle")

        for row in range(1,n+1):
            for col in range(1,n+1):
                if col == row or col == 1 or row == n:
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()


    elif choice == 2:
        print("You choose Left Side Inverted Triangle")

        for row in range(1,n+1):
            for col in range(1,n+1):
                if col == n-row+1 or col == 1 or row == 1:
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()

    elif choice == 3:
        print("You choose Right Side Triangle")

        for row in range(1,n+1):
            for space in range(1, n-row+1):
                print(" ",end=" ")
            for col in range(1,row+1):
                if col == row or col == 1 or row == n :
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()

    elif choice == 4:
        print("You choose Right Side Inverted Triangle")

        for row in range(1, n+1):
            for space in range(1,row):
                print(" ",end=" ")
            for col in range(1,n-row+2):
                if row == 1 or col == 1 or col == n-row+1:
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()

    else:
        print("exit")
        break

