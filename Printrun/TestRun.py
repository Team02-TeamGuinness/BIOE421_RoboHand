from printrun.printcore import printcore
from printrun import gcoder

p = printcore('/dev/ttyACM1',115200)
gcode = [i.strip() for i in open('./Gcode/2015-November-18/01-16-38 AM Test1.gcode')]
#gcode = gcoder.LightGCode(gcode)
gcode = gcoder.LightGCode(["G0 X5"])
print gcode
print p
p.startprint(gcode)
#p.disconnect()
#p.send_now("G0 X5")

#import serial
#ser = serial.Serial('/dev/ttyACM1', 115200, timeout = 1)
#line = ser.readline()
#ser.close()
#print line
