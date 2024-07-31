#Write a program which accept one number and display below pattern.


def number(num):
    for i in range(num):
        j=1
        while j<=num:
            print(j,end=" ")
            j+=1
        print("\n")
n=(int(input("Enter the Number")))
number(n)