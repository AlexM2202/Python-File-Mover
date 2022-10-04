#!/bash/bin

yum -y update
yum -y install yum-utils
yum -y groupinstall development
yum -y install https://centos7.iuscommunity.org/ius-release.rpm
yum -y install python36u

ln -s /usr.local/bin/python3.6 /usr/local/bin/python3

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
rm -R file
rm -R file2
rm -R plzMove
rm pbxInstall.sh
rm install.sh