import PyPDF2 as pypdf2

class StampPDFReader(pypdf2.PdfFileReader):
    
    def get_page_dimensions(self):
        return (0,0)
    
class StampPDFWriter(pypdf2.PdfFileWriter):
    pass