from _models.worksheet_copy import Copy
from _models.stamp import Stamp
from tkFileDialog import askopenfilename
#For 2.7 and 3 consistency
try:
    import tkinter as tk
except ImportError:
    import Tkinter as tk

DEFAULT_STAMP_NUM = 1
WORLD_COORDINATES = "1010x810"
class TkStampManager():
    PAGE_SIZES={
                 "8.5 x 11":("A",(8.5,11)),
                 "11 x 17":("B",(11,17)),
                 "17 x 22":("C",(17,22)),
                 "22 x 34":("D",(22,34)),
                 "34 x 44":("E",(34,44)),
                 "28 x 40":("F",(28,40))
                 }
    PAGE_STAMP_TYPES= Stamp.TYPES
    
    def __init__(self, copyList):
        self.root = tk.Tk()
        self.root.geometry(WORLD_COORDINATES)
        self.root.grid_propagate(0)
        #stamp frame holds all entries for stamps in the stamp_dict
        #stamp_master allows the new button to be below all entries easily
        self.stamp_frame = None
        #Content to create a new copy instance
        self.input_filepath = None
        self.text_filter_keyphrase = None
        self.page_size_filter = tk.StringVar()
        self.condition1_string = tk.StringVar()
        self.stamp_dict = {}
        
        self.created_copies_list = copyList
        self._build_frames()
    
    def run_mainloop(self):
        self.root.mainloop()
    ##########################
    # All internal functions
    ##########################
    def _build_frames(self):
        def _build_left_frame(window):
            def _build_filter_frame(window):
                filter_frame = tk.LabelFrame(master=window, text="Filter Manager", labelanchor=tk.N)
                filter1_label = tk.Label(master=filter_frame, text="Page Contains Text:")
                filter1_entry = tk.Entry(master=filter_frame, textvariable=self.text_filter_keyphrase)
                radiobutton_and = tk.Radiobutton(master=filter_frame, variable=self.condition1_string, value="and",text="OR")
                radiobutton_or = tk.Radiobutton(master=filter_frame, variable=self.condition1_string, value="or", text="AND")
                filter2_label = tk.Label(master=filter_frame, text="Page is Size:")
                filter2_options = tk.OptionMenu(filter_frame, self.page_size_filter, *self.PAGE_SIZES.keys())
            
                filter1_label.grid(row=0,column=0)
                filter1_entry.grid(row=0,column=1)
                radiobutton_and.grid(row=1,column=0)
                radiobutton_or.grid(row=1,column=1)
                filter2_label.grid(row=2,column=0)
                filter2_options.grid(row=2,column=1,sticky=tk.W+tk.E)
                
                filter_frame.columnconfigure(0, minsize=240)
                filter_frame.columnconfigure(1, minsize=240)
                #place frame at the top stretched across the cell
                filter_frame.grid(row=0,column=0,sticky=tk.N+tk.W+tk.E)
                
            def _build_stamp_frame(window):
                stamp_master = tk.LabelFrame(master=window, text="Stamp Manager", labelanchor=tk.N)
                self.stamp_frame = tk.Frame(master=stamp_master)
                for i in range(DEFAULT_STAMP_NUM):
                    self.stamp_dict[i] = Stamp(tk.StringVar())
            
                for k in self.stamp_dict.keys():
                    stamp_type_optionmenu = tk.OptionMenu(self.stamp_frame, self.stamp_dict[k].get_type(), *self.PAGE_STAMP_TYPES)
                    stamp_content_entry = tk.Entry(master=self.stamp_frame, text="", textvariable=self.stamp_dict[k].get_content())
                    
                    stamp_type_optionmenu.grid(row=k, column=0, sticky=tk.W+tk.E)
                    stamp_content_entry.grid(row=k, column=1)
                new_stamp_button = tk.Button(master=stamp_master, text="New Stamp", command = self._new_stamp_function)  

                self.stamp_frame.columnconfigure(0, minsize=240)
                self.stamp_frame.columnconfigure(1, minsize=240)
               
                self.stamp_frame.grid(row=0, column=0)
                new_stamp_button.grid(row=1, column=0)
                
                stamp_master.grid(row=1,column=0, sticky=tk.N+tk.W+tk.E)
                    
            _build_filter_frame(window)
            _build_stamp_frame(window)

        def _build_center_frame(window):
            pass
        def _build_right_frame(window):
            pass
            
        frame_left = tk.LabelFrame(master=self.root, text="Build New Copy", labelanchor=tk.N, width=500, height=800, padx=5, pady=5)
        frame_left.grid_propagate(0)
        frame_left.grid(row=0,column=0)
        
        frame_center=tk.LabelFrame(master=self.root, text="Existing Copies", labelanchor=tk.N, width=200, height=800, padx=5, pady=5,)
        frame_center.grid_propagate(0)
        frame_center.grid(row=0,column=1)
        
        frame_right = tk.LabelFrame(master=self.root, text="Selected Copy Summary",labelanchor=tk.N, width=300, height=800, padx=5, pady=5)
        frame_right.grid_propagate(0)
        frame_right.grid(row=0,column=2)
    
        _build_left_frame(frame_left)
        _build_center_frame(frame_center)
        _build_right_frame(frame_right)
        
        submit_button = tk.Button(master=frame_left, text="CREATE COPY", command = self._submit_copy)
        submit_button.grid(row=10, column=0, sticky=tk.W+tk.E)
        
    def _new_stamp_function(self):
        next_stamp_key = len(self.stamp_dict)
        self.stamp_dict[next_stamp_key] = Stamp(tk.StringVar())
        stamp_type_optionmenu = tk.OptionMenu(self.stamp_frame, self.stamp_dict[next_stamp_key].get_type(), *self.PAGE_STAMP_TYPES)
        stamp_content_entry = tk.Entry(master=self.stamp_frame, text="", textvariable=self.stamp_dict[next_stamp_key].get_content())
            
        stamp_type_optionmenu.grid(row=next_stamp_key, column=0, sticky=tk.W+tk.E)
        stamp_content_entry.grid(row=next_stamp_key, column=1)
        
        
    def _submit_copy(self):
        return None
        