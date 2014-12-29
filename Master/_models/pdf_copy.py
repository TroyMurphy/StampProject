try:
    from tkinter import IntVar
except:
    from Tkinter import IntVar

class StampPDFCopy(object):
    def __init__(self, copy_name=None, text_filter_content=None, 
                 size_filter_content=None, condition=None, stamp_dict = {}):
        self.display_name = copy_name.get().upper()
        self.text_filter_content = text_filter_content
        self.size_filter_content = size_filter_content
        self.condition = condition
        self.stamp_dict = stamp_dict
        self.outputPages = []
#        self.shouldPrint = IntVar()
        return self.validate()

    def get_filter1(self):
        return self.filter1
    def get_filter2(self):
        return self.filter2
    def get_condition(self):
        return self.condition
    def get_stamp_dict(self):
        return self.stamp_dict
    def get_name(self):
        return self.display_name
    def get_shouldPrint(self):
        return self.shouldPrint

    def validate(self):
        if (self.condition.get()=="all" or (self.text_filter_content.get() !="" and self.size_filter_content.get()!="")):
            return True
        return False