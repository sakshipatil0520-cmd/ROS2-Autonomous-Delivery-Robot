# 🤖 ROS2 Autonomous Delivery Robot

A ROS2-based autonomous mobile robot simulation designed to perform multi-point package delivery using autonomous navigation, localization, path planning, and task management.

The robot navigates through a simulated environment, visits predefined delivery locations, simulates package delivery, and finally returns to its home position.

This project was collaboratively developed by **Harshvardhan Nayakal** and **Sakshi Patil**.

---

## 📌 Project Overview

The **ROS2 Autonomous Delivery Robot** demonstrates how an autonomous mobile robot can be used for indoor logistics and delivery applications.

The project integrates:

- ROS2 Humble
- TurtleBot3
- Gazebo
- RViz2
- Nav2 Navigation Stack
- AMCL Localization
- Python
- ROS2 Actions
- ROS2 Topics
- TF2

The main system is controlled by a Python-based **Delivery Manager**, which maintains a delivery task queue and sends navigation goals to the Nav2 navigation stack.

The robot is designed to:

1. Start from its home position.
2. Navigate to Delivery Point A.
3. Simulate package delivery.
4. Navigate to Delivery Point B.
5. Simulate package delivery.
6. Navigate to Delivery Point C.
7. Simulate package delivery.
8. Return to the home position.
9. Complete the delivery mission.

---

# 🎯 Project Objectives

The main objectives of this project are:

- Develop an autonomous mobile robot using ROS2.
- Simulate the robot in a Gazebo environment.
- Implement autonomous navigation using Nav2.
- Use AMCL for robot localization.
- Visualize the robot using RViz2.
- Develop a Python-based delivery management system.
- Implement a delivery task queue.
- Navigate to multiple predefined delivery locations.
- Simulate package delivery operations.
- Automatically return the robot to the home position.
- Gain practical experience with ROS2 Actions, Topics, and TF2.

---

# 🧠 System Architecture

```text
                         ROS2 Humble
                              |
                              v
                    Delivery Manager Node
                              |
                              v
                     Delivery Task Queue
                              |
                              v
                    NavigateToPose Action
                              |
                              v
                         ROS2 Nav2
                              |
                +-------------+-------------+
                |                           |
                v                           v
          Global Planner              Local Planner
                |                           |
                +-------------+-------------+
                              |
                              v
                       TurtleBot3 Robot
                              |
                              v
                           Gazebo
```

### Localization System

```text
                    Map
                     |
                     v
                    AMCL
                     |
                     v
                  Odometry
                     |
                     v
                  base_link
                     |
                     v
                    RViz2
```

The expected TF relationship is:

```text
map
 |
 v
odom
 |
 v
base_link
```

---

# 🚚 Delivery Workflow

The robot follows a predefined delivery sequence.

```text
                    START
                      |
                      v
                 HOME POSITION
                      |
                      v
              DELIVERY POINT A
                      |
                      v
             PACKAGE DELIVERED
                      |
                      v
              DELIVERY POINT B
                      |
                      v
             PACKAGE DELIVERED
                      |
                      v
              DELIVERY POINT C
                      |
                      v
             PACKAGE DELIVERED
                      |
                      v
                 RETURN HOME
                      |
                      v
             MISSION COMPLETED
```

---

# 📍 Delivery Locations

The current project contains three delivery points.

| Delivery Task | X Coordinate | Y Coordinate |
|---|---:|---:|
| Delivery Point A | 2.0 | 1.0 |
| Delivery Point B | 3.0 | -1.0 |
| Delivery Point C | 1.0 | -2.0 |

### Home Position

```text
X = 0.0
Y = 0.0
```

> **Important:** The delivery coordinates must be adjusted according to the selected Gazebo map and the robot's starting position.

---

# ✨ Key Features

## 1. Autonomous Navigation

The robot uses the ROS2 Nav2 navigation stack to navigate autonomously to predefined delivery locations.

Nav2 provides:

- Global path planning
- Local path planning
- Obstacle avoidance
- Navigation control
- Goal management

---

## 2. Multi-Point Delivery

The robot can process multiple delivery locations sequentially.

The current task sequence is:

```text
Home
  ↓
Delivery Point A
  ↓
Delivery Point B
  ↓
Delivery Point C
  ↓
Home
```

---

## 3. Delivery Task Queue

Delivery tasks are stored in a Python task queue.

Example:

```python
DELIVERY_TASKS = [
    {
        "name": "Delivery Point A",
        "x": 2.0,
        "y": 1.0
    },
    {
        "name": "Delivery Point B",
        "x": 3.0,
        "y": -1.0
    },
    {
        "name": "Delivery Point C",
        "x": 1.0,
        "y": -2.0
    }
]
```

The Delivery Manager processes each task one at a time.

---

## 4. AMCL Localization

AMCL is used to estimate the robot's position inside the map.

The robot needs a valid localization system before autonomous navigation goals can be executed.

The expected TF tree is:

```text
map
 |
 v
odom
 |
 v
base_link
```

The robot's initial pose can be set in RViz2 using:

```text
2D Pose Estimate
```

---

## 5. RViz2 Visualization

RViz2 is used to visualize:

- Map
- Robot position
- Laser scan
- Robot path
- Navigation goals
- Global costmap
- Local costmap
- AMCL localization

The RViz2 Fixed Frame should normally be:

```text
map
```

Navigation goals can be sent using:

```text
2D Goal Pose
```

---

# 🛠️ Technologies and Tools

| Technology | Purpose |
|---|---|
| ROS2 Humble | Robot middleware |
| Python | ROS2 node development |
| TurtleBot3 | Mobile robot platform |
| Gazebo | Robot simulation |
| RViz2 | Visualization |
| Nav2 | Autonomous navigation |
| AMCL | Robot localization |
| LiDAR | Environment sensing |
| ROS2 Topics | Inter-node communication |
| ROS2 Actions | Navigation goal execution |
| TF2 | Coordinate transformations |
| Ubuntu 22.04 | Development environment |

---

# 📁 Project Structure

```text
ROS2-Autonomous-Delivery-Robot/
│
├── autonomous_delivery_robot/
│   │
│   ├── autonomous_delivery_robot/
│   │   ├── __init__.py
│   │   ├── delivery_manager.py
│   │   └── delivery_tasks.py
│   │
│   ├── launch/
│   │
│   ├── config/
│   │
│   ├── resource/
│   │   └── autonomous_delivery_robot
│   │
│   ├── package.xml
│   ├── setup.py
│   └── setup.cfg
│
├── screenshots/
│   ├── gazebo.png
│   ├── rviz2.png
│   └── delivery_navigation.png
│
├── .gitignore
│
└── README.md
```

---

# 💻 Installation and Setup

## Requirements

Make sure the following software is installed:

- Ubuntu 22.04
- ROS2 Humble
- Gazebo
- RViz2
- TurtleBot3 packages
- Nav2 packages
- Python 3

---

# 📦 Create ROS2 Workspace

```bash
mkdir -p ~/delivery_robot_ws/src
cd ~/delivery_robot_ws/src
```

---

# 📥 Clone the Repository

```bash
cd ~/delivery_robot_ws/src

git clone YOUR_GITHUB_REPOSITORY_URL
```

Replace:

```text
YOUR_GITHUB_REPOSITORY_URL
```

with the actual GitHub repository URL.

---

# 🔨 Build the Workspace

Go to the workspace:

```bash
cd ~/delivery_robot_ws
```

Source ROS2 Humble:

```bash
source /opt/ros/humble/setup.bash
```

Build the project:

```bash
colcon build --symlink-install
```

Source the workspace:

```bash
source ~/delivery_robot_ws/install/setup.bash
```

Verify the package:

```bash
ros2 pkg list | grep autonomous_delivery_robot
```

Expected output:

```text
autonomous_delivery_robot
```

Verify the executable:

```bash
ros2 pkg executables autonomous_delivery_robot
```

Expected output:

```text
autonomous_delivery_robot delivery_manager
```

---

# 🚀 How to Run the Project

The project requires multiple terminals.

---

## Terminal 1: Start Gazebo

Open Terminal 1:

```bash
source /opt/ros/humble/setup.bash

export TURTLEBOT3_MODEL=burger

ros2 launch turtlebot3_gazebo turtlebot3_world.launch.py
```

Wait for Gazebo to load completely.

---

## Terminal 2: Start Nav2

Open Terminal 2:

```bash
source /opt/ros/humble/setup.bash

export TURTLEBOT3_MODEL=burger

ros2 launch turtlebot3_navigation2 navigation2.launch.py use_sim_time:=True
```

Wait for Nav2 to start.

---

## Terminal 3: Start RViz2

Open Terminal 3:

```bash
source /opt/ros/humble/setup.bash

ros2 run rviz2 rviz2
```

In RViz2:

1. Set **Fixed Frame** to:

```text
map
```

2. Select:

```text
2D Pose Estimate
```

3. Click on the robot's estimated position.
4. Drag the mouse to set the robot's orientation.
5. Release the mouse button.

Then use:

```text
2D Goal Pose
```

to test autonomous navigation manually.

---

## Terminal 4: Run Delivery Manager

Open Terminal 4:

```bash
source /opt/ros/humble/setup.bash

source ~/delivery_robot_ws/install/setup.bash

ros2 run autonomous_delivery_robot delivery_manager
```

The Delivery Manager will start processing the delivery task queue.

---

# 🔍 System Verification

Before running the Delivery Manager, verify that Nav2 is active.

Check ROS2 actions:

```bash
ros2 action list
```

The following action should be available:

```text
/navigate_to_pose
```

Check localization:

```bash
ros2 topic echo /amcl_pose --once
```

Check the TF relationship:

```bash
ros2 run tf2_ros tf2_echo map base_link
```

A correctly configured navigation system should provide:

```text
map → odom → base_link
```

Check running nodes:

```bash
ros2 node list
```

Check available topics:

```bash
ros2 topic list
```

---

# 📊 Expected Mission Execution

When all components are correctly configured, the Delivery Manager should execute the following workflow:

```text
================================
Autonomous Delivery Mission
================================

Starting Delivery Point A
        ↓
Navigation Goal Accepted
        ↓
Delivery Point A Reached
        ↓
Package Delivered
        ↓
Starting Delivery Point B
        ↓
Navigation Goal Accepted
        ↓
Delivery Point B Reached
        ↓
Package Delivered
        ↓
Starting Delivery Point C
        ↓
Navigation Goal Accepted
        ↓
Delivery Point C Reached
        ↓
Package Delivered
        ↓
Returning Home
        ↓
Home Position Reached
        ↓
Mission Completed

================================
```

---

# 🧩 ROS2 Concepts Demonstrated

## ROS2 Nodes

The Delivery Manager is implemented as a ROS2 Python node.

---

## ROS2 Actions

The project uses:

```text
NavigateToPose
```

to send navigation goals to the Nav2 navigation server.

---

## ROS2 Topics

ROS2 topics provide communication between different robot components.

---

## TF2

TF2 manages coordinate transformations between:

```text
map
odom
base_link
```

---

## Nav2

The Nav2 navigation framework provides:

- Path planning
- Navigation
- Obstacle avoidance
- Goal execution

---

## AMCL

AMCL provides probabilistic localization of the robot within a known map.

---

# 🔧 Troubleshooting

## Problem 1: Package Not Found

If you see:

```text
Package 'autonomous_delivery_robot' not found
```

Run:

```bash
cd ~/delivery_robot_ws

source /opt/ros/humble/setup.bash

colcon build --symlink-install

source ~/delivery_robot_ws/install/setup.bash
```

Then verify:

```bash
ros2 pkg list | grep autonomous_delivery_robot
```

---

## Problem 2: Nav2 Action Not Available

Check:

```bash
ros2 action list
```

If this action is missing:

```text
/navigate_to_pose
```

make sure Nav2 is running.

---

## Problem 3: Invalid Frame ID "map"

If you see:

```text
Invalid frame ID "map"
```

check:

- Gazebo is running.
- Nav2 is running.
- Map Server is running.
- AMCL is running.
- RViz2 is configured correctly.
- Initial pose has been published.

Check:

```bash
ros2 topic list
```

and:

```bash
ros2 node list
```

---

## Problem 4: Delivery Goal Rejected

If the Delivery Manager reports:

```text
Delivery goal rejected
```

check:

1. Nav2 is running.
2. `/navigate_to_pose` is available.
3. The `map` frame exists.
4. The robot has been localized using `2D Pose Estimate`.
5. The target coordinates are inside the map.
6. The robot is not placed inside an obstacle.
7. The map and localization system are publishing valid TF transforms.

Check:

```bash
ros2 action list
```

Check:

```bash
ros2 run tf2_ros tf2_echo map base_link
```

Check:

```bash
ros2 topic echo /amcl_pose --once
```

---

# 🚧 Current Project Status

## Completed

- [x] ROS2 workspace created
- [x] ROS2 package created
- [x] Delivery Manager node created
- [x] Delivery task queue implemented
- [x] Multiple delivery points configured
- [x] Nav2 Action Client implemented
- [x] TurtleBot3 Gazebo simulation configured
- [x] RViz2 visualization configured
- [x] AMCL localization workflow configured
- [x] Delivery Manager executable configured
- [x] Multi-point delivery task system implemented

## Testing and Future Development

- [ ] Complete end-to-end autonomous navigation testing
- [ ] Validate map-to-robot localization
- [ ] Test multi-point delivery mission
- [ ] Validate automatic return-to-home
- [ ] Add delivery status visualization
- [ ] Add project demonstration video

---

# 🔮 Future Improvements

The project can be extended with:

- Dynamic delivery task allocation
- Real-time package tracking
- QR code-based package verification
- Computer vision-based package identification
- Dynamic obstacle avoidance
- Multi-robot delivery
- Fleet management integration
- Battery monitoring
- Automatic charging station
- Delivery status dashboard
- Web-based monitoring interface
- Voice-based delivery commands
- Real-world TurtleBot3 deployment

---

# 🌟 Future System Architecture

The system can be extended into a complete autonomous logistics platform.

```text
                 Delivery Management System
                            |
                            v
                     Task Allocation
                            |
              +-------------+-------------+
              |                           |
              v                           v
           Robot 1                     Robot 2
              |                           |
              v                           v
            Nav2                        Nav2
              |                           |
              v                           v
           Gazebo                  Gazebo / Real Robot
              |                           |
              +-------------+-------------+
                            |
                            v
                    Delivery Monitoring
```

This system can later be integrated with a **Multi-Robot Fleet Management System** for warehouse, logistics, and industrial automation applications.

---

# 📚 Learning Outcomes

Through this project, we gained practical experience in:

- ROS2 Humble
- Autonomous mobile robotics
- ROS2 Python development
- Nav2 Navigation Stack
- AMCL localization
- Gazebo simulation
- RViz2 visualization
- ROS2 Actions
- ROS2 Topics
- TF2 coordinate transformations
- Autonomous navigation
- Task queue management
- Multi-point delivery
- Autonomous delivery systems
- Robot simulation and testing

---

# 👨‍💻 Project Developers

This project was collaboratively developed by:

## Harshvardhan Nayakal

**Contributions:**

- ROS2 development
- Autonomous navigation
- Nav2 integration
- Python development
- Delivery task management
- System integration
- Simulation and testing

## Sakshi Patil

**Contributions:**

- ROS2 robotics development
- Autonomous navigation
- Simulation and testing
- System integration
- Project development

Together, **Harshvardhan Nayakal and Sakshi Patil** developed the **ROS2 Autonomous Delivery Robot** as a collaborative robotics project.

---

# 👥 Authors

**Harshvardhan Nayakal**  
**Sakshi Patil**

---

# 📌 Project Information

| Category | Details |
|---|---|
| Project Name | ROS2 Autonomous Delivery Robot |
| Domain | Robotics and Autonomous Systems |
| Platform | ROS2 Humble |
| Robot | TurtleBot3 Burger |
| Simulation | Gazebo |
| Visualization | RViz2 |
| Navigation | Nav2 |
| Localization | AMCL |
| Programming | Python |
| Operating System | Ubuntu 22.04 |
| Project Type | Autonomous Mobile Robot Simulation |
| Developers | Harshvardhan Nayakal, Sakshi Patil |

---

# 📜 License

This project is released under the **MIT License**.

---

# ⭐ Acknowledgement

This project was developed for learning and practical implementation of autonomous mobile robotics using ROS2.

We acknowledge the open-source ROS2, Nav2, TurtleBot3, Gazebo, and RViz2 communities for providing the tools and frameworks used in this project.

---

# 🔗 GitHub Repository

**Repository Name:**

```text
ROS2-Autonomous-Delivery-Robot
```

**Repository Description:**

```text
ROS2-based autonomous delivery robot using TurtleBot3, Gazebo, RViz2, Nav2, AMCL, and Python for multi-point autonomous package delivery.
```

---

# 🤖 Project Domain

```text
Robotics
ROS2
Autonomous Mobile Robotics
Autonomous Navigation
Mobile Robot
Nav2
AMCL
Gazebo Simulation
RViz2
Industrial Automation
Smart Logistics
Autonomous Delivery
```

---

## ⭐ If you find this project useful, consider giving the repository a star!

Developed with dedication by:

**Harshvardhan Nayakal & Sakshi Patil**
