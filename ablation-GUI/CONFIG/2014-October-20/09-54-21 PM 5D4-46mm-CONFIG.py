#File
fname = '5D4-46mm.gcode'
f=open(fname,'w')

#Laser Parameters
laserPower     = 10 #% max power
dwellTime      = 2 #ms
x_start        = 410
y_start        = 348
z_start        = 110.4 #mm above home
pauseTime      = 500 #ms; time paused after movement before ablation
feedRate       = 500 #movement speed

# Rectangle size properties
rectLength     = 46 #mm; x-direction
rectWidth      = 46 #mm; y-direction
spaceSmall     = 3 #mm; space between rectangles
hexLength      = 0.170 #mm

#Other
relative       = 0 #1 for no starting x,y; 0 for using starting co-ordinates