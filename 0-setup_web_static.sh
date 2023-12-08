#!/usr/bin/env bash
<<<<<<< HEAD
#sets up the web server for the deployment of web_static

apt update
apt install nginx -y

mkdir -p /data/web_static/shared/
mkdir -p /data/web_static/releases/test/
echo "This shit is working" > /data/web_static/releases/test/index.html
ln -sf /data/web_static/releases/test/ /data/web_static/current

chown -R ubuntu:ubuntu /data/

printf %s "server {
    listen 80;
    listen [::]:80;
    add_header X-Served-By $HOSTNAME;
    root /var/www/html;
    index index.html;
    location /hbnb_static {
        alias /data/web_static/current;
        index index.html;
    }
    location /redirect_me {
        return 301 https://www.youtube.com/watch?v=QH2-TGUlwu4;
    }
    error_page 404 /404.html;
    location /404 {
      root /var/www/html;
      internal;
    }
}" > /etc/nginx/sites-available/default

service nginx restart
=======
# Sets up web servers for deployment of web_static.

# Install Nginx if not installed
if ! command -v nginx &>/dev/null; then
    sudo apt-get update
    sudo apt-get install -y nginx
fi

# Create necessary directories if they don't exist
sudo mkdir -p /data/web_static/{releases/test,shared}
sudo mkdir -p /data/web_static/releases/test/
sudo touch /data/web_static/releases/test/index.html

# Create a fake HTML file
echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" | sudo tee /data/web_static/releases/test/index.html

# Create a symbolic link
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

# Give ownership of the /data/ folder to the ubuntu user AND group
sudo chown -R ubuntu:ubuntu /data/

# Update the Nginx configuration to serve the content of /data/web_static/current/ to hbnb_static
sudo sed -i '/listen 80 default_server/a location /hbnb_static { alias /data/web_static/current/;}' /etc/nginx/sites-enabled/default

# Restart Nginx
sudo service nginx restart
>>>>>>> 2f50fd399eb08e6a79fda921ef784634adc2e41f
