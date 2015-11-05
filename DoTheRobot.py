#Python script to take inputs from the RoboHandGUI and convert those inputs into a Gcode

import config
import writefile
import math

#Load the config file with use inputs

f = config.f

#Define the user inputs from the config file

flexion = config.flexion
extension = config.extension
repetitions = config.repetitions

#Define your global variables
