#! /bin/bash

source /root/ws_baxter/rosenv-baxter-master.bash
rosrun baxter_tools tuck_arms.py -t
rosrun baxter_tools enable_robot.py -d
