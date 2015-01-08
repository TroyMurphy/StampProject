class CopyListController(object):
    def __init__(self, copyList):
        self.copyList = copyList
        self.filepath = None
        
    def get_all(self):
        return self.copyList
    
    def set_filepath(self, filename):
        self.filepath = filename
    
    def get_selected(self):
        return [c for c in self.copyList if c.shouldPrint.get()]