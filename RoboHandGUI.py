#Python code for the Robo-Hand GUI

#First import the tkinter modules from Python v.3

from tkinter import *
from tkinter import ttk

#Define your mainframe widget that codes for your main window and define its title and grid layout

root = Tk()
root.title("Robo-Hand Control Center")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

#Define the flexion, extension, and repetition entry boxes and place them within the main window's grid layout

Flexion = StringVar()
Extension = StringVar()
Repetition = StringVar()

Flexion_entry = ttk.Entry(mainframe, width=7, textvariable=Flexion)
Flexion_entry.grid(column=2, row=1, sticky=(W, E))

Extension_entry = ttk.Entry(mainframe, width=7, textvariable=Extension)
Extension_entry.grid(column=2, row=2, sticky=(W, E))

Repetition_entry = ttk.Entry(mainframe, width=7, textvariable=Repetition)
Repetition_entry.grid(column=2, row=3, sticky=(W, E))

#Define the labels for the previously defined user-input entry boxes

ttk.Label(mainframe, text="Flexion =").grid(column=1, row=1, sticky=E)
ttk.Label(mainframe, text="degrees").grid(column=3, row=1, sticky=W)

ttk.Label(mainframe, text="Extension =").grid(column=1, row=2, sticky=E)
ttk.Label(mainframe, text="degrees").grid(column=3, row=2, sticky=W)

ttk.Label(mainframe, text="Number of Repetitions =").grid(column=1, row=3, sticky=E)

#Define your button

ttk.Button(mainframe, text="JAPICA!").grid(column=3, row=4, sticky=(E, S))

#Shortcuts and running

for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)

Flexion_entry.focus()
Extension_entry.focus()
Repetition_entry.focus()

root.mainloop()



