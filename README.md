# 🚁 Autonomous Drone Navigation using A* and YOLOv8

## Overview

A simulation-based autonomous UAV navigation system that combines
A* path planning, occupancy-grid mapping, computer vision,
YOLOv8 object detection, and dynamic obstacle replanning.

The system enables a simulated drone to navigate from a starting
position to a target while avoiding static and dynamically detected
obstacles.

## System Architecture

Camera / Image
↓
YOLOv8 Object Detection
↓
Obstacle Bounding Boxes
↓
Occupancy Grid
↓
A* Path Planning
↓
Collision-Free Path
↓
Dynamic Replanning
↓
Simulated Drone

## Features

- A* path planning
- 2D occupancy-grid mapping
- Simulated UAV navigation
- Static obstacle avoidance
- Dynamic obstacle detection
- Automatic path replanning
- OpenCV-based obstacle detection
- YOLOv8 object detection
- YOLO-to-occupancy-grid conversion
- Collision-free path validation
- A* vs BFS comparison
- Navigation performance metrics

## Technologies

- Python
- NumPy
- Matplotlib
- OpenCV
- YOLOv8
- A* Search
- Breadth-First Search
- Occupancy Grid Mapping
- Google Colab

## Project Demo

The project demonstrates a simulated drone navigating through
an obstacle-filled environment and dynamically changing its
path when a new obstacle is detected.

## Future Improvements

- Real-time video input
- Improved obstacle inflation
- 3D environment simulation
- Real drone integration
- Real-time flight testing
- Advanced path-planning algorithms

## Author

Nikitha J
