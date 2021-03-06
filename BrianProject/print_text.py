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
can = canvas.Canvas(packet, pagesize=letter)

font=15
offset=0.25*font
top_offset=150

can.setFillColorRGB(1,0,0,alpha=0.25)
#canvas.setStrokeColor(red)
can.setFont("Helvetica-Bold", font)

can.drawString(50, top_offset, "ISSUED FOR CONSTRUCTION")
can.drawString(50,top_offset-font-offset, "BY_____________________")
can.drawString(50,top_offset-2*font-2*offset, str(today))
can.save()

#move to the beginning of the StringIO buffer

new_pdf = PdfFileReader(packet)
# read your existing PDF
existing_pdf = PdfFileReader(file("docs/doc3.pdf", "rb"))
#existing_pdf = PdfFileReader(file("output/out14.pdf", "rb"))

output = PdfFileWriter()


page = existing_pdf.getPage(0)
page.scaleBy(2)
output.addPage(page)

page = existing_pdf.getPage(1)
page.mergePage(new_pdf.getPage(0))
output.addPage(page)




# finally, write "output" to a real file
outputStream = file("output/out.pdf", "wb")
output.write(outputStream)
outputStream.close()

