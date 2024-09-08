
import os
import hashlib
import sys

def calculate_checksum(file_path, block_size=65536):
    """Calculate the checksum of a file."""
    hasher = hashlib.md5()
    with open(file_path, 'rb') as file:
        while True:
            data = file.read(block_size)
            if not data:
                break
            hasher.update(data)
    return hasher.hexdigest()

def find_duplicate_files(directory):
    """Find and return a dictionary of duplicate files in the directory."""
    file_checksums = {}
    duplicate_files = {}

    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            checksum = calculate_checksum(file_path)

            if checksum in file_checksums:
                duplicate_files[checksum] = duplicate_files.get(checksum, []) + [file_path]
            else:
                file_checksums[checksum] = file_path

    return duplicate_files

def remove_duplicates(duplicate_files):
    """Remove duplicate files and write their names to a log file."""
    with open("Log.txt", "w") as log_file:
        for checksum, file_list in duplicate_files.items():
            if len(file_list) > 1:
                log_file.write(f"Duplicates for checksum {checksum}:\n")
                for file_path in file_list:
                    log_file.write(f"  {file_path}\n")
                    os.remove(file_path)

def main(directory):
    try:
        if not os.path.exists(directory):
            print(f"The directory '{directory}' does not exist.")
            return

        if not os.path.isdir(directory):
            print(f"'{directory}' is not a directory.")
            return

        duplicate_files = find_duplicate_files(directory)

        if not duplicate_files:
            print("No duplicate files found.")
        else:
            remove_duplicates(duplicate_files)
            print("Duplicate files removed. Check 'Log.txt' for details.")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python DirectoryDuplicateRemoval.py <directory>")
    else:
        directory = sys.argv[1]
        main(directory)
