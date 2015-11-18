#Python code for the Robo-Hand GUI

#First import the tkinter modules from Python v.3

from Tkinter import *
from ttk import * 
from time import strftime, localtime
import os
from printrun.printcore import printcore
from printrun import gcoder



PULLEYCIRC = 39.9925 #mm/rev (calculated using the pulley pitch diameter)
MOTORSTEPANGLE = 5. #steps/mm

#Define your date

def dateName():

	dateStr = strftime("%Y-%B-%d", localtime())
	return dateStr

#Define you time

def timeName():
	timeStr = strftime("%I-%M-%S %p", localtime())
	return timeStr

#Initialize your directory for storing your final Gcode

def initGcodeDir(filename):

	dateStr = dateName()
	timeStr = timeName()
	dirPath = "./Gcode/{0}".format(dateStr)
	if not os.path.exists(dirPath): os.makedirs(dirPath)
	filepath = "{0}/{1} {2}".format(dirPath,timeStr,filename)
	return filepath

#Write your Gcode file using the inputs from the GUI

def writeGcode(*args):

	if flexion.get() > 80 or extension.get() > 80:
		raise Exception("You Done Messed Up")
	path = initGcodeDir(filename.get())
	configParam = {
			"filenameStr": path,
			"flexionStr": str(round((float(flexion.get())/360.)*(PULLEYCIRC)*(MOTORSTEPANGLE),3)),
			"extensionStr": str(extension.get()),
			"repetitionStr": str(repetition.get())
			}

	try:
		f = open(configParam["filenameStr"] + ".gcode",'w')
	except:
		print("Error - Open")
		error.set("Cannot open" + configParam["filenameStr"] + ".gcode")

	header = (
			";********File Info********\n"
			";filename = {0}\n"
			";flexion = {1} degrees\n"
			";extension = {2} degrees\n"
			";repetitions = {3}\n" 
			";********Robo-Hand Run Parameters Gcode Commands********\n"
			"G92 X0\n").format(configParam["filenameStr"],
				configParam["flexionStr"],
				configParam["extensionStr"],
				configParam["repetitionStr"])
	body = ""
	for i in range(repetition.get()):
		if (flexion.get()):
			body += "G0 X{0}\n".format(configParam["flexionStr"])
			body += "G4 P500\n"
			body += "G0 X-{0}\n".format(configParam["flexionStr"])
			body += "G4 P500\n"
		if (extension.get()):
			body += "G0 X-{0}\n".format(configParam["extensionStr"])
			body += "G4 P500\n"
			body += "G0 X{0}\n".format(configParam["extensionStr"])
			body += "G4 P500\n"			

	f.writelines(header+body)
	f.close()

	#Send your generated Gcode directly to the printer

	p = printcore('/dev/ttyACM0',115200)
	gcode = [i.strip() for i in open(path + '.gcode')]
	gcode = gcoder.LightGCode(gcode)
	p.startprint(gcode)

#Define your mainframe widget that codes for your main window and define its title and grid layout

root = Tk()
root.title("Robo-Hand Control Center")

mainframe = Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

#Define the flexion, extension, and repetition entry boxes and place them within the main window's grid layout

flexion = IntVar()
extension = IntVar()
repetition = IntVar()
filename = StringVar()

flexion_entry = Entry(mainframe, width=7, textvariable=flexion)
flexion_entry.grid(column=2, row=1, sticky=(W, E))

extension_entry = Entry(mainframe, width=7, textvariable=extension)
extension_entry.grid(column=2, row=2, sticky=(W, E))

repetition_entry = Entry(mainframe, width=7, textvariable=repetition)
repetition_entry.grid(column=2, row=3, sticky=(W, E))

filename_entry = Entry(mainframe, width=7, textvariable=filename)
filename_entry.grid(column=2, row=4, sticky=(W, E))

#Define the labels for the previously defined user-input entry boxes

Label(mainframe, text="Flexion =").grid(column=1, row=1, sticky=E)
Label(mainframe, text="degrees").grid(column=3, row=1, sticky=W)

Label(mainframe, text="Extension =").grid(column=1, row=2, sticky=E)
Label(mainframe, text="degrees").grid(column=3, row=2, sticky=W)

Label(mainframe, text="Number of Repetitions =").grid(column=1, row=3, sticky=E)

Label(mainframe, text="Filename").grid(column=1, row=4, sticky=E)

#Define your button to go

Button(mainframe, text="JAPICA!",command=writeGcode).grid(column=3, row=4, sticky=(E, S))

#Shortcuts and running

for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)

flexion_entry.focus()
extension_entry.focus()
repetition_entry.focus()
filename_entry.focus()

root.mainloop()


