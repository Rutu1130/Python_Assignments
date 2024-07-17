#Write a program which contains one function named as Add() which accept two
#numbers from user and return addition of that two numbers  

#INPUT :11  5               OUTPUT : 16


def Add(No1, No2):

    Ans = 0

    Ans = No1 + No2 

    return Ans

def main():
    No1 = int(input("Enter the number :"))
    No2 = int(input("Enter the number :"))

    Ret = Add(No1, No2)

    print("Addtion is :",Ret)

if __name__ == "__main__":
    main()
