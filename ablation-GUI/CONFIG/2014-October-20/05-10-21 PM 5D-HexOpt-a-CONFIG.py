#File
fname = '5D-HexOpt-a.gcode'
f=open(fname,'w')

#Laser Parameters
laserPower     = 20 #% max power
dwellTime      = 1 #ms
x_start        = 403
y_start        = 343
z_start        = 110.4 #mm above home
pauseTime      = 500 #ms; time paused after movement before ablation
feedRate       = 500 #movement speed

# Rectangle size properties
rectLength     = 5 #mm; x-direction
rectWidth      = 5 #mm; y-direction
spaceSmall     = 3 #mm; space between rectangles
hexLength      = 0.200 #mm

#Other
relative       = 0 #1 for no starting x,y; 0 for using starting co-ordinates