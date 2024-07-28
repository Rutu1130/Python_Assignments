#Write a program which accept one number and display below pattern.


def Pattern(x):
    for i in range(x):
        for j in range(x):
            print("*",end=" ")
        print("\n")


x=(int(input("Enter the Number")))
Pattern(x)