import tkinter as tk
from tkinter import messagebox
root = tk.Tk()
root.title("Hydration Tracker")
root.configure(background= "powderblue")



WaterAmount= [0]
WaterNeed = [0]

def reset():
	WaterAmount[0]=0
	WaterNeed[0]=0
	x=0
	slider.config(state = "normal")
	slider.set(x)
	slider.config(state = "disabled")
	amountof.set(str(WaterAmount[0])+" oz/"+str(WaterNeed[0])+" oz")
#age algorithm
def addwater():

	#print("***************")
	try:
		value=int(ageInput.get())
	except ValueError:
		messagebox.showerror("Please Enter An Integer", "That's Not an Integer.")
		ageInput.delete(0,'end')

	ageof=int(ageInput.get())
	print(ageof)
	if 4 <=ageof <=8 : 
		WaterNeed[0]=40
		print(WaterNeed[0])
		ageInput.delete(0,'end')
	elif 9 <=ageof <=13 :
		WaterNeed[0]=64
		print(WaterNeed[0])
		ageInput.delete(0,'end')
	elif 14 <=ageof <=18 : 
		WaterNeed[0]=88
		print(WaterNeed[0])
		ageInput.delete(0,'end')
	elif 19 <=ageof <=163 : 
		WaterNeed[0]=104
		print(WaterNeed[0])
		ageInput.delete(0,'end')
	elif 19 <=ageof <=163 : 
		WaterNeed[0]=72
		print(WaterNeed[0])
		ageInput.delete(0,'end')
	elif ageof<=3:
		messagebox.showerror("Error","This Program Cannot Calaculate The Amount Of Water Needed For Children Under 4")
		ageInput.delete(0,'end')
	elif ageof>=164:
		messagebox.showerror("You Aren't that old", "The Guinness World Record is 164 Years Old. ")
		ageInput.delete(0,'end')
	amountof.set(str(WaterAmount[0])+" oz/"+str(WaterNeed[0])+" oz")

def water8():
	print("water8")
	WaterAmount[0]=WaterAmount[0]+8
	print(WaterAmount[0])
	amountof.set(str(WaterAmount[0])+" oz/"+str(WaterNeed[0])+" oz")
def waterC1():
	print("waterC1")
	try:
		value=int(under2.get())
	except ValueError:
		messagebox.showerror("Please Enter An Integer", "That's Not an Integer.")
		under2.delete(0,'end')

	WaterAmount[0]=(int(under2.get()))+WaterAmount[0]
	under2.delete(0,'end')
	print (WaterAmount[0])
	amountof.set(str(WaterAmount[0])+" oz/"+str(WaterNeed[0])+" oz")
def waterC2():
	print("waterC2")
	try:
		value=int(under3.get())
	except ValueError:
		messagebox.showerror("Please Enter An Integer", "That's Not an Integer.")
		under3.delete(0,'end')
	WaterAmount[0]=(int(under3.get()))+WaterAmount[0]
	under3.delete(0,'end')
	print (WaterAmount[0])
	amountof.set(str(WaterAmount[0])+" oz/"+str(WaterNeed[0])+" oz")


	
def setslider():
	print("sliderset")
	if int(WaterNeed[0])==0:
		messagebox.showerror("Error","Please Enter Your Age")
		WaterAmount[0]==0
	else:
		getnumber=int(WaterAmount[0])/int(WaterNeed[0])
		x=getnumber*100
		print(x)
		slider.config(state = "normal")
		slider.set(x)
		slider.config(state = "disabled")







root.grid_columnconfigure(1,weight=3)
root.grid_columnconfigure(3,weight=3)


amountof = tk.StringVar()
amountof.set(str(WaterAmount[0])+" oz/"+str(WaterNeed[0])+" oz")

#//widget1//
age = tk.Label(root, height = 3, width = 8, text = "Age:")
age.configure(background="powderblue")
age.grid (row = 0, column = 0,  )
#//widget2//
ageInput = tk.Entry(root, width = 8)
ageInput.grid (row=0, column =2)
#//widget3//
ageEnter = tk.Button(root, height = 1, width = 8, cursor = "hand1", text = "Enter", command=addwater)
ageEnter.grid (row=0, column =4)
#//widget4//

add1 = tk.Button(root, height = 2, width = 8, cursor = "hand1", text = "Add", command = lambda:[water8(),setslider()])
add1.grid (row=2, column = 0, )
add2 = tk.Button(root, height = 2, width = 8, cursor = "hand1", text = "Add", command = lambda:[waterC1(),setslider()])
add2.grid (row=2, column = 2, )
add3 = tk.Button(root, height = 2, width = 8, cursor = "hand1", text = "Add", command = lambda:[waterC2(),setslider()])
add3.grid (row=2, column = 4, )
#//widget8//


under1 = tk.Label(root, height=2,width=8,text="8 oz",background="powderblue")
under1.grid(row=3, column=0,)
under1b = tk.Label(root, height=2,width=8,text="(1 Glass)",background="powderblue")
under1b.grid(row=4, column=0,columnspan=2,)
under2 = tk.Entry(root,width=8)
under2.grid(row=4, column=2,)
under3 = tk.Entry(root,width=8)
under3.grid(row=4, column=4,)

under2label= tk.Label(root,height=2, width = 10,text="\u2193Custom Input (oz)\u2193",background="powderblue")
under2label.grid(row=3,column=2,sticky="NESW",columnspan=4)
#//Widget6$$
spacelabel=tk.Label(root,background="powderblue",text="You Are:")
spacelabel.grid(row=5,column=2,)
#//widget7##

#//widget8#
drank = tk.Label(root, background="powderblue", height=2, text="You Have Drank:")
drank.grid(row=8,column=1,columnspan=3)
#//widget9//
amountdrank = tk.Label(root,background="powderblue",textvariable=amountof)
amountdrank.grid(row=9,column=1, columnspan=3)

slider = tk.Scale(root, from_=0, to=100, orient=tk.HORIZONTAL)
slider.config(state = "disabled")
slider.grid(row=6, column=1, columnspan=3)



#//widget10//

hydrated=tk.Label(root,width=30,background="powderblue", text="(0 = Dehydrated, 100 = Hydrated)")
hydrated.grid(row=7,column=0,columnspan=5)
#//widget11//

resetbutton=tk.Button(root,width=8,command=reset,text=("Reset All"))
resetbutton.grid(row=10,column=2)
root.mainloop()