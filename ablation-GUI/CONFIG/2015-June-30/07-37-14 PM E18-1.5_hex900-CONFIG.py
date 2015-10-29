#File
fname = 'E18-1.5_hex900.gcode'
f=open(fname,'w')

#Laser Parameters
laserPower     = 20 #% max power
dwellTime      = 20 #ms
x_start        = 411
y_start        = 335
z_start        = 120.10 #mm above home
pauseTime      = 500 #ms; time paused after movement before ablation
feedRate       = 500 #movement speed

# Rectangle size properties
rectLength     = 5 #mm; x-direction
rectWidth      = 5 #mm; y-direction
spaceSmall     = 3 #mm; space between rectangles
hexLength      = 0.900 #mm

#Other
relative       = 1 #0 for homing before beginning.  1 if machine has already been homed