# Roomba Simulation
#### Created by Braden Piper, bradenpiper.com
#### Created on Thu Jan 5, 2023
#### Version = 1.1
---
## DESCRIPTION
This program uses Object Oriented Programming to simulate:
* A Rectangular Room
    - A room consisting of clean or dirty tiles
    - The room has a width and a height and contains (width * height) tiles.
    At any particular time, each of these tiles is either clean or dirty.
    - Initially, the entire floor is dirty. If a robot moves over a dirty
    tile, the tile becomes clean.
* The Robots
    - for the purposes of this program, the robots are points, and can pass
    through each other or occupy the same point without interfering.
    - At all times a robot has a particular position and direction in the room.
    A robot also has a fixed speed.
    - A robot may not move to a point outside of the room.
    - A robot has a direction of motion represented by an integer d
    satisfying 0 ≤ d < 360, which gives an angle in degrees.
    - All robots move at the same speed s, a float, which is given and is
    constant throughout the simulation. Every time-step, a robot moves in
    its direction of motion by s units.
    - If a robot detects that it will hit the wall within the time-step,
    that time step is instead spent picking a new direction at random. The
    robot will attempt to move in that direction on the next time step,
    until it reaches another wall.
* Position
    - A location within a two-dimensional room, used to keep track of the
    location of the robots.
    - The position is represented using coordinates (x, y), which are floats
    satisfying 0 ≤ x < w and 0 ≤ y < h.

The program demonstrates two different methods of movement by the robot(s):
1. A Standard Movement Robot
    - This robot attempts to move in its current direction; when it would
    hit a wall, it instead chooses a new direction randomly.
2. A Random Walk Robot
    - This robot uses the "random walk" movement strategy: it
    chooses a new direction at random at the end of each time-step.

The simulation ends when a specified fraction of the tiles in the room have been cleaned.

A few lines of code at the bottom of this program can be uncommented to run the
program using whatever parameters you desire.
---
##### NOTE:
This program was completed as part of the course MITx 6.00.2x - Introduction
to Computational Thinking and Data Science. The general framework, and some
of the functions were provided materials. The majority of the implementation is
my own work.
The provided materials include:
    Position class
    showPlot1 function
    showPlot 2 function
The other class names and function names were provided with docstrings, but the
implementations are my own.