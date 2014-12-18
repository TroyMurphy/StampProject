from multiprocessing import Condition
class Copy(object):
    def __init__(self, reader, filter1, filter2, condition,
                 stamp_dict):
        self.pdf = reader
        self.filter1 = filter1
        self.filter2 = filter2
        self.condition = condition
        self.stamp_dict = stamp_dict
        self.outputPages = []