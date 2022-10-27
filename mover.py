# Alex Marquardt with help from Grant Duchars

# imports
import paramiko
import os
import getpass
import logging
from pathlib import Path
# from tqdm import tqdm

# Console text formatting
YELLOWTXT = '\033[33m'
GREENTXT = '\033[32m'
BLUETXT = '\033[036m'
RESETTXT = '\033[39m'

# Gathering ssh information
address = input(YELLOWTXT + "Please input the server url:" + RESETTXT)
user = input(YELLOWTXT + "Please input the username:" + RESETTXT)
secret = getpass.getpass(YELLOWTXT + "Please input the password:" + RESETTXT)

#setting up log file
log = Path()
log = log.resolve()
log = str(log) + "/log.txt"
fp = open(log, 'a')
logging.basicConfig(filename=log, level=logging.DEBUG, format= "%(asctime)s %(message)s", filemode='a')

# Accessing ssh
ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_client.connect(address, username=user, password=secret)
ftp_client = ssh_client.open_sftp()

# Gathering path and destionation
src = input(YELLOWTXT + "Where is the Source:" + RESETTXT)
dest = input(YELLOWTXT + "Where is this going to:" + RESETTXT)

ftp_client.chdir(dest)

print (GREENTXT + "start!" + RESETTXT)

p = Path(src)
for year in p.iterdir():
    if (year.is_dir() == False):
        continue
    ftp_client.mkdir(year.name)
    for month in year.iterdir():
        ftp_client.mkdir(year.name + "/" + month.name)
        for day in month.iterdir():
            ftp_client.mkdir(year.name +"/" + month.name + "/" + day.name)
            for file in day.iterdir():
                ftp_client.put(str(day) + "/" + file.name, dest + "/" + year.name + "/" + month.name + "/" + day.name + "/" + file.name)
                logging.info(str(day) + "/" + file.name + " --> " + dest + "/" + year.name + "/" + month.name + "/" + day.name + "/" + file.name)
                os.remove(file)
            day.rmdir()
        month.rmdir()
    year.rmdir()
            
# Closing ftp and ssh

ftp_client.close()
ssh_client.close()
fp.write("\n Done! \n\n")
fp.close()
