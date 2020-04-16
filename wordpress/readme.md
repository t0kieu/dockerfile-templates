# Docker setup for wordpress & mariadb

This wordpress stack is based on:
 - mariadb:latest
 - wordpress with php-fpm on alpine
 - nginx on alpine
 
 # Setup
 ```bash
# Copy example file as .env
cp .env.example .env 
# Edit environment variables
vim .env
# Start it
docker-compose up -d
 ```

# TODO
- Setup HTTPS in nginx
- Add support for CDN
