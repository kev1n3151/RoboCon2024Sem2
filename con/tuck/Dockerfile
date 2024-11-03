# https://hub.docker.com/r/davetcoleman/baxter_simulator/~/dockerfile/
# vicariousinc/baxter-simulator:kinetic
# Run simulated Baxter in Gazebo

#FROM osrf/ros:kinetic-desktop-full-jessie
#FROM osrf/ros:kinetic-desktop-full

# https://github.com/ipeakermit/baxter-mobility-base-simdemo
FROM vxlab-rosie-core
MAINTAINER Ian Peake ian.peake@rmit.edu.au

ENV TERM xterm

# Setup catkin workspace
ENV CATKIN_WS=/root/ws_baxter
WORKDIR $CATKIN_WS/src

RUN apt -qq update && apt -y dist-upgrade
RUN apt-get update && apt-get -y install vim-tiny

COPY src $CATKIN_WS/src
 
# Replacing shell with bash for later docker build commands
RUN mv /bin/sh /bin/sh-old && \
    ln -s /bin/bash /bin/sh

RUN echo force docker rebuild 

RUN echo workspace $CATKIN_WS
WORKDIR $CATKIN_WS

COPY rosenv-baxter-master.bash rosenv-baxter-master.bash
RUN chmod +x rosenv-baxter-master.bash
COPY launch.bash launch.bash
COPY tuck.bash tuck.bash
#COPY untuck.bash untuck.bash
COPY tf.launch tf.launch
COPY xsetup.bash xsetup.bash
#COPY default.rviz /opt/ros/melodic/share/rviz/default.rviz
RUN chmod +x *.bash

RUN catkin build
#CMD ['./tuck.bash']
#RUN echo "source ~/ws_baxter/rosenv-baxter-master.bash" >> /root/.bashrc
