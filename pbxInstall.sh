#!/bash/bin

NORMAL = "\033[0;39m"
GREEN = "\033[31m"

yum -y update
yum -y install yum-utils

ln -s /usr/bin/python3.6 /usr/bin/python3

yum install python36u-pip
echo $GREEN "pip installed!" $NORMAL

pip3.6 install --upgrade pip
echo $GREEN "pip updated!" $NORMAL

pip3.6 install paramiko
echo $GREEN "paramiko installed!" $NORMAL

pip3.6 install tqdm
echo $GREEN "tqdm installed!" $NORMAL

yum -y install python36u-devel

echo $Green "Alex's file mover install complete!" $NORMAL

rm pbxInstall.sh
rm install.sh