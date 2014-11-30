#http://stackoverflow.com/questions/21113773/pdfminer-iterating-through-pages-and-converting-them-to-text
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




def contains_text(list,string):
    results=[]
    for x in list:
        if string in list[x]:
            results[x]=1
        else:
            results[x]=0
    return results


