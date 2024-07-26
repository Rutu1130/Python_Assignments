#write a program which accept name from user and display length of its name
# Input : Marvellous   Output : 10  

def Display(name):
    print("Length of the name is:", len(name))

def main():
    name = input("Enter your name: ")
    Display(name)

if __name__ == "__main__":
    main()
