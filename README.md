# Python-File-Mover

Welcome to Alex's python file mover. This program was designed to transport any number of folders with files inside of them to a new host through a ssh service.
This program was designed for freePBX with the intent to move a mass amount of recoarded calls to a NAS storage, but it can work on almost any linux machine.
The program scans a directory that you specify for its contents and moves them to a location of your choice. As of now this program will work on any pbx machine for moving recorded calls to another device over a network but will be updated to work on any device in the future. Right now it can only scan 3 folders deep but a later version will allow it to scan any number, and this update will allow it to work on any machine. There is an aditional program called tree.py with its classes in folder rptree that can map a directory tree from any starting location you give it.

To install all required pachages run the command "bash install.sh" or if you are on a freePBX machine run "bash pbxInstall.sh" instead.

To download on your machine either run ```git clone https://github.com/AlexM2202/Python-File-Mover.git``` or download the .zip file.

There are 2 versuons of the program. One is titled move and the other is Copy. Move will delete the moved files off of the hosts computer. Copy will strictly copy the files from the host computer. Both versions have an automated version called auto*.py (* is either move or copy). Both of these will use an input file that was created during install. The manual versions will prompt the user for inputs in the program.

README.md will be deleated in the installer!!
