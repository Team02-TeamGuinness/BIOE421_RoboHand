#File
fname = 'E23.3-600_12-well.gcode'
f=open(fname,'w')

#Laser Parameters
laserPower     = 40 #% max power
dwellTime      = 25 #ms
x_start        = 415
y_start        = 341
z_start        = 119.10 #mm above home
pauseTime      = 500 #ms; time paused after movement before ablation
feedRate       = 200 #movement speed

# Rectangle size properties
rectLength     = 46 #mm; x-direction
rectWidth      = 46 #mm; y-direction
spaceSmall     = 3 #mm; space between rectangles
hexLength      = 0.860 #mm

#Other
relative       = 0 #0 for homing before beginning.  1 if machine has already been homed