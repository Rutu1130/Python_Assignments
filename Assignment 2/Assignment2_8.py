#Write a program which accept one number and display below pattern.

def Num(n):
    for i in range(n):
        j=1
        while j<=i+1:
            print(j,end="")
            j+=1
        print("\n")
x=(int(input("Enter the Number")))
Num(x)
