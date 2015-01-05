import copy

try:
    from tkinter import IntVar
except:
    from Tkinter import IntVar

class StampPDFCopy(object):
    SIZE_TOLERANCE = 0.5

    PAGE_SIZES={
             "8.5 x 11":("A",(8.5,11)),
             "11 x 17":("B",(11,17)),
             "17 x 22":("C",(17,22)),
             "22 x 34":("D",(22,34)),
             "34 x 44":("E",(34,44)),
             "28 x 40":("F",(28,40))
             }
    
    def __init__(self, copy_name=None, text_filter_content=None, 
                 size_filter_content=None, condition=None, stamp_dict = {}):
        self.display_name = copy_name.upper()
        self.text_filter_content = text_filter_content
        self.size_filter_content = size_filter_content
        self.condition = condition
        self.stamp_dict = stamp_dict
        self.shouldPrint = IntVar()
      
        #deepcopied list of pypdf page objects from reader, is filtered by apply filters func
        self.valid_pages = [] 

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
    
    def set_valid_pages(self, filereader):
        for page in filereader.pages:
            self.valid_pages.append(copy.deepcopy(page))
        self.apply_filters()
        
    def str_rep(self):
        outputstring=""
        outputstring += self.get_name()
        return outputstring
    
    def test_page_text_filter(self):
        return self.text_filter_content in page.extractText()

    def test_page_size_filter(self, page):
        #72 points to an inch
        return abs(min(rect[2:])/72-self.get_size_filter[1][0])<=self.SIZE_TOLERANCE and \
            abs(max(rect[2:])/72-self.get_size_filter[1][1])<=self.SIZE_TOLERANCE
    
    def apply_filters(self):
        if self.condition=="all":
            return 0
        if self.condition=="and":
            for page in self.valid_pages:
                if (not self.test_page_text_filter(page)) or (not self.test_page_size_filter(page)):
                    self.valid_pages.remove(page)   
        elif self.condition=="or":
            for page in self.valid_pages:
                if (not self.test_page_text_filter(page)) and (not self.test_page_size_filter(page)):
                    self.valid_pages.remove(page)
        
    def stamp_pdf(self, pdf_reader):
        pass