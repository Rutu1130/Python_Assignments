#Write a program which contains one function named as ChkNum() which accept one
#parameter as number . If number is even thet it should display "Even Number" Otherwise 
#display "Odd Number " on console.

#INPUT :11  5               OUTPUT : Odd number
#                           OUTPUT : Even number


def ChkNum(No):

    if(No % 2 == 0):
        print("Even Number")

    else:
        print("Odd Number")

def main():
    No1 = int(input("Enter the number :"))

    ChkNum(No1)

if __name__ == "__main__":
    main()
