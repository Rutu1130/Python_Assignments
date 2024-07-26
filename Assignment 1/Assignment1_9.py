# Write a program which display first 10 even numbers on screen
# Output : 2  4  6  8  10  12  14  16  18  20

def Display():
    Num = 2
    iCnt = 0
    print("First 10 even numbers are:")
    while iCnt < 10:
        if Num % 2 == 0:
            iCnt += 1
            print(Num, end=" ")
        Num += 1
    print()  # For a new line after the output

def main():
    Display()

if __name__ == "__main__":
    main()


