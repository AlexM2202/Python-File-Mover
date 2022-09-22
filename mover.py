#Alex Marquardt

import os
import shutil

src = os.fspath(os.getcwd())

dest = input("Where is this going to - ")

for file in os.listdir():
    if file == "mover.py" or file == ".git":
        continue
    if os.path.isdir(file):
        finial = shutil.move(src + "/" + file, dest)
        print("Destination path:", finial)
