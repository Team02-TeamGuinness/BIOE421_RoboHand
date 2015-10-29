#File
fname = 'Test-z0.gcode'
f=open(fname,'w')

#Laser Parameters
laserPower     = 10 #% max power
dwellTime      = 7 #ms
x_start        = 414
y_start        = 343
z_start        = 125.25 #mm above home
pauseTime      = 500 #ms; time paused after movement before ablation
feedRate       = 500 #movement speed

# Rectangle size properties
rectLength     = 5 #mm; x-direction
rectWidth      = 5 #mm; y-direction
spaceSmall     = 3 #mm; space between rectangles
hexLength      = 0.500 #mm

#Other
relative       = 0 #0 for homing before beginning.  1 if machine has already been homed