import psutil

def get_process_info():
    process_info = []
    
    for process in psutil.process_iter(attrs=['pid', 'name', 'username']):
        try:
            pid = process.info['pid']
            name = process.info['name']
            username = process.info['username']
            process_info.append(f"PID: {pid}, Name: {name}, Username: {username}")
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    
    return process_info

def main():
    try:
        process_info = get_process_info()
        if process_info:
            for info in process_info:
                print(info)
        else:
            print("No running processes found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
