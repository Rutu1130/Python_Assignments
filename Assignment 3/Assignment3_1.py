def main():
    n = int(input("Enter the number of elements: "))
    numbers = []

    for i in range(n):
        num = float(input(f"Enter element {i+1}: "))
        numbers.append(num)

    total = sum(numbers)
    print("The sum of all elements is:", total)

if __name__ == "__main__":
    main()