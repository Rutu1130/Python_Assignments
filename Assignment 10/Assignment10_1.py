import os
import sys

def list_files_with_extension(directory, extension):
    try:
        # Check if the directory exists
        if not os.path.isdir(directory):
            return "Directory does not exist."

        # List all files in the directory with the specified extension
        files_with_extension = [file for file in os.listdir(directory) if file.endswith(extension)]
        
        if not files_with_extension:
            return f"No files with '{extension}' extension found in '{directory}'."

        return files_with_extension
    except Exception as e:
        return f"An error occurred: {e}"

def main():
    if len(sys.argv) != 3:
        print("Usage: python DirectoryFileSearch.py <directory> <extension>")
        return

    directory = sys.argv[1]
    extension = sys.argv[2]

    result = list_files_with_extension(directory, extension)

    if isinstance(result, list):
        print(f"Files with '{extension}' extension in '{directory}':")
        for file in result:
            print(file)
    else:
        print(result)

if __name__ == "__main__":
    main()
