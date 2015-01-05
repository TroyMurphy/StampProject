import PyPDF2 as pypdf2

class StampPDFReader(pypdf2.PdfFileReader):
    #uses super init function
    
    def getPagesOfSize(self, pageSize):
        return []
    
    
class StampPDFWriter(pypdf2.PdfFileWriter):
    
    def insert_title_page(self, title_text):
        return 0