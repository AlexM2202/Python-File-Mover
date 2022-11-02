#!bash/bin

sudo apt install pip
echo "pip installed!"

sudo pip install paramiko
echo "paramiko installed!"

sudo pip install tqdm
echo "tqdm installed!"

touch log.txt
touch inputs.txt
echo "Alex's file mover setup complete!"

sudo rm install.sh
sudo rm pbxInstall.sh