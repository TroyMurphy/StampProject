from PyPDF2 import PdfFileReader
from reportlab.lib.pagesizes import letter


PDF = PdfFileReader(file("docs/doc3.pdf", 'rb'))

print PDF.getPage(0).mediaBox
print PDF.getPage(3).mediaBox


def is_pagesize(list,string):
    results=[]
    for x in list:
        if string.upper() in x.upper():
            results.append(1)
#            print"True"
        else:
            results.append(0)
#            print"false"
    return results
