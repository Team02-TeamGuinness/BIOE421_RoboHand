#File
fname = 'C3-1.gcode'
f=open(fname,'w')

#Laser Parameters
laserPower     = 20 #% max power
dwellTime      = 25 #ms
x_start        = 416
y_start        = 343
z_start        = 123.10 #mm above home
pauseTime      = 500 #ms; time paused after movement before ablation
feedRate       = 500 #movement speed

# Rectangle size properties
rectLength     = 10 #mm; x-direction
rectWidth      = 10 #mm; y-direction
spaceSmall     = 3 #mm; space between rectangles
hexLength      = 0.700 #mm

#Other
relative       = 0 #0 for homing before beginning.  1 if machine has already been homed