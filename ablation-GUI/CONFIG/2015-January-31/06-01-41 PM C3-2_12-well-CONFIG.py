#File
fname = 'C3-2_12-well.gcode'
f=open(fname,'w')

#Laser Parameters
laserPower     = 15 #% max power
dwellTime      = 15 #ms
x_start        = 416
y_start        = 343
z_start        = 121.10 #mm above home
pauseTime      = 500 #ms; time paused after movement before ablation
feedRate       = 500 #movement speed

# Rectangle size properties
rectLength     = 23 #mm; x-direction
rectWidth      = 23 #mm; y-direction
spaceSmall     = 3 #mm; space between rectangles
hexLength      = 1.000 #mm

#Other
relative       = 0 #0 for homing before beginning.  1 if machine has already been homed