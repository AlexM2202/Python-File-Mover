#Alex Marquardt with help from Grand Duchars

#inports
import paramiko
import os
import shutil

#gathering ssh information
address = input("Please input the server url - ")
user = input("Please input the username - ")
secret = input("Please input the password - ")

#accessing ssh
ssh = paramiko.SSHClient()
ssh.connect(address, username=user, password=secret)

#gathering path and destionation
src = os.fspath(os.getcwd())
dest = input("Where is this going to - ")

#Loop for detecting and moving files
for file in os.listdir():
    # if file == "":
    #     continue
    if os.path.isdir(file):
        finial = shutil.move(src + "/" + file, dest)
        print("Destination path:", finial)

#closing ssh
ssh.close()

#i hope it works