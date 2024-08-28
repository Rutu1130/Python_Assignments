import os

def file_exists(filename):
    return os.path.isfile(filename)

def main():
    filename = input("Enter the file name to check if it exists: ")
    
    if file_exists(filename):
        print(f"The file '{filename}' exists in the current directory.")
    else:
        print(f"The file '{filename}' does not exist in the current directory.")

if __name__ == "__main__":
    main()