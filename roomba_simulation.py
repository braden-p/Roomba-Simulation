"""
Roomba Simulation
Created by Braden Piper, bradenpiper.com
Created on Thu Jan 5, 2023
Version = 1.1
------------------------------------------
DESCRIPTION:
A program capable of simulating one or multiple roomba vacuum robots cleaning a
rectangular room.

This program uses Object Oriented Programming to simulate:
    • A Rectangular Room
        - A room consisting of clean or dirty tiles
        - The room has a width and a height and contains (width * height) tiles.
        At any particular time, each of these tiles is either clean or dirty.
        - Initially, the entire floor is dirty. If a robot moves over a dirty
        tile, the tile becomes clean.
    • The Robots
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
    • Position
        - A location within a two-dimensional room, used to keep track of the
        location of the robots.
        - The position is represented using coordinates (x, y), which are floats
        satisfying 0 ≤ x < w and 0 ≤ y < h.

The program demonstrates two different methods of movement by the robot(s):
    (1) A Standard Movement Robot
        - This robot attempts to move in its current direction; when it would
        hit a wall, it instead chooses a new direction randomly.
    (2) A Random Walk Robot
        - This robot uses the "random walk" movement strategy: it
        chooses a new direction at random at the end of each time-step.

Termination
The simulation ends when a specified fraction of the tiles in the room have been cleaned.

A few lines of code at the bottom of this program can be uncommented to run the
program using whatever parameters you desire.
------------------------------------------
NOTE: This program was completed as part of the course MITx 6.00.2x - Introduction
to Computational Thinking and Data Science. The general framework, and some
of the functions were provided materials. The majority of the implementation is
my own work.
The provided materials include:
    Position class
    showPlot1 function
    showPlot 2 function
The other class names and function names were provided with docstrings, but the
implementations are my own.
"""
import math
import random

import ps2_visualize
import pylab

# Edit the number in the line below based on which version of Python you have
# for Python 3.5, the number should be 35
# for Python 3.6, the number should be 36
# for Python 3.10, the number should be 310 etc.
# This program will only work with Python versions 3.5 - 3.10

from verify_movement39 import testRobotMovement
# If you get a "Bad magic number" ImportError, you are not using the correct
# version of Python

class Position(object):
    """
    A Position represents a location in a two-dimensional room.
    """
    def __init__(self, x, y):
        """
        Initializes a position with coordinates (x, y).
        """
        self.x = x
        self.y = y
        
    def getX(self):
        return self.x
    
    def getY(self):
        return self.y
    
    def getNewPosition(self, angle, speed):
        """
        Computes and returns the new Position after a single clock-tick has
        passed, with this object as the current position, and with the
        specified angle and speed.

        Does NOT test whether the returned position fits inside the room.

        angle: number representing angle in degrees, 0 <= angle < 360
        speed: positive float representing speed

        Returns: a Position object representing the new position.
        """
        old_x, old_y = self.getX(), self.getY()
        angle = float(angle)
        # Compute the change in position
        delta_y = speed * math.cos(math.radians(angle))
        delta_x = speed * math.sin(math.radians(angle))
        # Add that to the existing position
        new_x = old_x + delta_x
        new_y = old_y + delta_y
        return Position(new_x, new_y)

    def __str__(self):  
        return "(%0.2f, %0.2f)" % (self.x, self.y)

class RectangularRoom(object):
    """
    A RectangularRoom represents a rectangular region containing clean or dirty
    tiles.

    A room has a width and a height and contains (width * height) tiles. At any
    particular time, each of these tiles is either clean or dirty.
    """
    def __init__(self, width, height):
        """
        Initializes a rectangular room with the specified width and height.

        Initially, no tiles in the room have been cleaned.

        width: an integer > 0
        height: an integer > 0
        """
        self.width = width
        self.height = height
        self.tiles = self.getNumTiles()
        self.cleanTiles = []
        self.numCleanTiles = self.getNumCleanedTiles()
        
    def getW(self):
        return self.width
    
    def getH(self):
        return self.height
        
    def __str__(self):
        return 'Rectangular Room: w:'+str(self.width)+' h:'+str(self.height)+' numTiles:'+str(self.tiles)+' cleanTiles:'+str(self.numCleanTiles)
        
    def cleanTileAtPosition(self, pos):
        """
        Mark the tile under the position POS as cleaned.

        Assumes that POS represents a valid position inside this room.

        pos: a Position
        """
        x = int(pos.getX())
        y = int(pos.getY())
        if self.isTileCleaned(x,y):
            pass
        else:
            self.cleanTiles.append((x,y))

    def isTileCleaned(self, m, n):
        """
        Return True if the tile (m, n) has been cleaned.

        Assumes that (m, n) represents a valid tile inside the room.

        m: an integer
        n: an integer
        returns: True if (m, n) is cleaned, False otherwise
        """
        if (m,n) in self.cleanTiles:
            return True
        else:
            return False
    
    def getNumTiles(self):
        """
        Return the total number of tiles in the room.

        returns: an integer
        """
        width = self.width
        height = self.height
        numTiles = width*height
        return numTiles

    def getNumCleanedTiles(self):
        """
        Return the total number of clean tiles in the room.

        returns: an integer
        """
        return len(self.cleanTiles)

    def getRandomPosition(self):
        """
        Return a random position inside the room.

        returns: a Position object.
        """
        x = random.uniform(0,self.getW())    
        y = random.uniform(0,self.getH()) 
        while x == self.getW() or y == self.getH():
            x = random.uniform(0,self.getW())    
            y = random.uniform(0,self.getH()) 
        randomPosition = Position(x,y)
        return randomPosition

    def isPositionInRoom(self, pos):
        """
        Return True if pos is inside the room.

        pos: a Position object.
        returns: True if pos is in the room, False otherwise.
        """
        x = pos.getX()
        y = pos.getY()
        if x >= 0 and x < self.getW() and y >= 0 and y < self.getH():
            return True
        else:
            return False

class Robot(object):
    """
    Represents a robot cleaning a particular room.

    At all times the robot has a particular position and direction in the room.
    The robot also has a fixed speed.

    Subclasses of Robot should provide movement strategies by implementing
    updatePositionAndClean(), which simulates a single time-step.
    """
    def __init__(self, room, speed):
        """
        Initializes a Robot with the given speed in the specified room. The
        robot initially has a random direction and a random position in the
        room. The robot cleans the tile it is on.

        room:  a RectangularRoom object.
        speed: a float (speed > 0)
        """
        self.speed = speed   
        self.position = room.getRandomPosition()
        self.direction = random.randrange(360)
        self.room = room
        self.room.cleanTileAtPosition(self.position)
        
    def __str__(self):
        return 'Robot with speed:'+str(self.speed)+' position:'+str(self.position)+' direction:'+str(self.direction)

    def getRobotPosition(self):
        """
        Return the position of the robot.

        returns: a Position object giving the robot's position.
        """
        return self.position
    
    def getRobotDirection(self):
        """
        Return the direction of the robot.

        returns: an integer d giving the direction of the robot as an angle in
        degrees, 0 <= d < 360.
        """
        return self.direction

    def setRobotPosition(self, position):
        """
        Set the position of the robot to POSITION.

        position: a Position object.
        """
        self.position = position

    def setRobotDirection(self, direction):
        """
        Set the direction of the robot to DIRECTION.

        direction: integer representing an angle in degrees
        """
        self.direction = direction

    def updatePositionAndClean(self):
        """
        Simulate the passage of a single time-step.

        Move the robot to a new position and mark the tile it is on as having
        been cleaned.
        """
        raise NotImplementedError # don't change this!


class StandardRobot(Robot):
    """
    A StandardRobot is a Robot with the standard movement strategy.

    At each time-step, a StandardRobot attempts to move in its current
    direction; when it would hit a wall, it *instead* chooses a new direction
    randomly.
    """
    def updatePositionAndClean(self):
        """
        Simulate the passage of a single time-step.

        Move the robot to a new position and mark the tile it is on as having
        been cleaned.
        """
        currentPosition = self.getRobotPosition()
        newPosition = currentPosition.getNewPosition(self.getRobotDirection(),self.speed)
        if self.room.isPositionInRoom(newPosition):
           self.setRobotPosition(newPosition)
           self.room.cleanTileAtPosition(newPosition)
        else:
           self.setRobotDirection(random.randrange(360))


def runSimulation(num_robots, speed, width, height, min_coverage, num_trials,
                  robot_type):
    """
    Runs NUM_TRIALS trials of the simulation and returns the mean number of
    time-steps needed to clean the fraction MIN_COVERAGE of the room.

    The simulation is run with NUM_ROBOTS robots of type ROBOT_TYPE, each with
    speed SPEED, in a room of dimensions WIDTH x HEIGHT.

    num_robots: an int (num_robots > 0)
    speed: a float (speed > 0)
    width: an int (width > 0)
    height: an int (height > 0)
    min_coverage: a float (0 <= min_coverage <= 1.0)
    num_trials: an int (num_trials > 0)
    robot_type: class of robot to be instantiated (e.g. StandardRobot or
                RandomWalkRobot)
    
    If you wish to watch a visualization of each simulation, uncomment the three
    lines that contain anim
    """
    results = []
    robots = []
    for trial in range(num_trials): # for each trial
        print('Starting trial',trial+1)
        #anim = ps2_visualize.RobotVisualization(num_robots, width, height)
        numSteps = 0
        robotCount = 0
        room1 = RectangularRoom(width, height)
        for num in range(num_robots):  # initialize the correct number of robots
            robotCount += 1
            #print('initializing robot',robotCount)
            robots.append(robot_type(room1,speed))
        cleanTileGoal = room1.getNumTiles() * min_coverage  # set clean tile goal
        print('Cleaning',cleanTileGoal,'tiles')
        while room1.getNumCleanedTiles() < cleanTileGoal:  # while clean tile goal is not met:
            numSteps += 1
            for robot in robots:   # for each robot in the list robots:
                #anim.update(room1, robots)
                robot.updatePositionAndClean()  # updatePositionAndClean
        results.append(numSteps)
        print('Trial',trial+1,'complete.')
        print('Total number of steps:',numSteps)
    #anim.done()
    sumResults = sum(results)
    print('Results:',results)
    print('Sum of Results:',sumResults)
    meanResults = sumResults /num_trials
    print('Mean of Results:',meanResults)
    return meanResults


# === Problem 5
class RandomWalkRobot(Robot):
    """
    A RandomWalkRobot is a robot with the "random walk" movement strategy: it
    chooses a new direction at random at the end of each time-step.
    """
    def updatePositionAndClean(self):
        """
        Simulate the passage of a single time-step.

        Move the robot to a new position and mark the tile it is on as having
        been cleaned.
        """
        self.setRobotDirection(random.randrange(360))   # change direction
        currentPosition = self.getRobotPosition()
        newPosition = currentPosition.getNewPosition(self.getRobotDirection(),self.speed)   # find new position
        if self.room.isPositionInRoom(newPosition):   # check if new position is in room
           self.setRobotPosition(newPosition)   # move robot to new position
           self.room.cleanTileAtPosition(newPosition)   # clean tile at new position
        else:
           self.setRobotDirection(random.randrange(360))   # find a new direction


def showPlot1(title, x_label, y_label):
    """
    Runs 400 trials, 200 using StandardRobot, and 200 using RandomWalkRobot.
    In each trial, the robot(s) clean(s) 80% of a 20x20 room.
    The trials are run in groups of twenty. Each group of twenty trials is run
    ten times, the first group using only 1 robot, the second using 2 robots,
    and so on, until the final group which uses 10 robots.
    After running all trials, it plots the results of the trials, with time-steps
    on the y-axis, and number of robots on the x-axis.
    """
    num_robot_range = range(1, 11)
    times1 = []
    times2 = []
    for num_robots in num_robot_range:
        print("Plotting", num_robots, "robots...")
        times1.append(runSimulation(num_robots, 1.0, 20, 20, 0.8, 20, StandardRobot))
        times2.append(runSimulation(num_robots, 1.0, 20, 20, 0.8, 20, RandomWalkRobot))
    pylab.plot(num_robot_range, times1)
    pylab.plot(num_robot_range, times2)
    pylab.title(title)
    pylab.legend(('StandardRobot', 'RandomWalkRobot'))
    pylab.xlabel(x_label)
    pylab.ylabel(y_label)
    pylab.show()

    
def showPlot2(title, x_label, y_label):
    """
    What information does the plot produced by this function tell you?
    """
    aspect_ratios = []
    times1 = []
    times2 = []
    for width in [10, 20, 25, 50]:
        height = 300//width
        print("Plotting cleaning time for a room of width:", width, "by height:", height)
        aspect_ratios.append(float(width) / height)
        times1.append(runSimulation(2, 1.0, width, height, 0.8, 200, StandardRobot))
        times2.append(runSimulation(2, 1.0, width, height, 0.8, 200, RandomWalkRobot))
    pylab.plot(aspect_ratios, times1)
    pylab.plot(aspect_ratios, times2)
    pylab.title(title)
    pylab.legend(('StandardRobot', 'RandomWalkRobot'))
    pylab.xlabel(x_label)
    pylab.ylabel(y_label)
    pylab.show()
    


# Uncomment this line to see a visualization of StandardRobot cleaning a 5x5 room
##testRobotMovement(StandardRobot, RectangularRoom)

# Uncomment this line to run the robot cleaning simulation and see the average
# time a robot takes to clean the room. As a reminder
# these are the paramaters of runSimulation:
# (number of robots, width of room, height of room, minimum required cleaning coverage, number of trials, robot type)
##print(runSimulation(1, 1.0, 10, 10, 0.75, 50, StandardRobot))

#Uncomment this line to run the simulation with a RandomWalkRobot
# print(runSimulation(1, 1.0, 5, 5, 1.0, 50, RandomWalkRobot))

# Uncomment this line to run the showPlot1 function
##showPlot1('Time It Takes 1-10 Robots to clean 80% of a Room', 'Number of Robots', 'Time Steps')

showPlot2('Time it takes two robots to clean 80% of variously shaped rooms', 'Aspect Ratio', 'Time-Steps')