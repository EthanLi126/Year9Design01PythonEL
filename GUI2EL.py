import tkinter as tk

root = tk.Tk()
root.title("Hydration Tracker")
root.configure(background= "powderblue")

def water8(event):
	print("water8")

def waterC(event):
	print("waterC")
#//widget1//
age = tk.Label(root, height = 3, width = 5, text = "Age:")
age.configure(background="powderblue")
age.grid (row = 0, column = 0, sticky = "NESW" )
#//widget2//
ageInput = tk.Entry(root, width = 5)
ageInput.grid (row=0, column =1)
#//widget3//
ageEnter = tk.Button(root, height = 1, width = 5, cursor = "hand1", text = "Enter")
ageEnter.grid (row=0, column =2)
#//widget4//

add1 = tk.Button(root, height = 2, width = 5, cursor = "hand1", text = "Add")
add1.grid (row=2, column = 0, sticky = "NESW")
add1.bind(water8)
add2 = tk.Button(root, height = 2, width = 5, cursor = "hand1", text = "Add")
add2.grid (row=2, column = 1, sticky = "NESW")
add3 = tk.Button(root, height = 2, width = 5, cursor = "hand1", text = "Add")
add3.grid (row=2, column = 2, sticky = "NESW")
#//widget5//
under1 = tk.Label(root, height=2,width=5,text="8 oz")
under1.grid(row=3, column=0, rowspan = 2,sticky = "NESW")
under2 = tk.Entry(root,width=5)
under2.grid(row=4, column=1,sticky = "NESW")
under2label= tk.Label(root,height=2, width = 10,text="Custom Input (oz)")
under2label.grid(row=3,column=1,sticky="NESW",columnspan=2)
under3label= tk.Label(root,height=2, width=5,text="Custom Input (oz)")
#under3label.grid(row=3,column=2,sticky="NESW")
under3 = tk.Entry(root,width=5)
under3.grid(row=4, column=2,sticky = "NESW")
#//widget6##
display = tk.Canvas(root)

display.create_line(0,0,2,1)
display.grid(row=5,columnspan=3)
root.mainloop()