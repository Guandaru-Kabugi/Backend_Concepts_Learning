docker info
docker version
docker login
docker context ls
unset DOCKER_HOST
sudo systemctl restart docker
export DOCKER_HOST=unix:///var/run/docker.sock
cat ~/.docker/config.json
sed -i '/"credsStore": "desktop"/d' ~/.docker/config.
sudo systemctl status docker
sudo systemctl status docker.socket
sudo systemctl stop docker.socket


# Running and Stopping Docker

docker pull [imagename] # pill an image from registry
docker run [imagename] # run containers
docker run -d [imagename] # detached mode
docker start [containername] start stopped containers
docker ps # list running containers
docker ps -a #list running and stopped containers
docker stop [containername] # stop containers
docker kill [containername] # kill containers
docker image inspect [imagename] # get image info
docker run --memory = '256m' nginx # max memory
docker run --cpus = '.5' nginx # max cpu
docker rm [containername]

# Run a container
docker run --publish 80:80 --name webserver nginx
--breakdown--
nginx = container image in the docker registry
webserver = container local name
80:80m= maps the host port to the container listening port


# Attach shell
docker run -it nginx -- /bin/bash # attach shell
docker run -it --microsoft/powershell:nanoserver pws.exe # attach powershell
docker container exec -it [containername] -- bash # attach to a running container

# Cleaning Up
docker rm [containername] # removes stopped containers
docker rm $(docker ps -a -q) #removes all stopped containers
docker images #list images
docker rmi [imagename] #deletes the image
docker system prune -a # removes all images not in use by any container

# Hands on
docker run -d -p 8080:80 --name webserver nginx
docker container exec -it webserver bash

