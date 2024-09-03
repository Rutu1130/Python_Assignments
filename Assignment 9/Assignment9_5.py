def count_string_frequency(filename, search_string):
    try:
        with open(filename, 'r') as file:
            content = file.read()
            frequency = content.count(search_string)
        return frequency
    except FileNotFoundError:
        return -1  # File not found
    except Exception as e:
        print(f"An error occurred: {e}")
        return -2  # Error occurred during file processing

def main():
    filename = input("Enter the name of the file: ")
    search_string = input("Enter the string to count: ")

    frequency = count_string_frequency(filename, search_string)

    if frequency == -1:
        print(f"The file '{filename}' does not exist.")
    elif frequency == -2:
        print("An error occurred during file processing.")
    else:
        print(f"The frequency of '{search_string}' in '{filename}' is {frequency}.")

if __name__ == "__main__":
    main()