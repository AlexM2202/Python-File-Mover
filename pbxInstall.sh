#!/bash/bin

NORMAL = "\033[0;39m"
GREEN = "\033[31m"

yum -y update
yum -y install yum-utils
yum -y groupinstall development
yum -y install https://centos7.iuscommunity.org/ius-release.rpm
yum -y install python36u

ln -s /usr.local/bin/python3.6 /usr/local/bin/python3

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
rm -R file
rm -R file2
rm -R plzMove
rm pbxInstall.sh
rm install.sh