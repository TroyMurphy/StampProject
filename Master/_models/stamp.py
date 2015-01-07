import StringIO
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter, legal, elevenSeventeen, landscape,portrait
from reportlab.lib.colors import PCMYKColor, PCMYKColorSep, Color, black, blue, red

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
        self.type = tk.StringVar()
        if kind is not None:
            self.type.set(kind)
        self.content = content or ""
        #TODO: Make these options later
        self.font = 15
        self.offset=0.25*self.font
        self.top_offset=150
        
    def set_type(self, type_index):
        self.type.set(self.TYPES[type_index])
    
    def set_content(self, content):
        self.content = content
        
    def get_content(self):
        return self.content

    def get_type(self):
        return self.type
    
    def generate_pdf_page(self, width, height):
        if self.type == self.TYPES[self.TEXT_INDEX]:
            packet = StringIO.StringIO()
            main_canvas = canvas.Canvas(packet, (width, height))
            main_canvas.setFillColorRGB(1,0,0,alpha=0.25)
            main_canvas.setFont("Helvetica-Bold", self.font)
            main_canvas.drawString(50, self.top_offset, self.content)
            main_canvas.save()
            
            return PdfFileReader(packet)
            
            
            
            
            
            
            
            
            
            