#!/usr/bin/env bash

rpm --import /etc/pki/rpm-gpg/RPM-GPG-KEY-CentOS-7

yum install -y net-tools

echo "Create deploy user"
useradd -c "deploy" -d /home/deploy -m deploy

echo "Give sudo rights"
echo "%deploy ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers.d/vagrant

echo "Set timezone to Swedish time"
sudo timedatectl set-timezone Europe/Stockholm

yum install -y cifs-utils

echo "Create authorized_keys file"
sudo -u deploy bash << EOF
mkdir -p ~/.ssh
chmod 777 ~/.ssh
chown deploy:deploy ~/.ssh
touch ~/.ssh/authorized_keys
EOF

echo "Fix key to authorized_keys"
cat /vagrant/deploy_id_rsa.pub >> /home/deploy/.ssh/authorized_keys

echo "Fix permissions for ssh"
sudo -u deploy bash << EOF
chmod 700 ~/.ssh
chmod 600 ~/.ssh/authorized_keys
EOF
