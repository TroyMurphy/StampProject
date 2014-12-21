from _models.worksheet_copy import Copy
from tkFileDialog import askopenfilename

try:
    import tkinter as tk
except ImportError:
    import Tkinter as tk


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
        self.active_copy = Copy()
        self.copy_list = copyList
        #must be independent of active_copy filters because
        #these filters are not saved to copy until save is pressed
        
    def run_mainloop(self):
        self.root.mainloop()
        
    def tk_set_input_options(self):
        #calls all left hand inputs for the interface
        self._build_file_prompt().grid(row=0,column=0)
        self._build_filter_section().grid(row=1,column=0, sticky=tk.W)
        self._build_stamp_section().grid(row=2, column=0, sticky=tk.W)
        self._tk_set_right_options().grid(row=0, column=1, rowspan=3, sticky=tk.W)
        self.save_copy_button = tk.Button(master=self.root,text="Save",command=self.save_copy)
        self.save_copy_button.grid(row=3, column=0)
        self.root.columnconfigure(0, minsize="800")
        
    def _build_file_prompt(self):
        self.title_bar = tk.Frame(master=self.root, width=20)
        self.file_path = tk.StringVar()
        self.file_path.set("Choose a pdf document")
        file_path_label = tk.Label(master = self.title_bar, textvariable=self.file_path)
        self.file_button = tk.Button(master=self.title_bar, text="Open",command= self.get_filepath)
        file_path_label.grid(row=0,column=0)
        self.file_button.grid(row=0, column=1)
        return self.title_bar
        
    def _build_filter_section(self):
        #Generates all entities for the window
        #Targeted to mirror image in TroyProject/docs/excel_copy_screenshot.png
        self.filter_frame = tk.LabelFrame(master=self.root, text="Filter Manager",width=500,name="filter_frame")
        
        condition_1_label = tk.Label(master=self.filter_frame, text="Page Contains Text")
        self.condition_1 = tk.Entry(master=self.filter_frame, name='condition_1_entry')
        self.operator = tk.IntVar()
        self.operator.set(0)
        and_operator = tk.Radiobutton(master=self.filter_frame, text="AND", variable=self.operator, value=0)
        or_operator = tk.Radiobutton(master=self.filter_frame, text="OR", variable=self.operator, value=1)
        condition_2_label = tk.Label(master=self.filter_frame, text="Page Is Size")
        self.condition_2 = tk.StringVar()
        pagesize_option_menu = apply(tk.OptionMenu, (self.filter_frame, self.condition_2) + tuple(self.PAGE_SIZES.values()))
        
        #packs entities into the grid
        condition_1_label.grid(row=1, column=0, sticky=tk.W)
        self.condition_1.grid(row=1, column=1)
        and_operator.grid(row=2, column=0)
        or_operator.grid(row=2, column=1)
        condition_2_label.grid(row=3, column=0, sticky=tk.W)
        pagesize_option_menu.grid(row=3, column=1)
        
        return self.filter_frame
    
    def _build_stamp_section(self):
        self.stamp_frame = tk.LabelFrame(master=self.root, text="Stamp Manager",width=500, name="stamp_frame")
        #Build the filters
        for i in range(self.active_copy.count_stamps() ):
            self.active_stamps[i] = (
                                      tk.StringVar(self.root),
                                      tk.Entry(master=self.stamp_frame)
                                      )
        #Show the filters
        #k is the index it will be shown in. Add one to offset title
        #v[0] is the variable tied to the optionMenu
        #v[1] is the input entry that must be placed in the adjacent column for info
        for k,v in self.active_stamps.items():
            option = apply(tk.OptionMenu, (self.stamp_frame, v[0]) + tuple(self.PAGE_FILTERS.values()))
            option.grid(row=k+1, column=0)
            v[1].grid(row=k+1, column=1)
        new_stamp_button = tk.Button(master=self.stamp_frame, text="New Stamp", command=self.new_stamp)
        new_stamp_button.grid(row=1, column=2)
        return self.stamp_frame
            
    def _tk_set_right_options(self):
        self.copy_frame = tk.Frame(master=self.root, name='right_options')
        self.copy_listbox = tk.Listbox(master=self.copy_frame, name="copy_listbox")
        for item in self.copy_list:
            self.copy_listbox.insert(tk.END, item.name or "copy")
        self.printButton = tk.Button(master=self.copy_frame, text="Print Copy", command=self._submit_function)
    
        self.copy_listbox.grid(row=0, column=0)
        self.printButton.grid(row=1, column=0)
        return self.copy_frame
    
    def _generate_filters(self):
        return self.condition_1, self.condition_2
    
    def _generate_stamps(self):
        return self.active_stamps
        
    def _submit_function(self):
        print("SUBMIT")
        
    def activeCopy(self):
        #get info from current window and generate a copy
        newCopy = Copy()
        return newCopy
    
    def save_copy(self):
        filter1,filter2 = self._generate_filters()
        stamp_dict = self._generate_stamps()
        copy = Copy(reader_filestream=self.filepath,)
        
    def get_filepath(self):
        filename = askopenfilename()
        self.file_path.set(filename)
    def new_stamp(self):
        print("New stamp")