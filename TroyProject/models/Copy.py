class Copy(object):
    """
    A copy defines a ruleset whereby given a path
    to a pdf document it can create a new PDF with
    pages which match a given criteria are stamped with
    the provided stamps
    """
    def __init__(self, pdf_file_path,
                 filter1, filter2, condition,
                 stamps):
        self.file_path = pdf_file_path
        self.filter1 = filter1
        self.filter2 = filter2
        self.condition = condition
        self.stamps = stamps
        