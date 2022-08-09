#!/bin/bash

echo 'This is the Ubuntu hardening script for the Faith-Kids2022 team'
echo 'Created by Dylan Wondal'
echo '

'

## Detect if the user is root
if [ "$EUID" -ne 0 ]
  then echo "Please run as root"
  exit
fi

## Upgrade system to ensure everything is up to date
sudo apt-get update > /dev/null
wait
sudo apt-get upgrade -y > /dev/null
wait
echo 'System is now up to date'

## Check if ufw is running and start if not
if [ -z "$(ps -A | grep ufw)" ]
  then
    echo 'ufw is not running, starting ufw'
    sudo ufw enable
    sudo ufw status
  else
    echo 'ufw is already running'
fi

## Check if pam cracklib is installed and install if not
if [ -z "$(dpkg -l | grep libpam-cracklib)" ]
  then
    echo 'pam-cracklib is not installed, installing'
    sudo apt-get install -y libpam-cracklib > /dev/null
    echo 'pam-cracklib is installed'
  else
    echo 'pam-cracklib is already installed'
fi


## Password policy 
sed -i.bak -e 's/PASS_MAX_DAYS\t[[:digit:]]\+/PASS_MAX_DAYS\t90/' /etc/login.defs
sed -i -e 's/PASS_MIN_DAYS\t[[:digit:]]\+/PASS_MIN_DAYS\t10/' /etc/login.defs
sed -i -e 's/PASS_WARN_AGE\t[[:digit:]]\+/PASS_WARN_AGE\t7/' /etc/login.defs
sed -i -e 's/difok=3\+/difok=3 ucredit=-1 lcredit=-1 dcredit=-1 ocredit=-1/' /etc/pam.d/common-password
sed -i -e '$a auth required pam_tally2.so deny=5 onerr=fail unlock_time=1800' /etc/pam.d/common-auth
echo 'Password policy is now set'








