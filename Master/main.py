from tkinter_helper import TkStampManager
from _models.stamp import Stamp
from _models.pdf_copy import StampPDFCopy

try:
    import tkinter as tk
except:
    import Tkinter as tk


##CREATE COPYFUNC FOR INSTANCES 1-6

def generate_base_copy_instances():
   #return a list of copies. Pass this function to prevent calling StringVars/IntVars before tk.Tk()
   shop_copy_stamps = {0 : Stamp()}
   shop_copy = StampPDFCopy(
                            copy_name= "SHOP",
                            text_filter_content="",
                            size_filter_content="",
                            condition = "all",
                            stamp_dict=shop_copy_stamps
                        )
   return [shop_copy]

##VARIABLES
COPIES_FUNC = generate_base_copy_instances

def main():
    root = TkStampManager(COPIES_FUNC)
    root.run_mainloop()
    
if __name__=="__main__":
    main()


#72 points per inch
#25.4 mm per inch