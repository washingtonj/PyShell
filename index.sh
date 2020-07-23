#! /bin/sh

clear
echo "Hi, this bash install all necessary tools for development"
echo "for first, let's update you dependecies and install python for run other shell commands \n" 

# Update repos and install python for run other scripts.
echo "Insert your password for update deps"
apt update && which python3 lsb-release || apt install curl python3 lsb-release whiptail -y 
yum update && which python3 lsb-release || yum -y install curl python3 redhat-lsb newt 

echo "Let's start a python script for install other applications"
python3 index.py