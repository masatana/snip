# Show downloaded docker images

```
$ sudo docker images
REPOSITORY                    TAG                 IMAGE ID            CREATED             VIRTUAL SIZE
kalilinux/kali-linux-docker   latest              11cd69e79221        7 days ago          325.1 MB
```

# docker run
```
$ sudo docker run -i -t [--name container_name] [image_name]:[tag_name] [args]
```

* `-d`: do background mode
* `-i`: connect host stdin to guest stdin
* `-t`: get tty

If escape with C-d, then guest paused.

To confirm, do `sudo docker ps -a`

# docker commit
To make new docker images, use `commit` command.

# docker rm
* docker rm [container_name] OR [container_id] ... remove docker container
* docker rmi [image_name] OR [image_id] ... remove docker image

# docker start
```
$ sudo docker start -i [container_name]
```
