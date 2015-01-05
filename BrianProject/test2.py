from PyPDF2 import PdfFileWriter, PdfFileReader
import StringIO
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter, legal, elevenSeventeen, landscape,portrait

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

can.setFillColorRGB(1,0,0)
#canvas.setStrokeColor(red)
can.setFont("Helvetica-Bold", font)

can.drawString(50, top_offset, "ISSUED FOR CONSTRUCTION")
can.drawString(50,top_offset-font-offset, "BY_____________________")
can.drawString(50,top_offset-2*font-2*offset, str(today))
can.save()

#move to the beginning of the StringIO buffer
packet.seek(0)
new_pdf = PdfFileReader(packet)
# read your existing PDF
existing_pdf = PdfFileReader(file("docs/doc3.pdf", "rb"))
output = PdfFileWriter()
# add the "watermark" (which is the new pdf) on the existing page



i=0
#getPage(2).mediaBox[0]
dimension=[]

for x in range(existing_pdf):
    singlePage = existing_pdf.getPage(i)
    output.addPage(singlePage)
    i=i+1

# finally, write "output" to a real file
outputStream = file("output/out9.pdf", "wb")
output.write(outputStream)
outputStream.close()

