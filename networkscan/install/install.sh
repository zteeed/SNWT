#! /bin/bash

function ask_debian() {
  read -p "This script has been tested on Debian stretch, keep going ? (y/N) " -r
  if [[ ! $REPLY =~ ^[Yy]$ ]]; then 
    exit 1
  else
    install_debian_stretch
  fi
}

function ask_auto_config() {
  read -p "Do you want ton make an automatic apache2/postgresql configuration ? (y/N) " -r
  if [[ $REPLY =~ ^[Yy]$ ]]; then 
    apache2_config
    postgresql_config
  fi
}

function postgresql_config() {
  file="$(find /etc -name pg_hba.conf)"
  line="$(cat $file | awk '{print NR-1 ";" $0}' | grep 'local.*all.*postgres' | cut -d';' -f1)"
  line=$(($line+1))
  echo "$file --> line=$line"
  sed -i "$line""s|peer|trust|g" $file
  sudo /etc/init.d/postgresql restart
}

function apache2_config() {
  file="/etc/apache2/apache2.conf"
  line="$(cat $file | awk '{print NR-1 ";" $0}' | awk '/<Directory \/var\/www/{flag=1;next}/<\/Directory/{flag=0}flag' | grep -i 'AllowOverride None' | cut -d';' -f1)"
  #line=$(($line+1))
  echo "$file --> line=$line"
  sed -i "$line""s|None|All|g" $file
  sudo /etc/init.d/apache2 restart
}

function install_debian_stretch() {
  path="/var/www/html/"
  sudo apt install git curl apache2 php postgresql php-pgsql python3 python3-pip
  sudo pip3 install -r requirements.txt
  git clone https://github.com/sweetalert2/sweetalert2.git
  curl -sL https://deb.nodesource.com/setup_10.x | sudo -E bash -
  sudo apt-get install -y nodejs
  cd ../../website/
  npm install --save sweetalert2
  cd -
  mv sweetalert2 ../../website/
  ask_auto_config
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
