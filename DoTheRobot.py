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

def currentXPos(x):

	global x_currentPos
	x_currentPos += x
	return x_currentPos

def guiGlobVars(kvarg):

	#File
	filename = kvarg['gcodeNameStr']
	global f
	f.close()
	f = open(filename,'w')

	#Flexion
	global flexion
	flexion = int(kvarg['flexion']

	#Extension
	global extension
	extension = int(kvarg['extension']

	#Repetitions
	global repetitions 
	repetitions = int(kvarg['repetitions']

#Write your Gcode

def writeGcode(kvarg):

	if (kvarg): guiGlobVars(kvarg)
	writefile.header(f)
	f.writelines("G28\n")
	f.writelines("G0 X" + str(flexion) + "\n")
	writefile.closefile(f)

def main():
	
	writeGcode()

if __name__ == '__main__': main()



	
