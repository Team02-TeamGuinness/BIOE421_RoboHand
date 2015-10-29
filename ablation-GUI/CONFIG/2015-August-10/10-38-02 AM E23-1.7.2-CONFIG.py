#File
fname = 'E23-1.7.2.gcode'
f=open(fname,'w')

#Laser Parameters
laserPower     = 40 #% max power
dwellTime      = 100 #ms
x_start        = 405
y_start        = 333
z_start        = 115.10 #mm above home
pauseTime      = 500 #ms; time paused after movement before ablation
feedRate       = 100 #movement speed

# Rectangle size properties
rectLength     = 10 #mm; x-direction
rectWidth      = 10 #mm; y-direction
spaceSmall     = 3 #mm; space between rectangles
hexLength      = 1.400 #mm

#Other
relative       = 1 #0 for homing before beginning.  1 if machine has already been homed