from reader import StampPDFReader

class Copy(object):
    def __init__(self, reader_filestream=None, filter1=None, filter2=None, condition=None, stamp_dict = {}):
        self.pdf = StampPDFReader(open(str(reader_filestream), 'rb'))
        self.filter1 = filter1
        self.filter2 = filter2
        self.condition = condition
        self.stamp_dict = stamp_dict
        self.outputPages = []
        
    def get_filter1(self):
        return self.filter1
    def get_filter2(self):
        return self.filter2
    def get_condition(self):
        return self.condition
    def get_stamp_dict(self):
        return self.stamp_dict
    
    def count_stamps(self):
        #Temporary: to be replaced with a default copy item created on main/loaded from json object
        return 1
        
        return len(self.stamp_dict.keys())