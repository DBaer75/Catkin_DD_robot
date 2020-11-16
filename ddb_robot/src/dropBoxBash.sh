#!/bin/bash

x_loc=$1
y_loc=$2
name=$3
rosrun gazebo_ros spawn_model -file /home/user/catkin_ws/src/Catkin_DD_robot/ddb_robot/models/box.sdf -sdf -x $x_loc -y $y_loc -z 5 -model $name

