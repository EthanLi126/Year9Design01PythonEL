#this imports the tkintrer "tool box" this contains
#all the suppor material to make GUI elements.
#by including "as tk" we are giving a short name to use.

import tkinter as tk

# main window

root = tk.Tk() #creates the standard main window.

# / / widget1 / /
#Three stages to build eleents/objects
#1. Construct the object:  We build and configure it.
#2. Configure the Object:  We specify behaviours and settings (OPTIONAL)
#3. Pack the Object: Put it in the window
output = tk.Text(root,height = 10, width = 30)
#ordered parameters: The order we send them matters. (COMMON)
#named paramters: Javascript and python specific
output.config(state = "disable", background = "red")
output.grid(row = 0, column = 0, rowspan = 5)


# / / widget2 / /

labInput1 = tk.Label(root, text = "Input 1")
labInput1.grid(row = 5, column = 0)

labInput2 = tk.Label(root, text = "Input 2")
labInput2.grid(row = 6, column = 0)

labInput3 = tk.Label(root, text = "Input 3")
labInput3.grid(row = 7, column = 0)

# / / widget3 / /
#How do I track the checkbox state.
var1=tk.IntVar()
var2=tk.IntVar()

#What the named variable does is binds the invar to the
#checkbox. If there is a change in the box, there is a change in the variable. 
#This is called BINDING

cHC = tk.Checkbutton(root, text="Expand", variable = var1)
cHC.grid(row=0,column=1)
cLF = tk.Checkbutton(root, text="Expand", variable =var2)
cLF.grid(row=1 ,column=1)

#We are writing an EVENT DRIVE PROGRAM
#Build the GUI
#Start it running
#Wait for "Event"
root.mainloop() #starts the program