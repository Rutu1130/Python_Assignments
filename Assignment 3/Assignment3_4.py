def main():
    n = int(input("Enter the number of elements: "))
    Data = []

    for i in range(n):
        num = float(input(f"Enter element {i+1}: "))
        Data.append(num)

    target_number = float(input("Enter the number to find its frequency: "))
    frequency = Data.count(target_number)
    
    print(f"The frequency of {target_number} in the list is:", frequency)

if __name__ == "__main__":
    main()