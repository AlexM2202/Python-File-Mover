#Alex Marquardt

import os
import shutil

src = os.fspath(os.getcwd())

dest = input("Where is this going to - ")

for file in os.listdir():
    if file == "mover.py":
        continue
    if os.path.isdir(file):
        finial = shutil.move(src, dest)
        #print(shutil.move(src,dest))
        print("Destination path:", finial)
