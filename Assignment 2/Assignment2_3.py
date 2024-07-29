#Write a program which accept number from user and return its factorial.
def Factorial(n):
          i=1
          while n>0:
                    i=i*n
                    n=n-1
          return i

def main():
        
    x=(int(input("Enter the number :")))
    Ret = Factorial(x)
    print("Factorial is : ",Ret)

if __name__ =="__main__":
        main()