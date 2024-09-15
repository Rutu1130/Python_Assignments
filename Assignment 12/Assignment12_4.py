import psutil
import sys
import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication

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

def send_email(log_file, to_email):
    from_email = "your_email@gmail.com"  # Replace with your email address
    password = "your_password"  # Replace with your email password

    subject = "Process Information Log"

    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject

    text = "Please find the attached process information log file."
    msg.attach(MIMEText(text, 'plain'))

    with open(log_file, "rb") as attachment:
        part = MIMEApplication(attachment.read(), Name=os.path.basename(log_file))

    part['Content-Disposition'] = f'attachment; filename="{os.path.basename(log_file)}"'
    msg.attach(part)

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(from_email, password)
    server.sendmail(from_email, to_email, msg.as_string())
    server.quit()

def main():
    try:
        if len(sys.argv) != 3:
            print("Usage: python ProcInfoLog.py <directory> <email>")
            return

        directory = sys.argv[1]
        to_email = sys.argv[2]

        if not os.path.exists(directory):
            print(f"The directory '{directory}' does not exist.")
            return

        process_info = get_process_info()
        log_file = create_log_file(directory, process_info)
        send_email(log_file, to_email)

        print(f"Process information log file '{log_file}' created and sent to {to_email} successfully.")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
