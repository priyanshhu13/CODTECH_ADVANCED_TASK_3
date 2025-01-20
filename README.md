# CODTECH_ADVANCED_TASK_3
#  Pentest Toolkit PS
## Personal Information
Name: Priyanshu Vijay Singh
Company: CODTECH IT SOLUTIONS
ID•. CT08FFC
Domain: Cyber Security
Duration: 20 dec 2024 to 20 jan 2025
Mentor: Neela Santhosh Kumar
## Overview
Pentest Toolkit PS is a Python-based tool designed for ethical hacking and penetration testing. It provides functionalities for:

- **Port Scanning**: Identify open ports on a target system and perform basic banner grabbing.
- **SSH Brute Forcing**: Attempt to log in to SSH servers using username and password combinations.

This tool is developed with ease of use in mind and incorporates threading for efficient operations.

## Features
1. **Port Scanning**
   - Identifies open ports within a given range on a target IP or Hostname.
   - Performs basic banner grabbing for open ports.

2. **SSH Brute Force**
   - Attempts to log in to an SSH server using a list of usernames and passwords.
   - Supports loading credentials from files or manual input.

## Installation

### 1. Clone the Repository
```bash
git clone https://github.com/hipremsoni/CODTECH_ADVANCED_TASK_3.git
cd CODTECH_ADVANCED_TASK_3
```

### 2. Install Requirements Packages 
```bash
pip3 install -r requirements.txt 
```

### 3. Run the Script
```bash
python toolkitps.py
```
## Requirements
- Python 3.x
- Libraries:
  - `socket`
  - `logging`
  - `concurrent.futures`
  - `paramiko`
  - `pyfiglet`
  - `colorama`

### 3. Operations

#### Port Scanning
1. Select option `1` for Port Scanning.
2. Enter the target IP address.
3. Specify the range of ports (start and end).
4. Provide a timeout value in seconds.
5. View results with open ports and banners (if available).

#### SSH Brute Force
1. Select option `2` for SSH Brute Force.
2. Enter the target IP address.
3. Choose to provide credentials via a file or manually.
4. If using a file, enter the file paths for usernames and passwords.
5. If entering manually, input comma-separated usernames and passwords.
6. View the results of the brute force attempts.

### Screenshot 
![image](https://github.com/user-attachments/assets/954e3125-d7c3-49b4-a7ce-ed5979a7d41b)
![image](https://github.com/user-attachments/assets/c904efe1-a151-4ba2-a033-cb6da0a0205b)
![image](https://github.com/user-attachments/assets/397eec9b-adbf-4136-a03d-59fe35d818ef)



### Example Outputs
```
 ____  _____ _   _ _____ _____ ____ _____
|  _ \| ____| \ | |_   _| ____/ ___|_   _|
| |_) |  _| |  \| | | | |  _| \___ \ | |
|  __/| |___| |\  | | | | |___ ___) || |
|_|   |_____|_| \_| |_| |_____|____/ |_|

 _____ ___   ___  _     _  _____ _____   ____  ____
|_   _/ _ \ / _ \| |   | |/ /_ _|_   _| |  _ \/ ___|
  | || | | | | | | |   | ' / | |  | |   | |_) \___ \
  | || |_| | |_| | |___| . \ | |  | |   |  __/ ___) |
  |_| \___/ \___/|_____|_|\_\___| |_|   |_|   |____/


Created by Premkumar Soni

Select operation:
1. Port Scan
2. SSH Brute Force
Enter choice (1/2): 1
Enter the target IP address or hostname ( ex :testphp.vulnweb.com): 192.168.0.34
Enter the start port: 1
Enter the end port: 1024
Enter the timeout for each port scan (in seconds): 2
Port 25 is open on 192.168.0.34
Port 53 is open on 192.168.0.34
Port 21 is open on 192.168.0.34Port 23 is open on 192.168.0.34

Port 22 is open on 192.168.0.34
Port 80 is open on 192.168.0.34
Banner for port 21 on 192.168.0.34: 220 (vsFTPd 2.3.4)
Banner for port 80 on 192.168.0.34: HTTP/1.1 200 OK
Date: Wed, 15 Jan 2025 06:31:13 GMT
Server: Apache/2.2.8 (Ubuntu) DAV/2
X-Powered-By: PHP/5.2.4-2ubuntu5.10
Content-Type: text/html
Banner for port 22 on 192.168.0.34: SSH-2.0-OpenSSH_4.7p1 Debian-8ubuntu1
Error grabbing banner for port 23 on 192.168.0.34: 'utf-8' codec can't decode byte 0xff in position 0: invalid start byte
Banner for port 25 on 192.168.0.34: 220 metasploitable.localdomain ESMTP Postfix (Ubuntu)
Port 111 is open on 192.168.0.34
Port 139 is open on 192.168.0.34
Timeout while grabbing banner for port 53 on 192.168.0.34
Banner for port 111 on 192.168.0.34: 
Timeout while grabbing banner for port 139 on 192.168.0.34
Port 445 is open on 192.168.0.34
Port 513 is open on 192.168.0.34
Port 512 is open on 192.168.0.34Port 514 is open on 192.168.0.34

Timeout while grabbing banner for port 445 on 192.168.0.34
Error grabbing banner for port 514 on 192.168.0.34: [WinError 10054] An existing connection was forcibly closed by the remote host
Error grabbing banner for port 513 on 192.168.0.34: [WinError 10054] An existing connection was forcibly closed by the remote host
Banner for port 512 on 192.168.0.34: Where are you?
Do you want to perform SSH brute-forcing on port 22 after port scan? (yes/no): yes
Do you want to use a file or enter credentials manually? (file/manual): file
Enter the path to the username file: u:\CODTECH INTERNSHIP\CODTECH ADV TASK\TASK 3\file.txt    
Enter the path to the password file: u:\CODTECH INTERNSHIP\CODTECH ADV TASK\TASK 3\file.txt
Attempting SSH login with username: hi and password: hi on 192.168.0.34:22
2025-01-15 12:02:23,433 - INFO - Connected (version 2.0, client OpenSSH_4.7p1)
2025-01-15 12:02:25,606 - INFO - Authentication (password) failed.
Failed SSH login with username: hi and password: hi on 192.168.0.34:22
Attempting SSH login with username: hi and password: admin on 192.168.0.34:22
2025-01-15 12:02:25,623 - INFO - Connected (version 2.0, client OpenSSH_4.7p1)
2025-01-15 12:02:28,016 - INFO - Authentication (password) failed.
Failed SSH login with username: hi and password: admin on 192.168.0.34:22
Attempting SSH login with username: hi and password: msfadmin on 192.168.0.34:22
2025-01-15 12:02:28,033 - INFO - Connected (version 2.0, client OpenSSH_4.7p1)
2025-01-15 12:02:30,057 - INFO - Authentication (password) failed.
Failed SSH login with username: hi and password: msfadmin on 192.168.0.34:22
Attempting SSH login with username: hi and password: password on 192.168.0.34:22
2025-01-15 12:02:30,071 - INFO - Connected (version 2.0, client OpenSSH_4.7p1)
2025-01-15 12:02:32,567 - INFO - Authentication (password) failed.
Failed SSH login with username: hi and password: password on 192.168.0.34:22
Attempting SSH login with username: hi and password: user on 192.168.0.34:22
2025-01-15 12:02:32,581 - INFO - Connected (version 2.0, client OpenSSH_4.7p1)
2025-01-15 12:02:34,887 - INFO - Authentication (password) failed.
Failed SSH login with username: hi and password: user on 192.168.0.34:22
Attempting SSH login with username: admin and password: hi on 192.168.0.34:22
2025-01-15 12:02:34,904 - INFO - Connected (version 2.0, client OpenSSH_4.7p1)
2025-01-15 12:02:36,886 - INFO - Authentication (password) failed.
Failed SSH login with username: admin and password: hi on 192.168.0.34:22
Attempting SSH login with username: admin and password: admin on 192.168.0.34:22
2025-01-15 12:02:36,902 - INFO - Connected (version 2.0, client OpenSSH_4.7p1)
2025-01-15 12:02:39,507 - INFO - Authentication (password) failed.
Failed SSH login with username: admin and password: admin on 192.168.0.34:22
Attempting SSH login with username: admin and password: msfadmin on 192.168.0.34:22
2025-01-15 12:02:39,525 - INFO - Connected (version 2.0, client OpenSSH_4.7p1)
2025-01-15 12:02:41,157 - INFO - Authentication (password) failed.
Failed SSH login with username: admin and password: msfadmin on 192.168.0.34:22
Attempting SSH login with username: admin and password: password on 192.168.0.34:22
2025-01-15 12:02:41,174 - INFO - Connected (version 2.0, client OpenSSH_4.7p1)
2025-01-15 12:02:43,416 - INFO - Authentication (password) failed.
Failed SSH login with username: admin and password: password on 192.168.0.34:22
Attempting SSH login with username: admin and password: user on 192.168.0.34:22
2025-01-15 12:02:43,429 - INFO - Connected (version 2.0, client OpenSSH_4.7p1)
2025-01-15 12:02:46,327 - INFO - Authentication (password) failed.
Failed SSH login with username: admin and password: user on 192.168.0.34:22
Attempting SSH login with username: msfadmin and password: hi on 192.168.0.34:22
2025-01-15 12:02:46,345 - INFO - Connected (version 2.0, client OpenSSH_4.7p1)
2025-01-15 12:02:47,727 - INFO - Authentication (password) failed.
Failed SSH login with username: msfadmin and password: hi on 192.168.0.34:22
Attempting SSH login with username: msfadmin and password: admin on 192.168.0.34:22
2025-01-15 12:02:47,745 - INFO - Connected (version 2.0, client OpenSSH_4.7p1)
2025-01-15 12:02:50,196 - INFO - Authentication (password) failed.
Failed SSH login with username: msfadmin and password: admin on 192.168.0.34:22
Attempting SSH login with username: msfadmin and password: msfadmin on 192.168.0.34:22
2025-01-15 12:02:50,212 - INFO - Connected (version 2.0, client OpenSSH_4.7p1)
2025-01-15 12:02:50,342 - INFO - Authentication (password) successful!
Successful SSH login with username: msfadmin and password: msfadmin on 192.168.0.34:22

```
## Code Structure
- `display_logo()`: Displays the tool's logo.
- `scan_port(ip, port, timeout)`: Scans a single port and attempts banner grabbing.
- `port_scan(ip, start_port, end_port, timeout)`: Scans multiple ports concurrently.
- `load_credentials_from_file(filepath)`: Loads usernames or passwords from a file.
- `brute_force_ssh(ip, username_list, password_list, timeout)`: Performs SSH brute force using the provided credentials.

## Notes
- Use this tool responsibly and only on systems you are authorized to test.
- Ensure compliance with applicable laws and ethical guidelines.
