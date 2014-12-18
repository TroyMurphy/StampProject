from PyPDF2 import PdfFileWriter, PdfFileReader
from pdfminer.pdfparser import PDFParser
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfdocument import PDFDocument
import StringIO
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter, legal, elevenSeventeen, landscape,portrait
from reportlab.lib.colors import PCMYKColor, PCMYKColorSep, Color, black, blue, red



class PDF(PdfFileReader):
    def getPageRotation(self,pageindex):
        rotation=self.getPage(pageindex)['/Rotate']
        return rotation


newerPdf = PDF(file("docs/doc3.pdf", "rb"))

#test=newerPdf.getPage(9)
test=newerPdf.getPageRotation(9)
print test
