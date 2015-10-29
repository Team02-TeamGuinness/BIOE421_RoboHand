#File
fname = '5C1-test.gcode'
f=open(fname,'w')

#Laser Parameters
laserPower     = 25 #% max power
dwellTime      = 60 #ms
x_start        = 410
y_start        = 348
z_start        = 104.4 #mm above home
pauseTime      = 500 #ms; time paused after movement before ablation
feedRate       = 500 #movement speed

# Rectangle size properties
rectLength     = 10 #mm; x-direction
rectWidth      = 10 #mm; y-direction
spaceSmall     = 3 #mm; space between rectangles
hexLength      = 1.300 #mm

#Other
relative       = 0 #1 for no starting x,y; 0 for using starting co-ordinates