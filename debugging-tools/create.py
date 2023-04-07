import os

def main():
    global depth
    depth = int(input("Depth:"))
    global width
    width = int(input("Width:"))
    createTree(os.fspath(os.getcwd()),0)

def createTree(path, curDepth):
    for num in range(width):
        if curDepth <= depth:
            os.mkdir(f"{path}/Dir{num}")
            createTree(f"{path}/Dir{num}",curDepth+1)
        file = open(f"{path}/File","w")
        file.write("Hello world\n")
        file.close()

if __name__ == "__main__":
    os.chdir('..')
    main()