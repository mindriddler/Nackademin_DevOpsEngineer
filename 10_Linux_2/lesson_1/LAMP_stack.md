sudo apt update && sudo apt upgrade -y
sudo apt install apache2
sudo apt install mysql-server
sudo mysql_secure_installation
sudo apt install php libapache2-mod-php php-mysql php-curl php-gd php-mbstring php-xml php-xmlrpc php-soap php-intl php-zip
sudo nano /etc/apache2/sites-available/wordpress.conf

<VirtualHost *:80>
    ServerName YOUR_DOMAIN_OR_IP
    DocumentRoot /var/www/wordpress

    <Directory /var/www/wordpress>
        Options -Indexes
        AllowOverride All
        Require all granted
        DirectoryIndex index.php
    </Directory>
</VirtualHost>

sudo a2ensite wordpress
sudo a2dissite 000-default
sudo a2enmod rewrite
sudo service apache2 reload

sudo mysql -u root -p


CREATE DATABASE wordpress DEFAULT CHARACTER SET utf8 COLLATE utf8_unicode_ci;

CREATE USER 'wordpressuser'@'localhost' IDENTIFIED BY 'STRONG_PASSWORD';

GRANT ALL ON wordpress.* TO 'wordpressuser'@'localhost';

FLUSH PRIVILEGES;

EXIT;

cd /tmp
curl -O https://wordpress.org/latest.tar.gz
tar xzvf latest.tar.gz
touch /tmp/wordpress/.htaccess
cp /tmp/wordpress/wp-config-sample.php /tmp/wordpress/wp-config.php
mkdir /tmp/wordpress/wp-content/upgrade

sudo cp -a /tmp/wordpress/. /var/www/wordpress
sudo chown -R www-data:www-data /var/www/wordpress
sudo find /var/www/wordpress/ -type d -exec chmod 750 {} \;
sudo find /var/www/wordpress/ -type f -exec chmod 640 {} \;

curl -s https://api.wordpress.org/secret-key/1.1/salt/

sudo nano /var/www/wordpress/wp-config.php

define('DB_NAME', 'wordpress');
define('DB_USER', 'wordpressuser');
define('DB_PASSWORD', 'STRONG_PASSWORD');
and replace secret keys

sudo service apache2 restart

sudo apt install certbot python3-certbot-apache

sudo certbot --apache




