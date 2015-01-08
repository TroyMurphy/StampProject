from tkinter_helper import TkStampManager
from _models.pdf_copy import StampPDFCopy, generate_base_copy_instances

try:
    import tkinter as tk
except:
    import Tkinter as tk


##CREATE COPYFUNC FOR INSTANCES 1-6


##VARIABLES
#copies_func not called in main, cannot legall instantiate
#tk.*Var until after tk.Tk() is called

COPIES_FUNC = generate_base_copy_instances

def main():
    root = TkStampManager(COPIES_FUNC)
    root.run_mainloop()
    
if __name__=="__main__":
    main()


#72 points per inch
#25.4 mm per inch