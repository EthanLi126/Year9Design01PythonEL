import tkinter as tk

root = tk.Tk()

def change(*args):

	x = int(entry.get())
	print(x)
	slider.config(state = "normal")
	slider.set(x)
	slider.config(state = "disabled")
entry = tk.Entry(root)
entry.bind("<Return >",change)
entry.pack()
slider = tk.Scale(root, from_=0, to=200, orient=tk.HORIZONTAL)
slider.config(state = "disabled")
slider.pack()
root.mainloop()
