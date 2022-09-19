# FRC-ROS

This is the source code for using ROS with an FRC Robot. The steps for installing and running ROS applications are identical for desktop PC's, laptops, Raspberry PI, NVidia Jetson.

## Youtube Demos
Simulation Demo: https://www.youtube.com/watch?v=qSjgmY7hYsY

Teleop Demo w/ SLAM: https://www.youtube.com/watch?v=1Qe-s1liH5k

Autonomous and Swerve Simulation: https://youtu.be/OrnWRP20IEY

## Setup

Setup is fairly simple. You will need a computer with Ubuntu 16.04 installed. This package is intended to be used on an NVidia Jetson TX2, however, you should be able to run it on a Raspberry Pi as well, but that won't have the performance of a PC or a Jetson.

### 1. Install Ubuntu on Your Computer

Make sure you have Ubuntu 20.04 installed on your computer: https://tutorials.ubuntu.com/tutorial/tutorial-install-ubuntu-desktop-1604#0

### 2. Download FRC-ROS to Your Computer

Enter the following to download FRC-ROS to your Documents:
```
cd ~/Documents
git clone https://github.com/JakeAllison/FRC-ROS.git
cd FRC-ROS
./Setup.sh
```


### 4. Install FRC-ROS on  (Skip if you're not using a Jetson)

Follow the steps above to install on your computer. This process is identical to your computer. Once you know how to use ROS, you will be able to connect your computer to your Jetson and have then interact seamlessly.

### 5. Make Updates When Needed

If you make changes to the source code, you will need to update the files from the location where you downloaded FRC-ROS to your Catkin workspace. Open a terminal and put the following command to bring up the simulation:
```
cd ~/Documents/FRC-ROS
```

### 6. Run a Simulation


You can run a robot simulation in Gazebo simulator. Open a terminal and put the following command to bring up the simulation:
```
roslaunch (package_here) (launch_here)
```
The options include the following and can be typed in similar to above:
- auton: Enables autonomous nagivation and driving.
- kinectlidar: Starts up a Kinect and RPLidarA2 connected over USB.
- robot: FOR THE REAL ROBOT. This brings up all sensors and the bridge to the roboRIO.
- sim: Brings up a simulation.
- slam: Enables SLAM (Simeltaneous Localization and Mapping)
- teleop: Enables teleop control through either GUI or any joystick such as an XBox controller.
- user_interface: Brings up GUI for viewing and sending data to ROS.
- visualize: Bring up RViz used to visualize ROS data.

## To-Do

### Implement a Network Tables Interface for RoboRIO

This requires 2 parts. The first part is a ROS package capable of communicating over FRC Network Tables. The second part needs a software interface on the RoboRIO to send and receive data to and from the Jetson.

Interface will be like this:

RoboRio Software (RoboRio) <--Network Tables--> ROS Converter Node (Rasp) <-- ROS Topics --> ROS Software (Rasp)

### Implement Commands and Data Transfer

The following data is the most essential data that will be transferred:
- Velocity Commands (Rasp -> RoboRIO) (required)
- Send IMU measurements (RoboRIO -> Rasp) (optional)
- Send Wheel Odometry (RoboRIO -> Rasp) (optional)

The folowing data will allow for usability in competition:
- Send Commands (RoboRIO -> Rasp)
- Receive Status (Rasp -> RoboRIO)

Commands from RoboRIO -> Rasp could include stuff like:
- Set navigation goals.
- Activate target tracking.
- Switch to Mapping-Mode (SLAM) or Localization-Only (needs existing map)

Status from Rasp -> RoboRIO could include stuff like:
- Target tracking info
- Localization info
- Navigation statuses
- General ROS Status

Related Resources:
  * https://www.chiefdelphi.com/t/controlling-a-roborio-through-a-raspberry-pi-a-wifi-router/392841
  * https://willhaley.com/blog/raspberry-pi-wifi-ethernet-bridge/
  * [Network Diagram Example](https://imgur.com/a/D1wnLnD)

### Implement Target Tracking

A single ROS node can take any camera data and perform image processing. This can be written and configured however the user likes and can output targeting data. A single node can be run, or multiple nodes can be doing processing on the same camera feed.

## Tutorials and Helpful Information

### Recommended Tutorials to Get Started

Getting Started:
- http://wiki.ros.org/
- http://wiki.ros.org/ROS/Tutorials

Additional Tutorials:
- http://wiki.ros.org/urdf/Tutorials
- http://gazebosim.org/tutorials?tut=ros_overview
- http://wiki.ros.org/rviz/Tutorials
- http://wiki.ros.org/navigation/Tutorials

### Packages and Software Used in FRC-ROS

Some sensor packages are included here:
- http://wiki.ros.org/rplidar
- http://wiki.ros.org/openni_launch

SLAM (Simeltaneous Localization and Mapping):
- https://en.wikipedia.org/wiki/Simultaneous_localization_and_mapping
- http://wiki.ros.org/hector_mapping
- http://wiki.ros.org/gmapping
- http://wiki.ros.org/rtabmap_ros

Robot Localization:
- https://roscon.ros.org/2015/presentations/robot_localization.pdf
- http://docs.ros.org/kinetic/api/robot_localization/html/index.html
- http://www.cs.cmu.edu/~rasc/Download/AMRobots5.pdf

Autonomous Navigation:
- https://en.wikipedia.org/wiki/Robot_navigation
- http://wiki.ros.org/move_base
- http://wiki.ros.org/costmap_2d
- http://wiki.ros.org/nav_core
- http://wiki.ros.org/navfn
- http://wiki.ros.org/dwa_local_planner

### Other Relevant Topics

Swerve Drive Kinematics:
- https://www.chiefdelphi.com/t/paper-4-wheel-independent-drive-independent-steering-swerve/107383

Machine learning is a more advanced topic:
- https://www.youtube.com/watch?v=aircAruvnKk
- https://developer.nvidia.com/embedded/twodaystoademo
- https://github.com/dusty-nv/ros_deep_learning




# M. S: Documentation + More 

[Link](https://docs.google.com/document/d/1wFLX0QiOwCm9FljDG9AHuZatXuKojD4X28V5rhxXCZM/edit#)
