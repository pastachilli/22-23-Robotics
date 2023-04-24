# University of Iowa Robotics Club Rover Code

This repository contains the code for the University of Iowa Robotics Club's Mars-like rover, which competes in international competitions such as the Canadian International Rover Challenge (CIRC). The rover is designed to perform a variety of tasks, including autonomous navigation, moving an arm, streaming webcam feeds, utilizing camera vision for autonomy, wirelessly connecting to beacons, and receiving GPS data.

## Components and Sensors

The rover is equipped with a GPS sensor, four cameras, and various science-related equipment. The code is structured into two main folders: `rover` and `homebase`.

- `rover`: Contains the code for the rover itself, which includes various ROS2 publishers and subscribers.
- `homebase`: Contains the code for the "Mission Control" component, which also includes various ROS2 publishers and subscribers.

The code is primarily written in Python and runs on a ROS2 (Robot Operating System 2) environment.

## Setup and Deployment

To set up and deploy the code, follow these steps:

1. Install ROS2 Humble by following the instructions in the [official documentation](https://docs.ros.org/en/humble/Installation.html).
2. Clone the repository: `https://github.com/pastachilli/22-23-Robotics`
3. Ensure that your environment is properly set up by sourcing the ROS2 installation: `source /opt/ros/humble/setup.bash`
4. Create a new ROS2 workspace if you haven't already: `mkdir -p ~/ros2_ws/src`
5. Navigate to the `src` directory in your ROS2 workspace: `cd ~/ros2_ws/src`
6. Create a new package directory for the rover or homebase code, e.g., `mkdir rover_package && cd rover_package`
7. Copy or symlink the `rover` or `homebase` directory from the cloned repository into the package directory: `cp -r /path/to/cloned/repo/rover .` or `cp -r /path/to/cloned/repo/homebase .`
8. Create a `setup.py` file in the package directory, specifying the entry points for the ROS2 nodes, and any other necessary configurations.
9. Create a `package.xml` file in the package directory, providing package metadata, dependencies, and any other necessary information.
10. Navigate back to the root of your ROS2 workspace: `cd ~/ros2_ws`
11. Build the workspace: `colcon build`
12. Source the workspace: `source install/setup.bash`
13. Launch the desired ROS2 nodes using the `ros2 launch` command, specifying the appropriate launch files for your use case.

_TODO_: Add information on external libraries and dependencies once they are provided.

