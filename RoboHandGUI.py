#Python code for the Robo-Hand GUI

#First import the tkinter modules from Python v.3

from tkinter import *
from tkinter import ttk
from time import strftime, localtime
import os

#Define your date

def dateName():

	dateStr = strftime("%Y-%B-%d", localtime())
	return dateStr

#Define you time

def timeName():

	timeStr = strftime("%I-%M-%S %p", localtime())

#Initialize your directory for storing your final Gcode

def initGcodeDir(filename):

	dateStr = dateName()
	timeStr = timeName()

	dirPath = "./Gcode/{0}".format(dateStr)
	if not os.path.exists(dirPath): os.makedirs(dirPath)
	filepath = "{0}/{1} {2}".format(dirPath,timeStr,filename)
	return filePath

#Write your config file using the inputs from the GUI

def writeConfig(*args):

	configParam = {
			"filenameStr": str("Test"), #filename.get()),
			"gcodenameStr": str("Test") + ".gcode", #filename.get()) + ".gcode",
			"flexionStr": str(flexion.get()),
			"extensionStr": str(extension.get()),
			"repetitionStr": str(repetition.get())
			}

	try:
		f = open("config.py",'w')
	except:
		print("Error - Open")
		error.set("Cannot open config.py")

	filetext = (
			"#File Info\n"
			"fname = '{0}'\n"
			"f = open(fname,'w')\n\n"
			"#Robo-Hand Run Parameters\n"
			"flexion = {1} #degrees\n"
			"extension = {2} #degrees\n"
			"repetitions = {3}\n"
			).format(configParam["gcodenameStr"],
			configParam["flexionStr"],
			configParam["extensionStr"],
			configParam["repetitionStr"]
			)

	f.writelines(filetext)
	f.close()

#Use your config file to call your separate program to actually write the Gcode file

#def configure(*args):

#	configParam = writeConfig(args)
#	import pulse
	

			


#Define your mainframe widget that codes for your main window and define its title and grid layout

root = Tk()
root.title("Robo-Hand Control Center")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

#Define the flexion, extension, and repetition entry boxes and place them within the main window's grid layout

flexion = StringVar()
extension = StringVar()
repetition = StringVar()

flexion_entry = ttk.Entry(mainframe, width=7, textvariable=flexion)
flexion_entry.grid(column=2, row=1, sticky=(W, E))

extension_entry = ttk.Entry(mainframe, width=7, textvariable=extension)
extension_entry.grid(column=2, row=2, sticky=(W, E))

repetition_entry = ttk.Entry(mainframe, width=7, textvariable=repetition)
repetition_entry.grid(column=2, row=3, sticky=(W, E))

#Define the labels for the previously defined user-input entry boxes

ttk.Label(mainframe, text="Flexion =").grid(column=1, row=1, sticky=E)
ttk.Label(mainframe, text="degrees").grid(column=3, row=1, sticky=W)

ttk.Label(mainframe, text="Extension =").grid(column=1, row=2, sticky=E)
ttk.Label(mainframe, text="degrees").grid(column=3, row=2, sticky=W)

ttk.Label(mainframe, text="Number of Repetitions =").grid(column=1, row=3, sticky=E)

#Define your button

ttk.Button(mainframe, text="JAPICA!",command=writeConfig).grid(column=3, row=4, sticky=(E, S))

#Shortcuts and running

for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)

flexion_entry.focus()
extension_entry.focus()
repetition_entry.focus()

root.mainloop()



