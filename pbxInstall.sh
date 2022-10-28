#!/bash/bin

NORMAL = "\033[0;39m"
GREEN = "\033[31m"

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

touch log.txt

echo "Alex's file mover install complete!"

rm pbxInstall.sh
rm install.sh