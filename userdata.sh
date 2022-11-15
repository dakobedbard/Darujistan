#!/bin/bash
exec > >(tee /var/log/user-data.log|logger -t user-data -s 2>/dev/console) 2>&1
echo "Hello World"
echo "This is a sample user data script"

sudo apt-get update && sudo apt-get -y upgrade
sudo apt-get -y install lsb-core