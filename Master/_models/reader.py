import PyPDF2 as pypdf2

class StampPDFReader(pypdf2.PdfFileReader):
    #uses super init function
    def getPagesOfSize(self, pageSize):
        return []