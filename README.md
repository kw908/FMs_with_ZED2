# FMs_with_ZED2
Implementing foundation models and other applications with ZED2 camera

## Platforms
* Ubuntu 20.04, ROS2 Foxy 

* NVIDIA Jetson Orin Nano

* ZED2 Camera

## ZED2 Camera Setup

## SLAM Toolbox and NAV2

Quickly test SLAM toolbox, after installing turtlebot3 package by ROBOTIS (https://github.com/ROBOTIS-GIT/turtlebot3/tree/foxy-devel):
```
ros2 launch turtlebot3_gazebo turtlebot3_world.launch.py
ros2 launch turtlebot3_navigation2 navigation2.launch.py
ros2 launch slam_toolbox online_async_launch.py
```

Before launching turtlebot3_world, export the following variables:
```
export TURTLEBOT3_MODEL=waffle LDS_MODEL=LDS-01
```
