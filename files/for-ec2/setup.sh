#!/bin/bash

#setup.sh - automating "Install a web server on your EC2 instance" from AWS Amazon docs

sudo dnf update -y

#install Apache web server, PHP, and MariaDB
sudo dnf install -y httpd php php-mysqli mariadb105

#todo: if error then 'cat /etc/system-release'
#to verify that instance was launched with Amazon Linux 2023 AMI
#and not with Amazon Linux 2 AMI

#start web server and enable it to start on boot
sudo systemctl start httpd
sudo systemctl enable httpd

#if user is alreday in the apache group then exit
if id -nG ec2-user | grep -qw apache; then
    echo "ec2-user is already in the apache group"

    #show apache group exists
    groups
else
    echo "Adding ec2-user to the apache group..."
    sudo usermod -a -G apache ec2-user
    echo "ec2-user has been added to the apache group"
    echo "You must log out and log back in for group changes to take effect"
    echo "Please run setup.sh again..."
    exit 0
fi

#change group ownership of /var/www and its contents to apache group
sudo chown -R ec2-user:apache /var/www

#change directory permissions of /var/www and its subdirectories to 
#add group write permissions and set group ID on future subdirectories
sudo chmod 2775 /var/www
find /var/www -type d -exec sudo chmod 2775 {} \;

#recursively change file permissions of /var/www and its subdirectories
find /var/www -type f -exec sudo chmod 0664 {} \;

#get absolute file path to setup.sh
abs_script_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
echo "Absolute script directory: $abs_script_dir"

#copy dbinfo.inc created with setup.py to /var/www/inc/
#copy SamplePage.php to /var/www/html/
mkdir -p /var/www/inc/
cp "$abs_script_dir/dbinfo.inc" /var/www/inc/
echo "Copied dbinfo.inc to /var/www/inc/"
cp "$abs_script_dir/SamplePage.php" /var/www/html/
echo "Copied SamplePage.php to /var/www/html/"
