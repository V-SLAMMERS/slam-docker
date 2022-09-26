FROM ubuntu:18.04

RUN apt update && apt upgrade -y

RUN apt install -y build-essential cmake git pkg-config libgtk-3-dev libavcodec-dev libavformat-dev libswscale-dev libv4l-dev libxvidcore-dev libx264-dev libjpeg-dev libpng-dev libtiff-dev gfortran openexr libatlas-base-dev python3-dev python3-numpy libtbb2 libtbb-dev libdc1394-22-dev

RUN mkdir -p /home/slam/lib

WORKDIR /home/slam/lib

RUN git clone https://github.com/opencv/opencv.git
RUN git clone https://github.com/opencv/opencv_contrib.git

# openCV
WORKDIR /home/slam/lib/opencv
RUN git checkout 3.4.9
WORKDIR /home/slam/lib/opencv_contrib
RUN git checkout 3.4.9
RUN mkdir -p /home/slam/lib/opencv/build
WORKDIR /home/slam/lib/opencv/build
RUN cmake -D OPENCV_EXTRA_MODULES_PATH=../../opencv_contrib/modules ..
RUN make -j8
RUN make install

# Eigen3
RUN apt install libeigen3-dev

# Pangolin
WORKDIR /home/slam/lib
RUN git clone https://github.com/HeejoonLee/pangolin_v0.5_w.git
WORKDIR /home/slam/lib/pangolin_v0.5_w
RUN apt install -y libgl1-mesa-dev libwayland-dev libxkbcommon-dev wayland-protocols libegl1-mesa-dev libc++-dev libglew-dev libeigen3-dev cmake g++ ninja-build libjpeg-dev libpng-dev libavcodec-dev libavutil-dev libavformat-dev libswscale-dev libavdevice-dev
RUN mkdir -p /home/slam/lib/pangolin_v0.5_w/build
WORKDIR /home/slam/lib/pangolin_v0.5_w/build
RUN cmake .. && make install

# ORB-SLAM 2
WORKDIR /home/slam
RUN git clone https://github.com/HeejoonLee/orb_slam2_w.git
WORKDIR /home/slam/orb_slam2_w
RUN ./build.sh

# LDSO
WORKDIR /home/slam
RUN git clone https://github.com/tum-vision/LDSO.git
WORKDIR /home/slam/LDSO
RUN apt install -y libgoogle-glog-dev libboost-all-dev
RUN ./make_project.sh
RUN mkdir /home/slam/vocab
RUN cp /home/slam/LDSO/vocab/orbvoc.dbow3 /home/slam/vocab/orbvoc.dbow3

# Script for running each SLAM
WORKDIR /home/slam
COPY run_slam.py /home/slam/
RUN chmod a+x *.py

# All datasets are located in: /home/slam/datasets

CMD ["/usr/bin/python3", "run_slam.py"]
