#File
fname = '12.gcode'
f=open(fname,'w')

#Laser Parameters
laserPower     = 1 #% max power
dwellTime      = 2 #ms
x_start        = 6
y_start        = 7
z_start        = 121.10 #mm above home
pauseTime      = 10 #ms; time paused after movement before ablation
feedRate       = 4 #movement speed

# Rectangle size properties
rectLength     = 8 #mm; x-direction
rectWidth      = 9 #mm; y-direction
spaceSmall     = 3 #mm; space between rectangles
hexLength      = 5.000 #mm

#Other
relative       = 0 #0 for homing before beginning.  1 if machine has already been homed
cleanTrigger	= 11 #number of rows between laser head cleanings