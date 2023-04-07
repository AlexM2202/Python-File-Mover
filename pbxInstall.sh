#!/bash/bin

BLUE='\033[36m'
GREEN='\033[32m'

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

yum -y update
yum -y install yum-utils

ln -s /usr/bin/python3.6 /usr/bin/python3

yum install python36u-pip
echo ""
echo -e "${GREEN}pip installed!\033[0m"
echo ""


pip3.6 install --upgrade pip
echo ""
echo -e "${GREEN}pip updated!\033[0m"
echo ""

pip3.6 install paramiko
yum -y install python36u-devel
echo ""
echo -e "${GREEN}paramiko installed!\033[0m"

echo ""
echo -e "${BLUE}<--===================================-->\033[0m"
echo -e "   ${GREEN}Alex's file mover install complete!\033[0m"
echo -e "${BLUE}<--===================================-->\033[0m"
echo ""

rm pbxInstall.sh
rm install.sh
rm README.md