# Write a program which accept number from user and print that number of " * " on screen
# Input : 5         Output :  *   *   *   *   *    


def Display(Num):
    for i in range(Num):
        print("*",end=" ")

def main():

    No = int(input("Enter the number : "))

    Display(No)

if __name__ == "__main__":
    main()

