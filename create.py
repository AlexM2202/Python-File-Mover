import os
import shutil
from tqdm import tqdm

GREENTXT = '\033[32m'
BLUETXT = '\033[036m'
x=1
dirs = []
src = os.fspath(os.getcwd())

answer = input("Are we adding(a) or removing(r) - ")
if answer == "a":
    num = input("How many files are we making? - ")
    num = int(num)
    while(x<=num):
        y = str(x)
        os.mkdir("file"+y)
        x = x+1
    for dir in os.listdir():
        if dir == ".git" or dir == "mover.py" or dir == "generator.py":
            continue
        if os.path.isdir(dir):
            dirs.append(dir)
    for dir in tqdm(dirs):
        currentDir = src + "/" + dir
        os.chdir(currentDir)
        fp = open(currentDir + "/file", 'w')
        fp.write('this is a test file')
        fp.close()
        # print(BLUETXT + "file created")

if answer == "r":
    for dir in os.listdir():
        if dir == ".git" or dir == "mover.py" or dir == "generator.py":
                continue
        if os.path.isdir(dir):
            dirs.append(dir)
    for dir in tqdm(dirs):
        currentDir = src + "/" + dir
        shutil.rmtree(currentDir)

print(GREENTXT + "Done!")