#!/bin/bash                                                                                                                   
# enable use of X on docker console host
USER=root
groupdel video &> /dev/null || true
#groupadd -og "${VIDEO_GROUP_ID}" video
groupadd -og "44" video
gpasswd -a "${USER}" video
#export DISPLAY=:0              
