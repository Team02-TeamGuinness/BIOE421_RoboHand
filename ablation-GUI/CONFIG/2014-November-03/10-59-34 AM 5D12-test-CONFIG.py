#File
fname = '5D12-test.gcode'
f=open(fname,'w')

#Laser Parameters
laserPower     = 10 #% max power
dwellTime      = 5 #ms
x_start        = 406
y_start        = 343
z_start        = 122.60 #mm above home
pauseTime      = 500 #ms; time paused after movement before ablation
feedRate       = 500 #movement speed

# Rectangle size properties
rectLength     = 5 #mm; x-direction
rectWidth      = 5 #mm; y-direction
spaceSmall     = 3 #mm; space between rectangles
hexLength      = 0.500 #mm

#Other
relative       = 1 #0 for homing before beginning.  1 if machine has already been homed