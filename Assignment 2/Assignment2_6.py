#Write a program which accept one number and display below pattern.
def pattern(x):
    for i in range(x):
        j=i+1
        while j<=x:
            print("*",end=" ")
            j+=1
        print("\n")    

x=(int(input("Enter the Number=")))

pattern(x)