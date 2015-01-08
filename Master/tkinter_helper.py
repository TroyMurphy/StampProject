from _models.pdf_copy import StampPDFCopy
from _models.reader import StampPDFReader, StampPDFWriter
from PyPDF2 import PdfFileReader, PdfFileWriter
from _models.stamp import Stamp
from tkFileDialog import askopenfilename
from datetime import datetime
import copy
#For 2.7 and 3 consistency
try:
    import tkinter as tk
except ImportError:
    import Tkinter as tk

DEFAULT_STAMP_NUM = 1
WORLD_COORDINATES = "1200x480"
LEFT_FRAME_WIDTH = 480
BUTTON_PADDING = 20
LABEL_FRAME_PADDING = 5
#DEFAULT_OUTPUT_NAME = lambda:"output.pdf"
DEFAULT_OUTPUT_NAME = lambda:"COPYSET_"+datetime.now().strftime("%y_%m_%d_%H-%M-%S")+".pdf"

class TkStampManager():
    PAGE_SIZES= StampPDFCopy.PAGE_SIZES
    PAGE_STAMP_TYPES= Stamp.TYPES
    
    def __init__(self, copyListFunc):
        self.root = tk.Tk()
        self.root.geometry(WORLD_COORDINATES)
        self.root.grid_propagate(0)
        #stamp frame holds all entries for stamps in the stamp_dict
        #stamp_master allows the new button to be below all entries easily
        self.stamp_frame = None
        #Content to create a new copy instance
        self.copy_name = tk.StringVar()
        self.input_filepath = tk.StringVar()
        self.input_filepath.set("Choose a file")
        self.output_filepath = tk.StringVar()
        self.output_filepath.set("Choose a file or set Input for default")
        self.in_filepath_button_text = tk.StringVar()
        self.out_filepath_button_text = tk.StringVar()
        self.in_filepath_button_text.set("Open")
        self.out_filepath_button_text.set("Open")
        self.text_filter_keyphrase = tk.StringVar()
        self.page_size_filter = tk.StringVar()
        self.condition_string = tk.StringVar()
        self.scale_output_to = tk.StringVar()
        #self.condition_string.trace('w', self.condition_update_function) # To disable filters on selection of all
        self.stamp_dict = {}
        
        self.created_copies_list = copyListFunc()
        self._build_frames()
    
    def run_mainloop(self):
        self.root.mainloop()
    ##########################
    # All internal functions
    ##########################
    def _build_frames(self):
        def _build_left_frame(window):
            def _build_name_frame(window):
                name_frame = tk.LabelFrame(master=window, text="Copy Name", labelanchor=tk.N, pady=LABEL_FRAME_PADDING)
                name_entry = tk.Entry(master=name_frame, textvariable=self.copy_name)
                name_entry.grid()
                name_frame.columnconfigure(0, minsize=LEFT_FRAME_WIDTH)
                name_frame.grid(row=0,column=0)
                
            def _build_filter_frame(window):
                filter_frame = tk.LabelFrame(master=window, text="Filter Manager", labelanchor=tk.N,pady=LABEL_FRAME_PADDING)
                filter1_label = tk.Label(master=filter_frame, text="Page Contains Text:")
                filter1_entry = tk.Entry(master=filter_frame, textvariable=self.text_filter_keyphrase)
                condition_frame = tk.Frame(master=filter_frame)
                radiobutton_and = tk.Radiobutton(master=condition_frame, variable=self.condition_string, value="and",text="OR")
                radiobutton_all = tk.Radiobutton(master=condition_frame, variable=self.condition_string, value="all", text="ALL")
                radiobutton_or = tk.Radiobutton(master=condition_frame, variable=self.condition_string, value="or", text="AND")
                filter2_label = tk.Label(master=filter_frame, text="Page is Size:")
                filter2_options = tk.OptionMenu(filter_frame, self.page_size_filter, *self.PAGE_SIZES.keys())
            
                filter1_label.grid(row=0,column=0)
                filter1_entry.grid(row=0,column=1)
                condition_frame.grid(row=1,column=0, columnspan=2)
                radiobutton_and.grid(row=0,column=0, padx=20)
                radiobutton_all.grid(row=0,column=1, padx=20)
                radiobutton_or.grid(row=0,column=2, padx=20)
                filter2_label.grid(row=2,column=0)
                filter2_options.grid(row=2,column=1,sticky=tk.W+tk.E)
                
                filter_frame.columnconfigure(0, minsize=LEFT_FRAME_WIDTH/2)
                filter_frame.columnconfigure(1, minsize=LEFT_FRAME_WIDTH/2)
                
                #place frame at the top stretched across the cell
                filter_frame.grid(row=1,column=0,sticky=tk.N+tk.W+tk.E, pady=LABEL_FRAME_PADDING)
                
            def _build_stamp_frame(window):
                stamp_master = tk.LabelFrame(master=window, text="Stamp Manager", labelanchor=tk.N,pady=LABEL_FRAME_PADDING)
                self.stamp_frame = tk.Frame(master=stamp_master)
                for i in range(DEFAULT_STAMP_NUM):
                    self.stamp_dict[i] = Stamp()
            
                for k in self.stamp_dict.keys():
                    stamp_type_optionmenu = tk.OptionMenu(self.stamp_frame, self.stamp_dict[k].get_type(), *self.PAGE_STAMP_TYPES)
                    stamp_content_entry = tk.Entry(master=self.stamp_frame, text="", textvariable=self.stamp_dict[k].get_content())
                    
                    stamp_type_optionmenu.grid(row=k, column=0, sticky=tk.W+tk.E)
                    stamp_content_entry.grid(row=k, column=1)
                new_stamp_button = tk.Button(master=stamp_master, text="New Stamp", command = self._new_stamp_function)  

                self.stamp_frame.columnconfigure(0, minsize=LEFT_FRAME_WIDTH/2)
                self.stamp_frame.columnconfigure(1, minsize=LEFT_FRAME_WIDTH/2)
               
                self.stamp_frame.grid(row=0, column=0)
                new_stamp_button.grid(row=1, column=0)
                
                stamp_master.grid(row=2,column=0, sticky=tk.N+tk.W+tk.E, pady=LABEL_FRAME_PADDING)
            def _build_scale_frame(window):
                scale_frame = tk.LabelFrame(master=window, text="Scale To", labelanchor=tk.N,pady=LABEL_FRAME_PADDING)
                scale_option_menu = tk.OptionMenu(scale_frame, self.scale_output_to, *self.PAGE_SIZES.keys())
                scale_option_menu.grid(sticky=tk.N+tk.W+tk.E)
                scale_frame.columnconfigure(0, minsize=LEFT_FRAME_WIDTH)
                scale_frame.grid(row=3,column=0, pady=LABEL_FRAME_PADDING)
            
            _build_name_frame(window)
            _build_filter_frame(window)
            _build_stamp_frame(window)
            _build_scale_frame(window)
            
        def _build_center_frame(window):
            def _build_copy_selection(window):
                selection_checkbuttons = tk.Frame(master=window, bg="grey", name='checkbutton_frame')
                rowindex = 0
                for c in self.created_copies_list:
                    insert_checkbox = tk.Checkbutton(master=selection_checkbuttons, text=c.get_name(), variable=c.shouldPrint, indicatoron=0, justify=tk.CENTER)
                    insert_checkbox.grid(row=rowindex, sticky=tk.W+tk.E)
                    rowindex += 1
                
                selection_checkbuttons.columnconfigure(0,minsize=LEFT_FRAME_WIDTH/2)    
                selection_checkbuttons.grid(row=0,column=0, sticky=tk.N+tk.W+tk.E)
            _build_copy_selection(window)
        def _build_right_frame(window):
            def _build_file_search(window):
                file_search_frame = tk.LabelFrame(master=window, text="Finder", labelanchor=tk.N,pady=LABEL_FRAME_PADDING)
                infile_search_label = tk.Label(master=file_search_frame, wraplength=400, textvariable=self.input_filepath, justify=tk.LEFT)
                infile_search_button = tk.Button(master=file_search_frame, textvariable=self.in_filepath_button_text, command=self._infile_search)
                outfile_search_label = tk.Label(master=file_search_frame, wraplength=400, textvariable=self.output_filepath, justify=tk.LEFT)
                outfile_search_button = tk.Button(master=file_search_frame, textvariable=self.out_filepath_button_text, command=self._outfile_search)
                
                infile_search_label.grid(row=0,column=0)
                infile_search_button.grid(row=0,column=1)
                outfile_search_label.grid(row=1)
                outfile_search_button.grid(row=1,column=1)
                
                file_search_frame.columnconfigure(0, minsize=400)
                file_search_frame.grid(row=0,column=0,sticky=tk.N+tk.W+tk.E)
                
            def _build_final_submit_button(window):
                submit_button = tk.Button(master=window, text="Print Selected Copies To File", command=self._final_submit_func)
                submit_button.grid(row=1, sticky=tk.N+tk.W+tk.E,pady=BUTTON_PADDING,)
            
            _build_file_search(window)
            _build_final_submit_button(window)
            
        frame_left = tk.LabelFrame(master=self.root, text="Build New Copy", labelanchor=tk.N, width=500, height=800,bg="grey", padx=5, pady=5, name="left_frame")
        frame_left.grid_propagate(0)
        frame_left.grid(row=0,column=0)
        
        frame_center=tk.LabelFrame(master=self.root, text="Copy Selection", labelanchor=tk.N, width=200, height=800, bg="grey",padx=5, pady=5, name="center_frame")
        frame_center.grid_propagate(0)
        frame_center.grid(row=0,column=1)
        
        frame_right = tk.LabelFrame(master=self.root, text="Selected Copy Summary",labelanchor=tk.N, width=500, height=800,bg="grey", padx=5, pady=5, name="right_frame")
        frame_right.grid_propagate(0)
        frame_right.grid(row=0,column=2)
    
        _build_left_frame(frame_left)
        _build_center_frame(frame_center)
        _build_right_frame(frame_right)
        
        submit_button = tk.Button(master=frame_left, text="CREATE COPY", command = self._submit_copy, pady=BUTTON_PADDING)
        submit_button.grid(row=10, column=0, sticky=tk.W+tk.E)
    
    def _infile_search(self):
        self.input_filepath.set(askopenfilename())
        self.in_filepath_button_text.set("Change")
        self.output_filepath.set(
                              self.input_filepath.get().rsplit('/',1)[0]+'/'+DEFAULT_OUTPUT_NAME()
                              )
        self.out_filepath_button_text.set("Change")
        
    def _outfile_search(self):
        self.output_filepath.set(askopenfilename())
        self.out_filepath_button_text.set("Change")
    
        
    def _new_stamp_function(self):
        next_stamp_key = len(self.stamp_dict)
        self.stamp_dict[next_stamp_key] = Stamp()
        stamp_type_optionmenu = tk.OptionMenu(self.stamp_frame, self.stamp_dict[next_stamp_key].get_type(), *self.PAGE_STAMP_TYPES)
        stamp_content_entry = tk.Entry(master=self.stamp_frame, text="", textvariable=self.stamp_dict[next_stamp_key].get_content())
            
        stamp_type_optionmenu.grid(row=next_stamp_key, column=0, sticky=tk.W+tk.E)
        stamp_content_entry.grid(row=next_stamp_key, column=1)
        
    def condition_update_function(self):
        pass
        
    def _submit_copy(self):
        if (self.condition_string.get() is not None and self.copy_name.get() is not ""):
            if self.condition_string=="all" or (self.page_size_filter.get()!="" and self.text_filter_keyphrase.get() !=""):
                c = StampPDFCopy(
                            copy_name=str(self.copy_name.get()),
                            text_filter_content=str(self.text_filter_keyphrase.get()),
                            size_filter_content=str(self.page_size_filter.get()),
                            condition = str(self.condition_string.get()),
                            stamp_dict=self.stamp_dict,
                            scale_output_to = self.scale_output_to.get()
                            )
            else:
                print("Conditions or All Filter Required")
            self.created_copies_list.append(c)
            print("Copy Created")
            #insert into checkbutton frame in center for final selection
            checkbutton_frame = self.root.nametowidget("center_frame.checkbutton_frame")
            insert_checkbox = tk.Checkbutton(master=checkbutton_frame, text=c.get_name(), variable=c.shouldPrint, indicatoron=0, justify=tk.CENTER)
            insert_checkbox.grid(row=len(self.created_copies_list),sticky=tk.W+tk.E)
            
            return c
        print ("{} is None".format("condition" if self.condition_string.get() is None else "name"))
        return False
    
    def _final_submit_func(self):
        
        input_filename = self.input_filepath.get()
        
        infile = file(input_filename, 'rb')
        writer = PdfFileWriter()
        
        progress_reader = PdfFileReader(infile)
        selected_copies = [c for c in self.created_copies_list if c.get_shouldPrint()]
        progress_blocks = progress_reader.getNumPages() * len(selected_copies)
        self._make_progress_bar(progress_blocks)
        
        for c in selected_copies:
            c.add_reader(StampPDFReader(infile))
            writer = c.add_valid_pages(writer)
        
        output_filename = self.output_filepath.get()
        outfile = file(output_filename, 'wb')
        print("Writing File....")
        writer.write(outfile)
        print("Successfully output file")
        infile.close()
        outfile.close()
        
        
        #Have each selected copy generate, stamp, and then add its pages to the filewriter object
        #=======================================================================
        # selected_copies = [c for c in self.created_copies_list if c.get_shouldPrint()]
        # for stamp_copy in selected_copies:
        #     copied_reader = copy.deepcopy(reader)
        #     stamp_copy.bind_pages(copied_reader)
        #     stamp_copy.apply_filters()
        #     for p in stamp_copy.get_filtered_pages():
        #         writer.addPage(p) 
        #=======================================================================

    def _make_progress_bar(self, numBlocks):
        progress_bar_frame = tk.LabelFrame(master=self.root.nametowidget('right_frame'), text="Progress")
        label_width = progress_bar_frame.winfo_width()//numBlocks
        for i in range(numBlocks):
            tk.Label(master=progress_bar_frame,name="pb_"+str(i), bg="white").grid(row=0,column=i, padx=2)
            progress_bar_frame.columnconfigure(i, minsize=label_width)
        
        progress_bar_frame.grid(row=2, column=0, sticky=tk.N+tk.W+tk.E)
        