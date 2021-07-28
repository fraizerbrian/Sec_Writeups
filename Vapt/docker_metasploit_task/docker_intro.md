# Docker

## Introduction to docker
Running metasploit on docker

docker images available on docker hub

Run docker on host machine by running `sudo docker run --rm -it -p 80:8080 peakkk/metasploitable`

to check available local images use `docker images`

to find docker images running use `docker ps -a`

running docker  with eg ubuntu 16.04 `docker run -it --name test 005d2078bdfa /bin/bash`



`docker run -`
`it` interactive session

`--name` give the docker a name

`--rm` doesnt save any work proceeded with, deletes container once exited

`-d` detached state

or alternatively together with another docker image
```
docker run -d --rm -p 3000:3000 bkimminich/juice-shop

docker run -it --rm parrotsec/security /bin/bash
```

Above runs owasp juice and parrot containers together

Confirm running on the image by running cat /etc/*issue

stopping a container `docker container stop [container_id]`

[https://hub.docker.com/r/citizenstig/dvwa](https://hub.docker.com/r/citizenstig/dvwa)

