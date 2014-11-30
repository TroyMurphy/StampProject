from PyPDF2 import PdfFileReader

PDF = PdfFileReader(file("docs/doc3.pdf", 'rb'))

if PDF.isEncrypted:
    decrypt = PDF.decrypt('')
    if decrypt == 0:
        print "Password Protected PDF: " + pdf_fp
        raise Exception("Nope")
    elif decrypt == 1 or decrypt == 2:
        print "Successfully Decrypted PDF"
content=[]

for page in PDF.pages:
    content.append(page.extractText())



print content[1]