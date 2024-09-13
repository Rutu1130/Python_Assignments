import psutil
import sys

def get_process_info(process_name):
    process_info = []

    for process in psutil.process_iter(attrs=['pid', 'name', 'username']):
        try:
            pid = process.info['pid']
            name = process.info['name']
            username = process.info['username']
            
            if name.lower() == process_name.lower():
                process_info.append(f"PID: {pid}, Name: {name}, Username: {username}")
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass

    return process_info

def main():
    try:
        if len(sys.argv) != 2:
            print("Usage: python ProcInfo.py <process_name>")
            return

        process_name = sys.argv[1]
        process_info = get_process_info(process_name)

        if process_info:
            for info in process_info:
                print(info)
        else:
            print(f"No running process with the name '{process_name}' found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
