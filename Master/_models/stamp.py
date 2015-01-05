try:
    from tkinter import StringVar
except:
    from Tkinter import StringVar

class Stamp(object):
    TEXT_INDEX=0
    IMAGE_INDEX=1
    TYPES = [
             "Text Stamp",
             "Image Stamp", 
             ]
    def __init__(self, type=None, content=None):
        self.type = type or StringVar()
        self.content = content or ""
        
    def set_type(self, option):
        self.type = self.TYPES[option]
    
    def set_content(self, content):
        self.content = content
        
    def get_content(self):
        return self.content

    def get_type(self):
        return self.type