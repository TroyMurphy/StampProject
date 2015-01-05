from tkinter_helper import TkStampManager
from _models.stamp import Stamp
from _models.pdf_copy import StampPDFCopy
##CREATE COPY INSTANCES 1-6
#===============================================================================
# shop_copy = StampPDFCopy(copy_name="SHOP COPY",
#                   condition="all",
#                   stamp_dict={0:Stamp()})
#===============================================================================

#===============================================================================
# stamp_copy = StampPDFCopy(
#                             copy_name="SHOP",
#                             text_filter_content="",
#                             size_filter_content="",
#                             condition = "all",
#                             stamp_dict={0: Stamp(Stamp.TYPES[Stamp.TEXT_INDEX], "Shop Copy")}
#                         )
#===============================================================================

###VARIABLES
COPIES = []

def main():
    root = TkStampManager(COPIES)
    root.run_mainloop()
    
if __name__=="__main__":
    main()


#72 points per inch
#25.4 mm per inch