def display_file_contents(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
            print(f"Contents of the file '{filename}':\n")
            print(content)
    except FileNotFoundError:
        print(f"The file '{filename}' does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    filename = input("Enter the name of the file to open and display its contents: ")
    display_file_contents(filename)

if __name__ == "__main__":
    main()