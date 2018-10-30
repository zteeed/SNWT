#! /bin/bash

function ask_debian() {
  read -p "This script has been tested on Debian stretch, keep going ? (y/N) " -r
  if [[ ! $REPLY =~ ^[Yy]$ ]]; then 
    exit 1
  else
    install_debian_stretch
  fi
}

function install_debian_stretch() {
  path="/var/www/html/"
  sudo apt install apache2 php postgresql php-pgsql python3 python3-pip
  sudo pip3 install -r requirements.txt
}

function main() {
  echo "-----------------------------------------------------"
  echo "----- Automatic Installation of the Environment -----"
  echo "-----------------------------------------------------"
  echo
  if lsb_release -a | grep -i "debian" > /dev/null; then
    if lsb_release -a | grep -i "stretch" > /dev/null; then
      echo "Debian stretch detected... OK!"; echo
      install_debian_stretch
    else
      ask_debian
    fi
  else
    ask_debian
  fi
}

main
