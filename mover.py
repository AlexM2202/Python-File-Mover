# Alex Marquardt with help from Grant Duchars

# imports
import paramiko
import os
import shutil
import getpass
from tqdm import tqdm

dirs = []

# Console text formatting
YELLOWTXT = '\033[33m'
GREENTXT = '\033[32m'
BLUETXT = '\033[036m'
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
print (GREENTXT + "start!" + RESETTXT)
# Loop for detecting and moving files
for dir in os.listdir():
    if dir == "mover.py" or dir == ".git" or dir == "generator.py" or dir == "README.md":
        continue
    if os.path.isdir(dir):
        dirs.append(dir)

size = len(dir)

for dir in tqdm(dirs):
    currentDir = src + "/" + dir
    # print(currentDir)
    os.chdir(currentDir)
    ftp_client.mkdir(dir)
    for file in os.listdir(currentDir):
        # print(dest + "/" + dir)
        # print(file)
        # print(currentDir)
        # print(YELLOWTXT + currentDir + "/" + file + RESETTXT + " --> " + BLUETXT + dest + "/" + dir + "/"+ file + RESETTXT)
        ftp_client.put(currentDir + "/" + file, dest + "/" + dir + "/" + file)
    shutil.rmtree(currentDir)
        
        
# Closing ftp and ssh
ftp_client.close()
ssh_client.close()