#File
fname = 'S10_L3000_z1.5_hx250.gcode'
f=open(fname,'w')

#Laser Parameters
laserPower     = 10 #% max power
dwellTime      = 3 #ms
x_start        = 421
y_start        = 345
z_start        = 122.60 #mm above home
pauseTime      = 500 #ms; time paused after movement before ablation
feedRate       = 500 #movement speed

# Rectangle size properties
rectLength     = 46 #mm; x-direction
rectWidth      = 23 #mm; y-direction
spaceSmall     = 3 #mm; space between rectangles
hexLength      = 0.250 #mm

#Other
relative       = 0 #0 for homing before beginning.  1 if machine has already been homed