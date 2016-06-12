from Tkinter import *
from tkFileDialog import askdirectory
from arrange import arrangefiles

root = Tk()
root.title("Arrange Directories")
root.geometry("300x100+50+50")

var = StringVar()
label = Label(root, textvariable = var)
var.set("Select the Directory to be arranged")

label.pack(pady=10)
def callback():
	path = askdirectory()
	print path

	arrangefiles(path)

errmsg = 'Error!'

Button(root,text='Select Folder', command = callback, width=10 ).pack()
Button(root,text='Close', width=10 ).pack()
root.mainloop()

