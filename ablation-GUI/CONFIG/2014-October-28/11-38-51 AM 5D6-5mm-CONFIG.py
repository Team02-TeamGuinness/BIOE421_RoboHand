#File
fname = '5D6-5mm.gcode'
f=open(fname,'w')

#Laser Parameters
laserPower     = 15 #% max power
dwellTime      = 3 #ms
x_start        = 404
y_start        = 343
z_start        = 123.8 #mm above home
pauseTime      = 500 #ms; time paused after movement before ablation
feedRate       = 500 #movement speed

# Rectangle size properties
rectLength     = 5 #mm; x-direction
rectWidth      = 5 #mm; y-direction
spaceSmall     = 3 #mm; space between rectangles
hexLength      = 0.500 #mm

#Other
relative       = 1 #0 for homing before beginning.  1 if machine has already been homed