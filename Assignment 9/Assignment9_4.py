import sys

def compare_files(file1, file2):
    try:
        with open(file1, 'r') as f1, open(file2, 'r') as f2:
            content1 = f1.read()
            content2 = f2.read()

            if content1 == content2:
                return "success"
            else:
                return "failure"
    except FileNotFoundError:
        return "One or both files do not exist."
    except Exception as e:
        return f"An error occurred: {e}"

def main():
    if len(sys.argv) != 3:
        print("Usage: python compare_files.py <file1> <file2>")
        return
    
    file1 = sys.argv[1]
    file2 = sys.argv[2]
    
    result = compare_files(file1, file2)
    print(result)

if __name__ == "__main__":
    main()