# Alex Marquardt with help from Grant Duchars
# This should just gather the ssh info and try to connnect
# inports
import paramiko
import os
import shutil
import getpass

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
    if dir == ".git":
        continue
    if os.path.isdir(dir):
        currentDir = src + "/" + dir
        #! ERRORS HERE WHEN TRYING TO MAKE A DIRECTORY ON THE CLIENT
        ftp_client.mkdir(dir)
        for file in os.listdir(currentDir):
            print(currentDir + "/" + file)
            print(dest + dir)
            ftp_client.put(currentDir + "/" + file, dest + dir)
        # final = shutil.move(src + "/" + file, dest)
        # shutil.rmtree(src + "/" + file)
        # print("Destination path:", final)

# Closing ftp and ssh
ftp_client.close()
ssh_client.close()

# I hope it works
