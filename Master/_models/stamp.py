class Stamp(object):
    TYPES = {
             "Text Stamp":0,
             "Image Stamp":1, 
             }
    def __init__(self, type=None):
        self.type = type
        self.content = ""
        
    def set_type(self, option):
        self.type = self.TYPES[option]
    
    def set_content(self, content):
        self.content = content
        
    def get_content(self):
        return self.content

    def get_type(self):
        return self.type