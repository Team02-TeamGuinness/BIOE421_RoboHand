import config
import writefile
import math

## Parameters

#File
f = config.f

#Laser Parameters
laserPower 		= config.laserPower
dwellTime     	= config.dwellTime
x_start			= config.x_start
y_start			= config.y_start
z_start			= config.z_start
pauseTime 		= config.pauseTime
feedRate        = config.feedRate

# Rectangle size properties
rectLength 	= config.rectLength
rectWidth   = config.rectWidth
spaceSmall 	= config.spaceSmall
hex_pack	= config.hexLength

# Other Parameters
relative   	= config.relative
y_brush_top = 335
y_brush_dist = 80
x_brush = 232
cleanTrigger = config.cleanTrigger

x_current = x_start
y_current = y_start

def currentX(x):
	global x_current
	x_current += x
	return x_current
	
def currentY(y):
	global y_current
	y_current += y
	return y_current
	

def check_Conditions(laser, dwell, z):
	if len(laser) != len(dwell): return 0
	if len(laser) != len(z): return 0
	return len(laser)

def hex_pattern(hex_pack):
	global x_dist
	x_dist = float("{:.3f}".format(hex_pack))
	global y_dist
	y_dist = float("{:.3f}".format(hex_pack * (3**0.5) / 2))
	return
	
def formatFloat(fl):
	fl = float(fl)
	fl = float("{:.3f}".format(fl))
	return fl

def guiGlobVars(kvarg):
	#File
	filename = kvarg['gcodeNameStr']
	global f
	f.close()
	f = open(filename,'w')
	
	#Laser Parameters
	global laserPower
	laserPower 		= float(kvarg['laserStr'])
	global dwellTime
	dwellTime     	= int(kvarg['dwellStr'])
	global x_start
	x_start			= int(kvarg['xStr'])
	global y_start
	y_start			= int(kvarg['yStr'])
	global z_start
	z_start			= float(kvarg['zStr'])
	global pauseTime
	pauseTime 		= int(kvarg['pauseStr'])
	global feedRate
	feedRate        = int(kvarg['speedStr'])
	
	# Rectangle size properties
	global rectLength
	rectLength 	= int(kvarg['lengthStr'])
	global rectWidth
	rectWidth   = int(kvarg['widthStr'])
	global spaceSmall
	spaceSmall 	= int(kvarg['spaceStr'])
	global hex_pack
	hex_pack	= float(kvarg['hexPackStr'])
	
	hex_pattern(hex_pack)
	
	# Other Parameters
	global relative
	relative   	= int(kvarg['relStr'])	
	global cleanTrigger
	cleanTrigger= int(kvarg['cleanStr'])

def gcode_move(x_move, y_move):
	x_move = formatFloat(x_move)
	y_move = formatFloat(y_move)
	f.writelines("G0 X" + str(x_move) + " Y" + str(y_move) + " F1000\n")
	f.writelines("G4 P" + str(pauseTime) + "\n")
	currentX(x_move)
	currentY(y_move)

def cleanLaserHead():
	x_initial = formatFloat(currentX(0))
	y_initial = formatFloat(currentY(0))
	
	f.writelines("\n;; Cleaning\n\n")
	f.writelines("M3 S0\n")
	
	f.writelines("G90\n")
	f.writelines("G0 X" + str(x_brush) + " Y" + str(y_brush_top) + " F1000\n")
	f.writelines("G4 P250\n")
	f.writelines("G0 Y" + str(y_brush_top - y_brush_dist) + " F1000\n")
	f.writelines("G4 P250\n")
	f.writelines("G0 Y" + str(y_brush_top) + " F1000\n")
	f.writelines("G4 P250\n")
	f.writelines("G0 X" + str(x_initial) + " Y" + str(y_initial) + " F1000\n")
	f.writelines("G4 P500\n")
	f.writelines("G91\n")
	
	f.writelines(";; Done Cleaning\n\n")
	
	
def gcode_rectangle(dwellTime, laserPower):
	y_total = 0
	flag = -1
	pulseDist = formatFloat(1/x_dist)
	
	cleanCount = 0
	
	while y_total < rectWidth:
		f.writelines("G1 X" + str(-1*rectLength) + " S" + str(laserPower) + " L" + str(dwellTime*1000) + " P" + str(pulseDist) + " F" + str(feedRate) + " B1\n") 
		currentX(-1*rectLength)
		
		cleanCount += 1
		if cleanCount == cleanTrigger:
			cleanCount = 0 
			cleanLaserHead()
		
		x_overhang = flag * x_dist/2
		gcode_move(rectLength + x_overhang, -1*y_dist)
		
		y_total += y_dist
		flag *= -1	
	return 
	

def writeGCODE(kvarg):
	
	if (kvarg): guiGlobVars(kvarg)
	
	## Write GCODE file
	writefile.header(f)
	
	f.writelines("M3 S0\n") ## Laser Off
	
	if relative == 0: 
		f.writelines("G28\n") ## Home axes.
	else:
		f.writelines("G90\n")
		f.writelines("M3 S0\n") ## Laser Off
	f.writelines("G0 X" + str(x_start) + " Y" + str(y_start) + " F2000\n") # Move to x and y-axis start
	f.writelines("G0 Z" + str(z_start) + " F300\n") ##Move to z-axis position
	if relative == 1: 
		f.writelines("G91\n")
	
	x_current = currentX(0)
	y_current = currentY(0)
	currentX(-1*x_current+x_start)
	currentY(-1*y_current+y_start)
	
	## Print Square
	gcode_rectangle(dwellTime, laserPower)

	cleanLaserHead()	
	writefile.closefile(f)

def main():
	writeGCODE()

if __name__ == '__main__': main()
	
	
	
	




