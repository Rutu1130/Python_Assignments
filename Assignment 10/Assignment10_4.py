import os
import shutil
import sys

def copy_files_with_extension(source_directory, destination_directory, extension):
    try:
        
        if not os.path.isdir(source_directory):
            return f"Source directory '{source_directory}' does not exist."

       
        if not os.path.exists(destination_directory):
            os.makedirs(destination_directory)
            
        for filename in os.listdir(source_directory):
            if filename.endswith(extension):
                source_file = os.path.join(source_directory, filename)
                destination_file = os.path.join(destination_directory, filename)
                shutil.copy2(source_file, destination_file)

        return f"All files with '{extension}' extension from '{source_directory}' copied to '{destination_directory}'."
    except Exception as e:
        return f"An error occurred: {e}"

def main():
    if len(sys.argv) != 4:
        print("Usage: python DirectoryCopyExt.py <source_directory> <destination_directory> <extension>")
        return

    source_directory = sys.argv[1]
    destination_directory = sys.argv[2]
    extension = sys.argv[3]

    result = copy_files_with_extension(source_directory, destination_directory, extension)

    print(result)

if __name__ == "__main__":
    main()
