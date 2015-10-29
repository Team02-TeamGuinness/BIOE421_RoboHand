#File
fname = '.gcode'
f=open(fname,'w')

#Laser Parameters
laserPower     = 17.5 #% max power
dwellTime      = 3 #ms
x_start        = 416
y_start        = 34`
z_start        = 122.10 #mm above home
pauseTime      =  #ms; time paused after movement before ablation
feedRate       = 500 #movement speed

# Rectangle size properties
rectLength     =  #mm; x-direction
rectWidth      =  #mm; y-direction
spaceSmall     = 3 #mm; space between rectangles
hexLength      = 0.300 #mm

#Other
relative       = 0 #0 for homing before beginning.  1 if machine has already been homed