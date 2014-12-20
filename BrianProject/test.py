from Tkinter import *
from tkFileDialog import *
root = Tk()
root.wm_title("Pages to PDF")

w = Label(root, text="Please choose a .pages file to convert.") 
fileName = askopenfilename(parent=root)

w.pack()
root.mainloop()