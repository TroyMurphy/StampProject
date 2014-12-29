from tkinter_helper import TkStampManager
from _models.stamp import Stamp

###CREATE COPY INSTANCES 1-6
#===============================================================================
# shop_copy = Copy(copy_name="SHOP COPY",
#                  condition="all",
#                  stamp_dict={0:Stamp()})
#===============================================================================

###VARIABLES
COPIES = []

def main():
    root = TkStampManager(COPIES)
    root.run_mainloop()
    
if __name__=="__main__":
    main()
