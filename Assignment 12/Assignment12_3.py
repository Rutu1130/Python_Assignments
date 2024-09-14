import psutil
import os
import sys

def get_process_info():
    process_info = []

    for process in psutil.process_iter(attrs=['pid', 'name', 'username']):
        try:
            pid = process.info['pid']
            name = process.info['name']
            username = process.info['username']
            process_info.append(f"Name: {name}, PID: {pid}, Username: {username}")
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass

    return process_info

def create_log_file(directory, process_info):
    log_filename = os.path.join(directory, "ProcessInfoLog.txt")
    with open(log_filename, "w") as log_file:
        for info in process_info:
            log_file.write(info + "\n")
    return log_filename

def main():
    try:
        if len(sys.argv) != 2:
            print("Usage: python ProcInfoLog.py <directory>")
            return

        directory = sys.argv[1]

        if not os.path.exists(directory):
            print(f"The directory '{directory}' does not exist.")
            return

        process_info = get_process_info()
        log_file = create_log_file(directory, process_info)

        print(f"Process information log file '{log_file}' created successfully in {directory}.")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
