import os
import socket
import sys
import subprocess

def get_user():
    return os.getenv('REPL_OWNER', 'Unknown')

def get_hostname():
    return socket.gethostname()

def get_project_folder():
    return os.getcwd()

def get_project_name():
    return input("Enter the Replit project name: ")

def get_ssh_sftp_details(project_name):
    if project_name == "PythonProjectInfoPrinter":
        user = "f337ac3a-fd45-46a6-9868-0e094366997e"
        host = "f337ac3a-fd45-46a6-9868-0e094366997e-00-3oo6dq7zmtrws.picard.replit.dev"
        return user, host
    else:
        return "Unknown", "Unknown"

def save_output_to_file(output):
    filename = input("Enter the filename to save the output (e.g., output.txt): ")
    with open(filename, 'w') as f:
        f.write(output)
    print(f"Output saved to {filename}")

def main():
    project_name = get_project_name()
    user, host = get_ssh_sftp_details(project_name)
    hostname = get_hostname()
    project_folder = get_project_folder()
    port = 22
    key_location = "~/.ssh/replit"

    output = "System and Project Information:\n"
    output += "=" * 30 + "\n"
    output += f"Project Name:    {project_name}\n"
    output += f"User:            {user}\n"
    output += f"Host:            {host}\n"
    output += f"SSH Connection:  ssh {user}@{host}\n"
    output += f"Hostname:        {hostname}\n"
    output += f"Project Folder:  {project_folder}\n"
    output += f"Port:            {port}\n"
    output += f"Key Location:    {key_location}\n"

    print(output)

    save_option = input("Do you want to save the output to a file? (y/n): ").lower()
    if save_option == 'y':
        save_output_to_file(output)

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"An error occurred: {e}", file=sys.stderr)
        sys.exit(1)
