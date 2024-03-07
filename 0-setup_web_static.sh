#!/usr/bin/env bash
if ! command -v nginx &> /dev/null; then
	sudo apt-get update
	sudo apt-get install -y nginx
fi
sudo mkdir -p /data/web_static/releases/test
sudo mkdir -p /data/web_static/shared

echo "Hello" | sudo tee /data/web_static/releases/test/index.html

sudo rm -rf /data/web_static/current
sudo ln -s /data/web_static/releases/current/ /data/web_static/releases/test/

sudo chown -R ubuntu:ubuntu /data/

sudo sed -i 's|# server_name _;|location /hbnb_static/ {\n\talias /data/web_static/current/;\n\tindex index.html;\n}\n\nserver_name _;|' /etc/nginx/sites-available/default

sudo service nginx restart
exit 0
