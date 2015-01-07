import copy
from collections import OrderedDict

try:
    from tkinter import IntVar
except:
    from Tkinter import IntVar

PIXELS_PER_INCH = 72

class StampPDFCopy(object):
    SIZE_TOLERANCE = 0.5

    PAGE_SIZES= OrderedDict([
             ("8.5 x 11",("A",(8.5,11))),
             ("11 x 17",("B",(11,17))),
             ("17 x 22",("C",(17,22))),
             ("22 x 34",("D",(22,34))),
             ("34 x 44",("E",(34,44))),
             ("28 x 40",("F",(28,40)))
             ])
    
    def __init__(self, copy_name=None, text_filter_content=None, 
                 size_filter_content=None, condition=None, stamp_dict=None, scale_output_to=None):
        self.display_name = copy_name.upper()
        self.text_filter_content = text_filter_content
        self.size_filter_content = size_filter_content
        self.condition = condition
        self.shouldPrint = IntVar()
        if type(stamp_dict)==dict:
            self.stamp_dict = stamp_dict
        elif type(stamp_dict)==tuple:
            init_stamps(stamp_dict)
        else:
            stamp_dict={}
        #deepcopied list of pypdf page objects from reader, is filtered by apply filters func
        self.valid_pages = []
        self.scale_output_to=scale_output_to
        
    def init_stamps(self, stamp_objects):
        #must initialize an instance with empty stringvar objects to call this function
        if text_filter is not None:
            self.text_filter_content.set(text_filter)
        if size_filter is not None:
            self.size_filter_content.set(size_filter)
        self.condition.set(condition)
        for i in range(len(stamp_objects)):
            self.stamp_dict[i] = stamp_objects[i]
        
    def get_text_filter(self):
        return self.text_filter_content
    def get_size_filter(self):
        return self.PAGE_SIZES[self.size_filter_content]
    def get_condition(self):
        return self.condition
    def get_stamp_dict(self):
        return self.stamp_dict
    def get_name(self):
        return self.display_name
    def get_shouldPrint(self):
        return self.shouldPrint.get()
    
    def add_reader(self, reader):
        self.reader = reader
        self.stamp_pdf()
    
    def test_page_text_filter(self):
        words = [w.strip() for w in self.text_filter_content.split(",")]
        document_text = page.extractText()
        for w in words:
            if w in document_text():
                return True
        return False

    def test_page_size_filter(self, page):
        #72 points to an inch
        return abs(min(rect[2:])/PEXELS_PER_INCH -self.get_size_filter[1][0])<=self.SIZE_TOLERANCE and \
            abs(max(rect[2:])/PIXELS_PER_INCH-self.get_size_filter[1][1])<=self.SIZE_TOLERANCE
    
    def add_valid_pages(self, writer):
        if self.reader is None:
            #raise exception
            return 0
        
        if self.condition=="all":
            #add all pages, no filter to increase speed up
            for page in self.reader.pages:
                writer.addPage(page)
        elif self.condition=="and":
            for page in self.reader.pages:
                if (self.test_page_text_filter(page)) and (self.test_page_size_filter(page)):
                    writer.addPage(page)   
        elif self.condition=="or":
            for page in self.valid_pages:
                if (self.test_page_text_filter(page)) or (self.test_page_size_filter(page)):
                    writer.addPage(page)
        return writer
    
    def get_pages(self):
        return self.valid_pages
    
    def stamp_pdf(self):
        #will stamp every page on reader with stamp.
        #Should only stamp valid pages.
        for stamp in self.get_stamp_dict().values():
            #TODO: SET OFFSETS HERE!
            for page in self.reader:
                stamp_pdf = stamp.generate_pdf_page(page.trimBox[2]*PIXELS_PER_INCH,page.trimBox[3]*PIXELS_PER_INCH)
                page = page.mergePage(stamp_pdf.getPage(0))
