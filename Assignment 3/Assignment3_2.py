def main():
    n = int(input("Enter the number of elements: "))
    numbers = []

    for i in range(n):
        num = float(input(f"Enter element {i+1}: "))
        numbers.append(num)

    max_number = max(numbers)
    print("The maximum number is:", max_number)

if __name__ == "__main__":
    main()