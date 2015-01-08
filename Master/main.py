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
    shop_copy_stamps = {0 : Stamp(Stamp.TYPES[Stamp.TEXT_INDEX], "SHOP COPY")}
    shop_copy = StampPDFCopy(
                            copy_name= "SHOP",
                            text_filter_content="",
                            size_filter_content="",
                            condition = "all",
                            stamp_dict=shop_copy_stamps
                        )
    foreman_copy_stamps = {0 : Stamp(Stamp.TYPES[Stamp.TEXT_INDEX], "FOREMAN COPY")}
    foreman_copy = StampPDFCopy(
                            copy_name= "FOREMAN",
                            text_filter_content="",
                            size_filter_content="",
                            condition = "all",
                            stamp_dict=foreman_copy_stamps
                        )
    machine_copy_stamps = {0 : Stamp(Stamp.TYPES[Stamp.TEXT_INDEX], "MACHINE COPY")}
    machine_copy = StampPDFCopy(
                            copy_name= "MACHINE",
                            text_filter_content="machine, shop",
                            size_filter_content="8.5 x 11",
                            condition = "and",
                            stamp_dict=machine_copy_stamps
                        )
    burn_copy_stamps = {0 : Stamp(Stamp.TYPES[Stamp.TEXT_INDEX], "BURN TABLE COPY")}
    burn_copy = StampPDFCopy(
                            copy_name= "BURN TABLE",
                            text_filter_content="burn, dxf, table",
                            size_filter_content="8.5 x 11",
                            condition = "and",
                            stamp_dict=burn_copy_stamps
                        )
    bend_copy_stamps = {0 : Stamp(Stamp.TYPES[Stamp.TEXT_INDEX], "BEND COPY")}
    bend_copy = StampPDFCopy(
                            copy_name= "BEND",
                            text_filter_content="bend, form, fti",
                            size_filter_content="8.5 x 11",
                            condition = "and",
                            stamp_dict=bend_copy_stamps
                        )
    file_copy_stamps = {0 : Stamp(Stamp.TYPES[Stamp.TEXT_INDEX], "FILE COPY")}
    file_copy = StampPDFCopy(
                            copy_name= "FILE",
                            text_filter_content="",
                            size_filter_content="",
                            condition = "all",
                            stamp_dict=file_copy_stamps,
                            scale_output_to ="8.5 x 11"
                        )
   
    return [shop_copy, foreman_copy, machine_copy, burn_copy, bend_copy, file_copy]

##VARIABLES
COPIES_FUNC = generate_base_copy_instances

def main():
    root = TkStampManager(COPIES_FUNC)
    root.run_mainloop()
    
if __name__=="__main__":
    main()


#72 points per inch
#25.4 mm per inch