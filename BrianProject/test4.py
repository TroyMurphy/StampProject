#http://stackoverflow.com/questions/21113773/pdfminer-iterating-through-pages-and-converting-them-to-text
from PyPDF2 import PdfFileReader, PdfFileWriter
from decimal import *
import StringIO
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter, legal, elevenSeventeen, landscape,portrait
from reportlab.lib.colors import PCMYKColor, PCMYKColorSep, Color, black, blue, red
from math import sqrt
from datetime import date


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
        # print results
        # print "results type is "+ str(type(results))
        # mylist=list(set(results))
        mylist=results

        return sorted(mylist)

    def orFilter2(self):
        list1=self.getlist1()
        list2=self.getlist2()

        #newlist=sorted(list(set(list1+list2)))
        newlist=list(sorted(set(list1+list2)))
        #print type(newlist)
        return newlist

    def orFilter(self):
        list1=self.getlist1()
        list2=self.getlist2()
        results=list1
        for i in list2:
            if i not in results:
                results.append(i)
            else:
                pass
        return sorted(results)


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

    def returnListOfAllPages(self):
        numpages=self.getNumPages()
        list=[]
        x=1
        for page in range(numpages):
            list.append(x)
            x+=1
        return list

    def findSamePageSizes(self,pageSize):

        global sizes
        results=[]
        j=0
        #tolerance that pagesize is allowed to be
        tolerance=0.5
        for x in range(self.getNumPages()):
            rect=self.getPage(x).trimBox
            #tester=float(rect[3])/72
            #print tester
            if abs(min(rect[2:])/72-sizes[pageSize][0])<=tolerance and abs(max(rect[2:])/72-sizes[pageSize][1])<=tolerance:
                results.append(x+1)
            else:
                pass
        return results


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
                # Difference between trimbox and media box. Trimbox is original fullsize and mediabox is actual size after scale
                # print "Media box"+str(round(page.mediaBox[2],3))+" "+str(round(page.mediaBox[3],3))
                # print "Trimbox "+str(page.trimBox[2])+" "+str(page.trimBox[3])
                # print "**************"
                scaledPages.append(page)
            return scaledPages

    def findScalingFactorForPageIndex(self,page,newdictkey):
        global key
        key=newdictkey
        global sizes
        global scaledPageMax
        global scaledPageMin

        if abs(scaledPageMax/self.currentPageLandscapeWidth(page)-1)>abs(scaledPageMin/self.currentPageLandscapeHeight(page)-1):

        #    print scaledPageMax

            scaleFactor=float(scaledPageMax)/float(self.currentPageLandscapeWidth(page))

        else:
            #print self.currentPageLandscapeWidth(page)
            #print scaledPageMax
            scaleFactor=float(scaledPageMin)/float(self.currentPageLandscapeHeight(page))
        #Test to see what scale factor is
        # print "Scaled Page Dimensions are "+str(scaledPageMax)+" "+str(scaledPageMin)
        # print "Actual Page Size is "+str(self.currentPageLandscapeWidth(page))+" "+str(self.currentPageLandscapeHeight(page))
        # print "Scale Factor is "+str(scaleFactor)
        # print "************************"
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
        return float(min(rect[2:]))/72

    def currentPageLandscapeWidth(self,page):
        rect=self.getPage(page-1).trimBox
        return float(max(rect[2:]))/72

    def currentPagePortraitHeight(self,page):
        rect=self.getPage(page-1).trimBox
        return float(max(rect[2:]))/72

    def currentPagePortraitWidth(self,page):
        rect=self.getPage(page-1).trimBox
        return float(min(rect[2:]))/72

    def getPageRotationFromPageObject(self):
        rotation=self['/Rotate']
        return rotation

    def getPageObjectHeight(self):
        height=self.mediaBox[3]
        return height

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

        existing_pdf.mergePage(new_pdf.getPage(0))
        output.addPage(existing_pdf)

    #def stampPages(self,listOfPageObjects,xPercentOffset=0.2,yPercentOffset=0.2):
    def stampPages(self,listOfPageObjects,stamps,xPercentOffset=0.2,yPercentOffset=0.2,offset=30):
    #def stampPages(self,listOfPageObjects,filepath):
        #output = PdfFileWriter()
        global output
        j=0
        stampedPages=[]

        for page in listOfPageObjects:
            packet = StringIO.StringIO()

            existingPdfPage=page
            #trimbox gives original page size
            # widthPoints=existingPdfPage.trimBox[2]
            # heightPoints=existingPdfPage.trimBox[3]

            widthPoints=float(existingPdfPage.mediaBox[2])
            heightPoints=float(existingPdfPage.mediaBox[3])

            widthInches=widthPoints/72
            heightInches=heightPoints/72

            widthMill=widthInches*25.4
            heightMill=heightInches*25.4

            widthPoints=widthInches*72
            heightPoints=widthInches*72

            dimensionCurrentPdfPage=(widthInches*72,heightInches*72)
            can = canvas.Canvas(packet, dimensionCurrentPdfPage)

            #Dimensions in
            xcordStampPos=xPercentOffset*widthPoints
            ycordStampPos=yPercentOffset*heightPoints

            # print "Page Dimensions "+str(widthPoints)+" "+str(heightPoints)
            # print "Stamp Location "+str(xcordStampPos)+" "+str(ycordStampPos)
            # print "**************"

            for i in reversed(stamps):

                color=i[0]
                alpha=i[1]
                fontType=i[2]
                fontSize=i[3]
                stampText=i[4]
                can.setFillColor(color,alpha=alpha)
                can.setFont(fontType, fontSize)

                #Dimensions in points
                can.drawString(xcordStampPos, ycordStampPos, stampText)

                ycordStampPos=ycordStampPos+fontSize+offset



            can.save()
            packet.seek(0)
            new_pdf = PdfFileReader(packet)

            # existingPdfPage.mergePage(new_pdf.getPage(0))
            # output.addPage(existingPdfPage)

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

#GLOBAL VARIABLE
output = PdfFileWriter()

INPUT_FILE_PATH="docs/doc3.pdf"
OUTPUT_FILE_PATH="output/d56.pdf"
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
TODAY=str(date.today())
WONUMBER=str(16456)

#############################################
#STEP 0) Choose PDF that will be stamped
#############################################
#
#Select PDF that will be Stamped
#pdf = PDF(open("docs/doc3.pdf", "rb"))
pdf = PDF(open(INPUT_FILE_PATH, "rb"))

#############################################
#STEP 1) List criteria to search for and filter correctly
#############################################

crit1=pdf.findSamePageSizes("A")
#crit1=pdf.noFilter()
crit2=pdf.containsTextReturnList("DXF")

filter=PageFilters(crit1,crit2)
list=filter.andFilter()
#list=filter.orFilter()

#listOfAllPages=pdf.returnListOfAllPages()

#############################################
#STEP 3) Scale all pages to a certain size, or none. Use key from sizes such as "A"

outputPages=pdf.scaleListOfPagesToCertainSize(list,"None")

#############################################
#STEP 4) Create a copy cover page with title and description

copyCover1=PDF(open("blank_page.pdf", "rb"))
coverPage=copyCover1.createCoverPage("Machine Shop Copy","This is the machine shop")

stamps=[

    (red,0.25,"Helvetica-Bold",22,"FOREMAN COPY"),
    (red,0.25,"Helvetica-Bold",22,"FILE COPY"),
    (red,0.25,"Helvetica-Bold",22,"FTI COPY"),
    (red,0.25,"Helvetica-Bold",22,"MACHINE SHOP COPY"),
    (red,0.25,"Helvetica-Bold",22,"BURN TABLE COPY"),
    (red,0.25,"Helvetica-Bold",22,"REFERENCE COPY"),
    (red,0.25,"Helvetica-Bold",22,"SHOP COPY"),
    (red,0.25,"Helvetica-Bold",22,"QA COPY"),
    (red,0.25,"Helvetica-Bold",22,"FABRICATION COPY"),
    (red,0.25,"Helvetica-Bold",22,"VENDOR COPY"),
    (red,0.25,"Helvetica-Bold",9,"APPROVED FOR CONSTRUCTION"),
    (red,0.25,"Helvetica-Bold",9,"BY_______________________"),
    (red,0.25,"Helvetica-Bold",9,"DATE "+TODAY),
    (red,0.25,"Helvetica-Bold",9,"(DESTROY PREVIOUS REVISION"),
    (red,0.25,"Helvetica-Bold",10,"WO# "+WONUMBER),
    (red,0.25,"Helvetica-Bold",12,"CONTROLLED DOCUMENT")
    ]

outputPdf=pdf.stampPages(outputPages,stamps,xPercentOffset=0.1,yPercentOffset=0.15,offset=0)

###############

crit1=pdf.findSamePageSizes("B")
#crit1=pdf.noFilter()
#crit2=pdf.containsTextReturnList("MACHINE SHOP")
crit2=pdf.noFilter()


filter=PageFilters(crit1,crit2)
#list=filter.andFilter()
list=filter.orFilter()

#listOfAllPages=pdf.returnListOfAllPages()

#############################################
#STEP 3) Scale all pages to a certain size, or none. Use key from sizes such as "A"

outputPages=pdf.scaleListOfPagesToCertainSize(list,"None")

#############################################
#STEP 4) Create a copy cover page with title and description

copyCover2=PDF(open("blank_page.pdf", "rb"))
coverPage=copyCover2.createCoverPage("Foreman copy","This is foreman copy")

stamps=[

    (red,0.25,"Helvetica-Bold",15,"SHOP COPY"),
    (red,0.25,"Helvetica-Bold",15,"REFERENCE COPY"),
    (red,0.25,"Helvetica-Bold",8,"APPROVED FOR CONSTRUCTION"),
    (red,0.25,"Helvetica-Bold",8,"BY_______________________"),
    (red,0.25,"Helvetica-Bold",8,"DATE "+TODAY),
    (red,0.25,"Helvetica-Bold",8,"(DESTROY PREVIOUS REVISION"),
    (red,0.25,"Helvetica-Bold",10,"WO# "+WONUMBER),
    ]
outputPdf=pdf.stampPages(outputPages,stamps,xPercentOffset=0.1,yPercentOffset=0.15,offset=0)






#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#DO NOT COPY BELOW LINE

outputStream = file(OUTPUT_FILE_PATH, "wb")
output.write(outputStream)
outputStream.close()
