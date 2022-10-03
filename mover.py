# Alex Marquardt with help from Grant Duchars

# imports
import paramiko
import os
import shutil
import getpass


dirs = []

# Console text formatting
YELLOWTXT = '\033[33m'
RESETTXT = '\033[39m'

# Gathering ssh information
address = input(YELLOWTXT + "Please input the server url:" + RESETTXT)
user = input(YELLOWTXT + "Please input the username:" + RESETTXT)
secret = getpass.getpass(YELLOWTXT + "Please input the password:" + RESETTXT)

# Accessing ssh
ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_client.connect(address, username=user, password=secret)
ftp_client = ssh_client.open_sftp()

# Gathering path and destionation
src = os.fspath(os.getcwd())
dest = input(YELLOWTXT + "Where is this going to:" + RESETTXT)
ftp_client.chdir(dest)

# Loop for detecting and moving files
for dir in os.listdir():
    if dir == ".git" or dir == "mover.py":
        continue
    if os.path.isdir(dir):
        dirs.append(dir)

for dir in dirs:
    currentDir = src + "/" + dir
    print(currentDir)
    os.chdir(currentDir)
    ftp_client.mkdir(dir)
    for file in os.listdir(currentDir):
        
        print(dest + "/" + dir)
        print(file)
        # print(currentDir)
        # ftp_client.chdir(currentDir)
        ftp_client.put(currentDir + "/" + file, dest + "/" + dir + "/" + file)
        shutil.rmtree(currentDir + "/")

# Closing ftp and ssh
ftp_client.close()
ssh_client.close()