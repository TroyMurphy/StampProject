import copy, operator, StringIO
from _models.stamp import Stamp
from PyPDF2 import PdfFileReader
from collections import OrderedDict
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter, legal, elevenSeventeen, landscape,portrait
from reportlab.lib.colors import PCMYKColor, PCMYKColorSep, Color, black, blue, red
from reportlab.lib.units import inch

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
    
    def test_page_text_filter(self, page):
        words = [w.strip() for w in self.text_filter_content.split(",")]
        document_text = page.extractText()
        for w in words:
            if w in document_text:
                return True
        return False

    def test_page_size_filter(self, page):
        return all([
                   abs(min(page.trimBox[2:])/PIXELS_PER_INCH -self.get_size_filter()[1][0])<=self.SIZE_TOLERANCE , 
                   abs(max(page.trimBox[2:])/PIXELS_PER_INCH-self.get_size_filter()[1][1])<=self.SIZE_TOLERANCE
                   ])
    
    def add_valid_pages(self, writer):
        if self.reader is None:
            #raise exception
            return 0
        print("Creating {}".format(self.get_name()))
        progress_end = self.reader.getNumPages()
        progress_count = 1
        self.addCoverPage(writer)
        #just as efficient as commented section. and is 
        for page in self.reader.pages:
            if (self.condition=="all") or eval(str(self.test_page_text_filter(page)) +
                                         " " + self.get_condition() + " " +
                                         str(self.test_page_size_filter(page))):
                return_page = self.stamp_page(page)
                if self.scale_output_to is not None:
                    return_page = self.scalePage(return_page)
                writer.addPage(return_page)
                print("Added %d of %d" % (progress_count, progress_end))
            else:
                print("Omitted %d of %d" % (progress_count, progress_end))
            progress_count+=1
        return writer
        #=======================================================================
        # To demonstrate how duplicate code can be removed
        # with no loss of speed
        # elif self.condition == and
        #    ......
        # elif self.condition == or
        #     ......
        #=======================================================================
    
    def get_pages(self):
        return self.valid_pages
    
    def stamp_page(self, page):
        #will stamp every page on reader with stamp.
        #Should only stamp valid pages.
        for idx,stamp in self.get_stamp_dict().items():
            #Add each stamp one canvas at a time.
            #TODO: optimize this step
            page = stamp.stampContent(page, idx)
        return page
    
    def addCoverPage(self, writer):
        blank_page = writer.addBlankPage(width=612, height=792)
        stamped_page = self.stampPageTitle(blank_page)
        blank_page.mergePage(stamped_page)
        print("Cover Page Added")
    def stampPageTitle(self, page):
        packet = StringIO.StringIO()
        main_canvas = canvas.Canvas(packet, (float(page.mediaBox[2]), float(page.mediaBox[3])))
        main_canvas.setFillColorRGB(0,0,0,alpha=1)
        main_canvas.setFont("Helvetica-Bold", 50)
        main_canvas.drawString(3*inch, 8*inch, self.display_name)
        main_canvas.save()

        stamped_pdf= PdfFileReader(packet)
        return stamped_pdf.getPage(0)
    
    def scalePage(self, page):
        orig_dimensions = page.mediaBox[2:]
        scale_dimensions = (self.PAGE_SIZES[self.scale_output_to][1][0]*PIXELS_PER_INCH,self.PAGE_SIZES[self.scale_output_to][1][1]*PIXELS_PER_INCH)
        max_dim_idx = orig_dimensions.index(max(orig_dimensions))
        min_dim_idx = int(not(max_dim_idx))
        page.scaleTo(scale_dimensions[min_dim_idx],scale_dimensions[max_dim_idx])
        return page
    
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


