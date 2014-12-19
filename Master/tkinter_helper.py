try:
    import tkinter as tk
except ImportError:
    import Tkinter as tk

class TkStampManager():
    def __init__(self, copyList):
        self.root = tk.Tk()
        self.copy_list = copyList
    def run_mainloop(self):
        self.root.mainloop()
        
    def tk_set_input_options(self):
        #calls all left hand inputs for the interface
        self._build_filter_section()
        self._tk_set_right_options()
        
    def _tk_set_right_options(self):
        self.copy_frame = tk.Frame(master=self.root, name='right_options')
        self.copy_listbox = tk.Listbox(master=self.copy_frame, name="copy_listbox")
        for item in self.copy_list:
            self.copy_listbox.insert(tk.END, item.name or "copy")
        self.printButton = tk.Button(master=self.copy_frame, text="Print Copy", command=self._submit_function)
    
        self.copy_listbox.grid(row=0, column=0)
        self.printButton.grid(row=1, column=0)
        self.copy_frame.grid(row=0, column=10, rowspan=9)
    
    def _build_filter_section(self):
        #Generates all entities for the window
        #Targeted to mirror image in TroyProject/docs/excel_copy_screenshot.png
        self.filter_frame = tk.Frame(master=self.root, name="filter_frame")
        
        title = tk.Label(master=self.filter_frame, text="Page Filters:")
        condition_1_label = tk.Label(master=self.filter_frame, text="Page Contains Text")
        self.condition_1 = tk.Entry(master=self.filter_frame, name='condition_1_entry')
        self.operator = tk.IntVar()
        self.operator.set(0)
        and_operator = tk.Radiobutton(master=self.filter_frame, text="AND", variable=self.operator, value=0)
        or_operator = tk.Radiobutton(master=self.filter_frame, text="OR", variable=self.operator, value=1)
        condition_2_label = tk.Label(master=self.filter_frame, text="Page Is Size")
        self.condition_2 = tk.Entry(master=self.filter_frame, name='condition_2_entry')
        
        #packs entities into the grid
        title.grid(row=0, column=0, columnspan=2, sticky=tk.W)
        condition_1_label.grid(row=1, column=0, sticky=tk.W)
        self.condition_1.grid(row=1, column=1)
        and_operator.grid(row=2, column=0)
        or_operator.grid(row=2, column=1)
        condition_2_label.grid(row=3, column=0, sticky=tk.W)
        self.condition_2.grid(row=3, column=1)
        
        self.filter_frame.grid(row=0,column=0)
        
    def _submit_function(self):
        print("SUBMIT") 