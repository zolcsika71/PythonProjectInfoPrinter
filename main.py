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

def get_ssh_sftp_details():
    try:
        result = subprocess.run(['grep', '-i', 'ssh', '/etc/hosts'], capture_output=True, text=True)
        ssh_host = result.stdout.strip().split()[-1] if result.stdout else "Unknown"
        return ssh_host, ssh_host  # Assuming SFTP uses the same host as SSH
    except Exception:
        return "Unknown", "Unknown"

def main():
    user = get_user()
    hostname = get_hostname()
    project_name = "this project"
    project_folder = get_project_folder()
    ssh_host, sftp_host = get_ssh_sftp_details()
    port = 22
    key_location = "~/.ssh/replit"

    print("System and Project Information:")
    print("=" * 30)
    print(f"User:            {user}")
    print(f"Hostname:        {hostname}")
    print(f"Project Name:    {project_name}")
    print(f"Project Folder:  {project_folder}")
    print(f"SSH Host:        {ssh_host}")
    print(f"SFTP Host:       {sftp_host}")
    print(f"Port:            {port}")
    print(f"Key Location:    {key_location}")

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"An error occurred: {e}", file=sys.stderr)
        sys.exit(1)
