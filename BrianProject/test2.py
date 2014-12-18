from PyPDF2 import PdfFileWriter, PdfFileReader
import StringIO
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter, legal, elevenSeventeen, landscape,portrait
from reportlab.lib.colors import PCMYKColor, PCMYKColorSep, Color, black, blue, red

import time
from datetime import date

today=date.today()


#WORKS RIGHT NOW

packet = StringIO.StringIO()

# create a new PDF with Reportlab
can = canvas.Canvas(packet, pagesize=portrait(letter))

textobject = can.beginText()
textobject.setTextOrigin(0, 0)
textobject.setFont("Helvetica-Bold", 14)
textobject.textLines('''
With many apologies to the Beach Boys
and anyone else who finds this objectionable
''')
packet.seek(0)
#move to the beginning of the StringIO buffer

new_pdf = PdfFileReader(packet)
# read your existing PDF
#existing_pdf = PdfFileReader(file("docs/doc3.pdf", "rb"))
existing_pdf = PdfFileReader(file("docs/wordtest.pdf", "rb"))


output = PdfFileWriter()


# page = existing_pdf.getPage(0)
# page.scaleBy(2)
# output.addPage(page)

page = existing_pdf.getPage(0)
page.mergePage(new_pdf.getPage(0))
output.addPage(page)


# finally, write "output" to a real file
outputStream = file("output/out44.pdf", "wb")
output.write(outputStream)
outputStream.close()

