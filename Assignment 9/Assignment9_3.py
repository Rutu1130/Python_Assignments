import sys

def copy_file_contents(input_filename, output_filename):
    try:
        with open(input_filename, 'r') as input_file, open(output_filename, 'w') as output_file:
            content = input_file.read()
            output_file.write(content)
        print(f"Contents from '{input_filename}' copied to '{output_filename}'.")
    except FileNotFoundError:
        print(f"The file '{input_filename}' does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    if len(sys.argv) != 3:
        print("Usage: python copy_file.py <input_filename> <output_filename>")
        return
    
    input_filename = sys.argv[1]
    output_filename = sys.argv[2]
    
    copy_file_contents(input_filename, output_filename)

if __name__ == "__main__":
    main()





