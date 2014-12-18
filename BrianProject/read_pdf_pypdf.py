#http://stackoverflow.com/questions/21113773/pdfminer-iterating-through-pages-and-converting-them-to-text
from PyPDF2 import PdfFileReader, PdfFileWriter
from decimal import *
import StringIO
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter, legal, elevenSeventeen, landscape,portrait
from reportlab.lib.colors import PCMYKColor, PCMYKColorSep, Color, black, blue, red
from math import sqrt



#PDF = PageObject(PdfFileReader, file("docs/doc3.pdf", 'rb'))

#Brian Changed Pypdf2 generic __repr__

class PageFilters():
    def __init__(self,list1,list2):
        self.list1=list1
        self.list2=list2

    def getlist1(self):
        return self.list1

    def getlist2(self):
        return self.list2

    def andFilter(self):
        list1=self.getlist1()
        list2=self.getlist2()
        results=[]
        j=0
        for x in list1:
            if x in list2:
                #print x
                results.append(list1[j])
                j+=1
            else:
                j+=1
        mylist=list(set(results))

        return sorted(mylist)

    def orFilter(self):
        list1=self.getlist1()
        list2=self.getlist2()

        newlist=sorted(list(set(list1+list2)))
        return newlist


class PDF(PdfFileReader):

    def getText(self):
        #return list of pages text string
        i=0
        content=[]
        for page in self.pages:
            content.append(self.getPage(i).extractText())
            i += 1
        return content

    def containsTextReturnList(self, string):
        results=[]
        j=0
        text=self.getText()
        for x in range(self.getNumPages()):
            #print "Page Number"+ str(j+1)
            if string.upper() in text[j].upper():
                #print j+1
                results.append(j+1)
                j+=1
            else:
                j+=1
        return results

    def noFilter(self):
        result=[]
        return result

    def findSamePageSizes(self,pageSize):

        global sizes
        results=[]
        j=0
        #tolerance that pagesize is allowed to be
        tolerance=0.1
        for x in range(self.getNumPages()):
            rect=self.getPage(x).trimBox
            #tester=float(rect[3])/72
            #print tester
            if abs(min(rect[2:])/72-sizes[pageSize][0])<=tolerance and abs(max(rect[2:])/72-sizes[pageSize][1])<=tolerance:
                results.append(x+1)
            else:
                pass
        return results

    # def samePageSize(self,pageSize):
    #
    #     global sizes
    #     global key
    #     tolerance=0.5
    #     j=0
    #     rect=self.getPage(pageSize).trimBox
    #
    #     if abs(min(rect[2:])/72-sizes[key][0])<=tolerance and abs(max(rect[2:])/72-sizes[key][1])<=tolerance:
    #         #print str(rect[2]/72)+ str(rect[3])+ str(sizes[key][0])+ str(sizes[key][1])
    #         return True
    #     else:
    #         #print str(rect[2]/72)+" "+ str(rect[3]/72)+" "+ str(sizes[key][0])+" "+ str(sizes[key][1])
    #         return False

    def scaleListOfPagesToCertainSize(self,listOfPages,dictkey):
        #returns a list with each entry being a page object

        if dictkey=="None":

            #print "Dict key is none"
            scaledPages=[]

            for x in listOfPages:
                page=self.getPage(x-1)
                scaledPages.append(page)
            return scaledPages
        else:
            scaledPages=[]

            for x in listOfPages:

                page=self.getPage(x-1)
                scale=self.findScalingFactorForPageIndex(x,dictkey)
                #print scale
                page.scaleBy(scale)
                scaledPages.append(page)
            return scaledPages

    def findScalingFactorForPageIndex(self,page,newdictkey):
        global key
        key=newdictkey
        global sizes
        global scaledPageMax
        global scaledPageMin

        if abs(scaledPageMax/self.currentPageLandscapeWidth(page)-1)>abs(scaledPageMin/self.currentPageLandscapeHeight(page)-1):
        #    print self.currentPageLandscapeWidth(page)
        #    print scaledPageMax

            scaleFactor=float(scaledPageMax)/float(self.currentPageLandscapeWidth(page))

        else:
            #print self.currentPageLandscapeWidth(page)
            #print scaledPageMax
            scaleFactor=float(scaledPageMin)/float(self.currentPageLandscapeHeight(page))
        #print scaleFactor
        return scaleFactor





    def isLandscape(self,page):
        rect=self.getPage(page-1).trimBox
        if rect[2]>rect[3]:
            return True
        elif rect[2]<rect[3]:
            return False
        else:
            pass

    def isPortrait(self,page):
        rect=self.getPage(page-1).trimBox
        if rect[2]<rect[3]:
            return True
        elif rect[2]>rect[3]:
            return False
        else:
            pass



    def currentPageLandscapeHeight(self,page):
        rect=self.getPage(page-1).trimBox
        return min(rect[2],rect[3])/72

    def currentPageLandscapeWidth(self,page):
        rect=self.getPage(page-1).trimBox
        return max(rect[2],rect[3])/72

    def currentPagePortraitHeight(self,page):
        rect=self.getPage(page-1).trimBox
        return max(rect[2],rect[3])/72

    def currentPagePortraitWidth(self,page):
        rect=self.getPage(page-1).trimBox
        return min(rect[2],rect[3])/72

    def getPageRotationFromPageObject(self):
        rotation=self['/Rotate']
        return rotation

    def getPageObjectHeight(self):
        height=self.mediaBox[3]
        return height

    # def createTitlePage(self,title,description):
    #         global output
    #         packet = StringIO.StringIO()
    #         can = canvas.Canvas(packet, pagesize="letter")
    #         #titlePage=PDF(open("blank_page.pdf", "rb"))
    #         titleStampPage=self.getPage(0)
    #         font=25
    #         offset=0.25*font
    #         top_offset=0
    #
    #         can.setFillColorRGB(1,0,0,alpha=0.75)
    #         #canvas.setStrokeColor(red)
    #         can.setFont("Helvetica-Bold", font)
    #
    #         can.drawString(40,200, title)
    #         can.drawString(40,150, description)
    #         #can.drawString(0,top_offset-2*font-2*offset, "HOLA")
    #         can.save()
    #         packet.seek(0)
    #         new_pdf = PdfFileReader(packet)
    #
    #         titleStampPage.mergePage(new_pdf.getPage(0))
    #         output.addPage(titleStampPage)


    def createCoverPage(self,title,description):
        global output
        packet = StringIO.StringIO()
        # create a new PDF with Reportlab
        can = canvas.Canvas(packet, pagesize=letter)
        existing_pdf=self.getPage(0)
        font=15
        offset=0.25*font
        top_offset=700

        can.setFillColorRGB(1,0,0,alpha=1)
        #canvas.setStrokeColor(red)
        can.setFont("Helvetica-Bold", font)

        can.drawString(50, top_offset, title)
        can.drawString(50,top_offset-font-offset, description)
        can.save()

        #move to the beginning of the StringIO buffer

        new_pdf = PdfFileReader(packet)
        # read your existing PDF
        #existing_pdf = PdfFileReader(file("docs/doc3.pdf", "rb"))
        #existing_pdf = PdfFileReader(file("output/out14.pdf", "rb"))


        existing_pdf.mergePage(new_pdf.getPage(0))
        output.addPage(existing_pdf)

    def stampPages(self,listOfPageObjects):
    #def stampPages(self,listOfPageObjects,filepath):
        #output = PdfFileWriter()
        global output
        j=0
        stampedPages=[]

        for page in listOfPageObjects:
            packet = StringIO.StringIO()

            existingPdfPage=page

            dimensionCurrentPdfPage=(existingPdfPage.trimBox[2]*72,existingPdfPage.trimBox[3]*72)
            can = canvas.Canvas(packet, dimensionCurrentPdfPage)

            font=25
            offset=0.25*font
            top_offset=0

            can.setFillColorRGB(1,0,0,alpha=0.75)
            #canvas.setStrokeColor(red)
            can.setFont("Helvetica-Bold", font)

            can.drawString(30, 30, "ISSUED FOR CONSTRUCTION")
            #can.drawString(0,top_offset-font-offset, "BY_____________________")
            #can.drawString(0,top_offset-2*font-2*offset, "HOLA")
            can.save()
            packet.seek(0)
            new_pdf = PdfFileReader(packet)

            existingPdfPage.mergePage(new_pdf.getPage(0))
            output.addPage(existingPdfPage)

            if '/Rotate' in page:
                #print True
                rotationAngle=page['/Rotate']
            else:
                #print False
                rotationAngle=0

            if rotationAngle==0:
                existingPdfPage.mergePage(new_pdf.getPage(0))
                output.addPage(existingPdfPage)
            elif rotationAngle !=0:
                pageHeight=existingPdfPage.trimBox[3]
                translatePageDown=(float(pageHeight)/72)*25.4*sqrt(2)


                existingPdfPage.mergeRotatedTranslatedPage(new_pdf.getPage(0),rotation=90,tx=translatePageDown,ty=translatePageDown)
                output.addPage(existingPdfPage)

        # outputStream = file(filepath, "wb")
        # output.write(outputStream)
        # outputStream.close()



    # def createOutputOfPages(self,pageObject,outputFilePath):
    #     #Last step after all copies have been made to create final file from all pages in global output variable
    #
    #     global output
    #     for x in pageObject:
    #         output.addPage(x)
    #     outputStream = file(outputFilePath, "wb")
    #     output.write(outputStream)
    #     outputStream.close()




sizes={
        "None":(0,0),
        "A":(8.5,11),
        "B":(11,17),
        "C":(17,22),
        "D":(22,34),
        "E":(34,44),
        "F":(28,40)
        }

key="A"

scaledPageMax=sizes[key][1]
scaledPageMin=sizes[key][0]


#
pdf = PDF(open("docs/doc3.pdf", "rb"))
copyCover=PDF(open("blank_page.pdf", "rb"))

#GLOBAL VARIABLE
output = PdfFileWriter()
OUTPUT_FILE_PATH="output/d32.pdf"
#
#
crit1=pdf.findSamePageSizes("B")
#crit1=pdf.noFilter()
crit2=pdf.containsTextReturnList("BECKET")

filter=PageFilters(crit1,crit2)
list=filter.andFilter()


#pdf.createTitlePage("Machine Shop","Contains MS and page 8.5")
outputPages=pdf.scaleListOfPagesToCertainSize(list,"None")

#titlePage=PDF(open("blank_page.pdf", "rb"))
#titlePage.createTitlePage("test","test2")

coverPage=copyCover.createCoverPage("Machine Shop Copy","This is the machine shop")
outputPdf=pdf.stampPages(outputPages)


outputStream = file(OUTPUT_FILE_PATH, "wb")
output.write(outputStream)
outputStream.close()

#output=pdf.stampPages([pdf.getPage(2)],"output/d14.pdf")

#END


# crit1=pdf.findSamePageSizes("A")
# #crit1=pdf.noFilter()
# crit2=pdf.containsTextReturnList("Machine Shop")
#
# filter=PageFilters(crit1,crit2)
# list=filter.orFilter()









# pdf = PDF(open("docs/doc3.pdf", "rb"))


# text =ScaledPage("A")
#
# test=text.scalePageMin
#
# print test

#text=pdf.getPagesize()
#text=pdf.containsTextReturnList("Machine Shop")
#text=pdf.pageOrientation()
#text=pdf.currentPageLandscapeHeight(2)

#START TEST

# pdf = PDF(open("docs/doc3.pdf", "rb"))
#
# crit1=pdf.findSamePageSizes("A")
# #crit1=pdf.noFilter()
# crit2=pdf.containsTextReturnList("Machine Shop")
#
# filter=PageFilters(crit1,crit2)
#
# print filter.andFilter()

#END TEST


#print text
#text=pdf.getText()


#rect=pdf.getPage(6).mediaBox.getHeight()
#print rect


#text=pdf.getPage(6).mediabox
#print text


pageSize={"A":(8.5,11),
           "B":(11,17),
           "C":(17,22),
           "D":(22,34),
           "E":(34,44),
           "F":(28,40)
           }

#print pageSize["A"]

#A 8.5 11
#B 11 17
#C 17 22
#D 22 34
#C1 24 36
#E 34 44
#F 28 40
#
#A0 841 1189
#A1 594 841
#A2 420 594
#
#
#