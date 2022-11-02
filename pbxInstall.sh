#!/bash/bin

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
echo "What is the source - "
read src 
echo $src >> inputs.txt
echo "What is it going? - "
read dest 
echo $dest >> inputs.txt

yum -y update
yum -y install yum-utils

ln -s /usr/bin/python3.6 /usr/bin/python3

yum install python36u-pip
echo "pip installed!"


pip3.6 install --upgrade pip
echo "pip updated!"

pip3.6 install paramiko
echo "paramiko installed!" 

pip3.6 install tqdm
echo "tqdm installed!"

yum -y install python36u-devel

echo "Alex's file mover install complete!"

rm pbxInstall.sh
rm install.sh