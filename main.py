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

def main():
    project_name = get_project_name()
    user, host = get_ssh_sftp_details(project_name)
    hostname = get_hostname()
    project_folder = get_project_folder()
    port = 22
    key_location = "~/.ssh/replit"

    print("System and Project Information:")
    print("=" * 30)
    print(f"Project Name:    {project_name}")
    print(f"User:            {user}")
    print(f"Host:            {host}")
    print(f"SSH Connection:  ssh {user}@{host}")
    print(f"Hostname:        {hostname}")
    print(f"Project Folder:  {project_folder}")
    print(f"Port:            {port}")
    print(f"Key Location:    {key_location}")

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"An error occurred: {e}", file=sys.stderr)
        sys.exit(1)
