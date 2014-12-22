from _models.worksheet_copy import Copy
from tkFileDialog import askopenfilename
#For 2.7 and 3 consistency
try:
    import tkinter as tk
except ImportError:
    import Tkinter as tk

DEFAULT_STAMP_NUM = 2
WORLD_COORDINATES = "1010x810"
class TkStampManager():
    PAGE_SIZES={
                 "A":(8.5,11),
                 "B":(11,17),
                 "C":(17,22),
                 "D":(22,34),
                 "E":(34,44),
                 "F":(28,40)
                 }
    PAGE_STAMPS={
                  0:"Text Stamp",
                  1:"Image Stamp", 
                   }
    
    def __init__(self, copyList):
        self.root = tk.Tk()
        self.root.geometry(WORLD_COORDINATES)
        self.root.grid_propagate(0)
        #Content to create a new copy instance
        self.input_filepath = None
        self.text_filter_keyphrase = None
        self.page_size_filter_keyphrase = None
        self.condition_string = tk.StringVar()
        self.stamp_dict = {}
        
        self.created_copies_list = copyList
        self._build_frames()
    
    def run_mainloop(self):
        self.root.mainloop()
    ##########################
    # All internal functions
    ##########################
    def _build_frames(self):
        frame_left = tk.LabelFrame(master=self.root, text="Build New Copy", labelanchor=tk.N, width=500, height=800, padx=5, pady=5)
        frame_left.grid_propagate(0)
        frame_left.grid(row=0,column=0)
        
        frame_center=tk.LabelFrame(master=self.root, text="Existing Copies", labelanchor=tk.N, width=200, height=800, padx=5, pady=5,)
        frame_center.grid_propagate(0)
        frame_center.grid(row=0,column=1)
        
        frame_right = tk.LabelFrame(master=self.root, text="Selected Copy Summary",labelanchor=tk.N, width=300, height=800, padx=5, pady=5)
        frame_right.grid_propagate(0)
        frame_right.grid(row=0,column=2)
    
        frame_filters = tk.LabelFrame(master=frame_left, text="Filter Manager", width=200, padx=5,pady=5)
        frame_filters.grid(row=0, column=0)
        
        button = tk.Button(master=frame_filters, width=50, text="Button")
        button.grid(row=0,column=0)
        
        