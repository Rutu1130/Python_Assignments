# Write a program which contains one funcion that accept one number from
#user and returns True is divisible ny 5 otherwise return False
# Input :  8           Output : False
# Input :  25           Output : True




def Display(No):

    if (No % 5 == 0 ):
        return True
    
    else:
        return False
    
def main():
    No = int(input("Enter the Number : "))

    Ret = Display(No)
    if (Ret == True):
        print("True")

    else:
        print("False")
    
if __name__ == "__main__":
    main()
