#! /bin/sh

clear
echo "Hi, this bash install all necessary tools for development"
echo "for first, let's update you dependecies and install python for run other shell commands \n" 

# Update repos and install python for run other scripts.
echo "Insert your password for update deps"
sudo apt update && which python3 || sudo apt install python3 -y

echo "Let's start a python script for install other applications"
python3 main.py