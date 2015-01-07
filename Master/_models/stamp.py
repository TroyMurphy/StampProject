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
        
    def set_type(self, type_index):
        self.type.set(self.TYPES[type_index])
    
    def set_content(self, content):
        self.content = content
        
    def get_content(self):
        return self.content

    def get_type(self):
        return self.type