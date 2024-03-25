# FMs_with_ZED2
Implementing foundation models and other applications with ZED2 camera

## Platforms
* Ubuntu 20.04, ROS2 Foxy 

* NVIDIA Jetson Orin Nano

* ZED2 Camera

## ZED2 Camera Setup
The NAV2 SLAM Toolbox supports ZED camera series: [Using VIO to Augment Robot Odometry](https://navigation.ros.org/tutorials/docs/integrating_vio.html)

To print only certain desired fields published in a ros2 topic, use 'grep' command piped from 'ros2 topic echo', for example:
```
ros2 topic echo /zed/zed_node/odom | grep -A 4 "pose"
```

## SLAM Toolbox and NAV2

Quickly test SLAM toolbox, after installing [turtlebot3 package](https://github.com/ROBOTIS-GIT/turtlebot3/tree/foxy-devel) by ROBOTIS :
```
ros2 launch turtlebot3_gazebo turtlebot3_world.launch.py
ros2 launch turtlebot3_navigation2 navigation2.launch.py
ros2 launch slam_toolbox online_async_launch.py
```

Before launching turtlebot3_world, export the following variables:
```
export TURTLEBOT3_MODEL=waffle LDS_MODEL=LDS-01
```
