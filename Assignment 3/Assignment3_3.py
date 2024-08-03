def main():
    n = int(input("Enter the number of elements: "))
    numbers = []

    for i in range(n):
        num = float(input(f"Enter element {i+1}: "))
        numbers.append(num)

    min_number = min(numbers)
    print("The maximum number is:", min_number)

if __name__ == "__main__":
    main()