# slam-docker
Docker image of existing SLAM frameworks

## Description

`slam-docker` repo contains a *Dockerfile* file used to create the Docker image containing libraries and dependencies required to run popular SLAM frameworks.

There is no need to clone this repository when you want to run the Docker container on your system. Simply pull the latest image(`heejoon1130/slam:0.2`) from *Docker Hub* and create a container using `docker run`.

Clone this repository only when you want to submit changes to the existing Docker image.

## Compatibility

* Ubuntu
* Windows 10 with WSL2
> This Docker image does not run on ARM64 systems

## Supported Frameworks

* ORB-SLAM2(Kitti)
* LDSO(Kitti, EuRoC)
> This Docker image does not contain any datasets. All the datasets must exist on the host system prior to running the Docker container.

## Links

https://hub.docker.com/repository/docker/heejoon1130/slam
