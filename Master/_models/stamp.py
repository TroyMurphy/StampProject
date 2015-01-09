import StringIO
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter, legal, elevenSeventeen, landscape,portrait
from reportlab.lib.colors import PCMYKColor, PCMYKColorSep, Color, black, blue, red

from PyPDF2 import PdfFileReader

try:
    import tkinter as tk
except:
    import Tkinter as tk

class Stamp(object):
    TEXT_INDEX=0
    IMAGE_INDEX=1
    TYPES = [
             "Text Stamp",
             "Image Stamp", 
             ]
    def __init__(self, kind=None, content=None):
        self.kind = tk.StringVar()
        if kind is not None:
            self.kind.set(kind)
        self.content = tk.StringVar()
        if content is not None:
            self.content.set(content)
        #TODO: Make these options later
        self.font = 20
        self.offset=0.25*self.font
        
    def set_type(self, type_index):
        self.kind.set(self.TYPES[type_index])
    
    def set_content(self, content):
        self.content.set(content)
        
    def get_content_var(self):
        return self.content
    def get_content(self):
        return self.content.get()

    def get_type(self):
        return self.kind
    
    def stampContent(self, page, index):
        #returns an iterable of stamped page objects to write to file.
        if self.kind.get() == self.TYPES[self.TEXT_INDEX]:
            packet = StringIO.StringIO()
            
            widthPoints=float(page.mediaBox[2])
            heightPoints=float(page.mediaBox[3])
            
            main_canvas = canvas.Canvas(packet, (widthPoints, heightPoints))
            main_canvas.setFillColorRGB(1,0,0,alpha=0.5)
            main_canvas.setFont("Helvetica-Bold", self.font)
            main_canvas.drawString(50, 150*(index+1), self.get_content())
            main_canvas.save()
            
            stamped_pdf = PdfFileReader(packet)
            stamped_page = stamped_pdf.getPage(0)
                
            rotation_angle = page.get('/Rotate', 0)
            #stamped_page.rotateClockwise(page.get('/Rotate'))
            page.mergeRotatedTranslatedPage(
                page2=stamped_page,
                rotation=rotation_angle,
                tx=stamped_page.mediaBox.getWidth() / 2,
                ty=stamped_page.mediaBox.getWidth() / 2
                )
            return page
            
            
            
            
            
            
            
            