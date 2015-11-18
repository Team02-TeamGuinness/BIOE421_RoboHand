from printrun.printcore import printcore
from printrun import gcoder

p = printcore('/dev/ttyACM0',115200)
gcode = [i.strip() for i in open('./Gcode/2015-November-18/01-16-38 AM Test1.gcode')]
gcode = gcoder.LightGCode(gcode)
p.startprint(gcode)

#p = printcore('/dev/ttyACM0',115200)
#gcode = [i.strip() for i in open('./Gcode/2015-November-18/01-16-38 AM Test1.gcode')
#gcode = gcoder.LightGCode(gcode)
#p.startprint(gcode)
