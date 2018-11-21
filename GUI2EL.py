import tkinter as tk

root = tk.Tk()

#//widget1//
age = tk.Label(root, height = 5, width = 5, text = "Age:")
age.grid (row = 0, column = 0, sticky = "NESW")
#//widget2//
ageInput = tk.Entry(root, width = 5)
ageInput.grid (row=0, column =1)
#//widget3//
ageEnter = tk.Button(root, height = 1, width = 5, cursor = "hand1", text = "Enter")
ageEnter.grid (row=0, column =2)
#widget4//

add1 = tk.Button(root, height = 5, width = 5, cursor = "hand1", text = "Add")
add1.grid (row=2, column = 0, sticky = "NSEW")
add2 = tk.Button(root, height = 5, width = 5, cursor = "hand1", text = "Add")
add2.grid (row=2, column = 1, sticky = "NESW")
add3 = tk.Button(root, height = 5, width = 5, cursor = "hand1", text = "Add")
add3.grid (row=2, column = 2, sticky = "NESW")
root.mainloop()