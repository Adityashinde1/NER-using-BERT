#!bin/bash

sudo apt update 

sudo apt-get update

sudo apt upgrade -y 

curl -fsSL https://get.docker.com -o get-docker.sh

sudo sh get-docker.sh

sudo usermod -aG docker cloud

sudo usermod -aG docker circleci

newgrp docker

curl -O https://dl.google.com/dl/cloudsdk/channels/rapid/downloads/google-cloud-cli-409.0.0-linux-x86_64.tar.gz

tar -xf google-cloud-cli-409.0.0-linux-x86_64.tar.gz

./google-cloud-sdk/install.sh --path-update true