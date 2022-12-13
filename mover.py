#! /usr/bin/python3

# Made by Alex Marquardt with help from Grant Duchars
# V-2.1 11/18/2022

# imports
import paramiko
import os
import getpass
import logging
import errno
from pathlib import Path

# Console text formatting
YELLOWTXT = "\033[33m"
GREENTXT = "\033[32m"
BLUETXT = "\033[036m"
RESETTXT = "\033[39m"

# Files moved counter
counter = 0

def main():
    start = Path(os.getcwd())
    if (start.name != 'Python-File-Mover'):
        inputs_path = os.getcwd() + "/Python-File-Mover/inputs.txt"
    else:
        inputs_path = os.getcwd() + "/inputs.txt"
    try:
        inputs = open(str(inputs_path), 'r')

        # auto inputs from inputs.txt
        line = inputs.readline()
        address = line.strip()
        line = inputs.readline()
        user = line.strip()
        line = inputs.readline()
        secret = line.strip()
        line = inputs.readline()
        src = line.strip()
        line = inputs.readline()
        dest = line.strip()

    except FileNotFoundError as e:
        if e.errno == errno.EACCES:
            print("file exists, but isn't readable")
        elif e.errno == errno.ENOENT:
            print("files isn't readable because it isn't there")
    

    inputs.close()

    # Gathering ssh information
    # address = input(f"{YELLOWTXT}Please input the server url:{RESETTXT}")
    # user = input(f"{YELLOWTXT}Please input the username:{RESETTXT}")
    # secret = getpass.getpass(f"{YELLOWTXT}Please input the password:{RESETTXT}")

    # Gathering path and destionation
    # src = input(f"{YELLOWTXT}Where is the Source:{RESETTXT}")
    # dest = input(f"{YELLOWTXT}Where is this going to:{RESETTXT}")

    # Setting up log file
    log = Path()
    log = log.resolve()
    log = f"{log}/log.txt"
    fp = open(log, 'a')
    logging.basicConfig(filename=log, level=logging.DEBUG, format= "%(asctime)s %(message)s", filemode='a')

    # Accessing ssh
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh_client.connect(address, username=user, password=secret)
    global ftp_client 
    ftp_client = ssh_client.open_sftp()

    ftp_client.chdir(dest)

    # Notify moving start
    print(f"{GREENTXT}Start!{RESETTXT}")

    # Run through and move filetree to nas
    parent = Path(src)
    findAndMove(parent, dest)

    # Finishing up
    print (f"{counter} file(s) were moved.")
    print(f"{GREENTXT}Done!{RESETTXT}")
    
    # Closing ftp and ssh
    ftp_client.close()
    ssh_client.close()
    fp.write("\n Done! \n\n")
    fp.close()

def findAndMove(parent, remotePath):
    for child in parent.iterdir():
        if (child.is_dir() == False):
            print(f"{BLUETXT}{child}{RESETTXT}")
            # Move file to nas
            ftp_client.put(f"{child}",f"{remotePath}/{child.name}")
            logging.info(f"{child} --> {remotePath}/{child.name}")
            # Increment files moved counter
            global counter
            counter = counter + 1
            # Remove file from original
            os.remove(child)
        else:
            try:
                ftp_client.mkdir(f"{remotePath}/{child.name}")
            except IOError:
                logging.info(f"{child.name} alread exists")
            findAndMove(child, f"{remotePath}/{child.name}")
            child.rmdir()

if __name__ == "__main__":
    main()