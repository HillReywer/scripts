#!/bin/bash

# Parameters
APP_NAME="your_app_name"
APP_DIR="/var/www/$APP_NAME"
REPOSITORY="https://github.com/your_username/your_repository.git"
BRANCH="main"
NGINX_CONFIG="/etc/nginx/sites-available/$APP_NAME"
NEW_RELEASE_DIR="$APP_DIR/releases/$(date +%Y%m%d%H%M%S)"

# Create a new release directory
mkdir -p $NEW_RELEASE_DIR

# Clone the latest version of the application
git clone -b $BRANCH $REPOSITORY $NEW_RELEASE_DIR

# Install dependencies and build the application
cd $NEW_RELEASE_DIR
npm install
npm run build

# Create a symlink for the new release
ln -sfn $NEW_RELEASE_DIR $APP_DIR/current

# Update the Nginx configuration to point to the new release
sudo sed -i "s|root .*;|root $APP_DIR/current/public;|" $NGINX_CONFIG

# Reload Nginx to apply the changes
sudo systemctl reload nginx

# Remove old releases to save disk space (keep the latest 5 releases)
ls -1 $APP_DIR/releases/ | sort -rn | tail -n +6 | xargs -I{} rm -rf $APP_DIR/releases/{}
