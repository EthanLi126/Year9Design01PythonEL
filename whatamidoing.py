import tkinter as tk 

root = tk.Tk()


def __init__(self,parent):

        self.button1=Tkinter.Button(self.frame,text="YES")
        self.button1.pack(side=BOTTOM)
        self.button1.bind("<Button-1>", self.button1Click)

        self.button2=Tkinter.Button(self.frame,text="NO")
        self.button2.pack()
        self.button2.bind("<Button-1>", self.button2Click)

def leftKey(event):
	print("hi")
	
	#bLind.grid(row=previous_row-1)
def rightKey(event):
	bLind.grid(row=previous_row+1)
def upKey(event):
	bLind.grid(row=previous_column+1)
def downKey(event):
	bLind.grid(row=previous_column-1)

bLind = tk.Label(root, height = 5, width = 5, text = "bLind")
bLind.bind('<Left>', leftKey)
bLind.bind('<Right>', rightKey)
bLind.bind('<Up>', upKey)
bLind.bind('<Down>', downKey)
bLind.grid (row = 5, column = 5, sticky = "NESW")

info = bLind.grid_info()
previous_row = int(info["row"])
previous_column = int(info["column"])








root.mainloop()