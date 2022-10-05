# Python-File-Mover

Welcome to Alex's python file mover. This program was designed to transport any number of folders with files inside of them to a new host through a ssh service.
This program was designed for freePBX with the intent to move a mass amount of recoarded calls to a NAS storage, but it can work on almost any linux machine.
The program scans the directory it is in for all the directories in its home folder and then moves them along with any and all files inside of them to a NAS.
To install all required pachages run the command "bash install.sh" or if you are on a freePBX machine run "bash pbxInstall.sh" instead.

To download on your machine either run "git clone https://github.com/AlexM2202/Python-File-Mover.git" or download the .zip file.

There is a program (create.py) that will generate a number of folders with sub files for you to test the program.

The main program is call "move.py". Run it in the folder that contains the sub folders with files you wish to move.

README.md will be deleated in the installer!!
