#File
fname = '5D11_1ms_10x10mm.gcode'
f=open(fname,'w')

#Laser Parameters
laserPower     = 10 #% max power
dwellTime      = 1 #ms
x_start        = 400
y_start        = 327
z_start        = 122.60 #mm above home
pauseTime      = 500 #ms; time paused after movement before ablation
feedRate       = 500 #movement speed

# Rectangle size properties
rectLength     = 10 #mm; x-direction
rectWidth      = 10 #mm; y-direction
spaceSmall     = 3 #mm; space between rectangles
hexLength      = 0.250 #mm

#Other
relative       = 1 #0 for homing before beginning.  1 if machine has already been homed