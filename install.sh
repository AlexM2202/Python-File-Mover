#!bash/bin

touch log.txt
touch inputs.txt
echo "What is the address? - "
read address
echo $address >> inputs.txt 
echo "What is the username? - "
read user
echo $user >> inputs.txt
echo "What is the password? - "
read pass
echo $pass >> inputs.txt
echo "What is the source? - "
read src 
echo $src >> inputs.txt
echo "What is it going? - "
read dest 
echo $dest >> inputs.txt

sudo apt install pip
echo "pip installed!"

sudo pip install paramiko
echo "paramiko installed!"

sudo pip install tqdm
echo "tqdm installed!"

echo "Alex's file mover setup complete!"

sudo rm install.sh
sudo rm pbxInstall.sh
sudo rm README.md