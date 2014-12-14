#http://stackoverflow.com/questions/21113773/pdfminer-iterating-through-pages-and-converting-them-to-text
from PyPDF2 import PdfFileReader
#from pyPdf import PdfFileReader
#from PyPDF2.pdf import PageObject
#from PyPDF2.generic import RectangleObject
#PDF = PdfFileReader(file("docs/doc3.pdf", 'rb'))
#PDF = PageObject(PdfFileReader)

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

class ScaledPage():

    def __init__(self,key):
        global sizes
        self.key=key
        minval=round(min(sizes[key]),3)
        maxval=round(max(sizes[key]),3)
        self.scalePageMin=round(min(sizes[key]),3)
        self.scalePageMax=max(sizes[key])
        self.scalePageLandscapeHeight=minval
        self.scalePageLandscapeWidth=maxval
        self.scalePagePortraitHeight=maxval
        self.scalePagePortraitWidth=minval

    def getKey(self):
        return self.key

    def scalePageLandscapeHeight(self):
        return self.scalePageLandscapeHeight

    def scalePageLandscapeWidth(self):
        return self.scalePageLandscapeWidth

    def scalePagePortraitHeight(self):
        return self.scalePagePortraitHeight

    def scalePagePortraitWidth(self):
        return self.scalePagePortraitHeight

    def smartScale(self,page):
        pass



class PDF(PdfFileReader,ScaledPage):


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
        tolerance=0.5
        for x in range(self.getNumPages()):
            rect=self.getPage(x).trimBox
            #print str(min(rect[2:])/72)," ", max(rect[2:])/72
            if abs(min(rect[2:])/72-sizes[pageSize][0])<=tolerance and abs(max(rect[2:])/72-sizes[pageSize][1])<=tolerance:
                results.append(x+1)
            else:
                pass
        return results


    def samePageSize(self,pageSize):

        global sizes
        global key
        tolerance=0.5
        j=0
        rect=self.getPage(pageSize).trimBox
        print str(rect[2]/72)+ str(rect[3])+ str(sizes[key][0])+ str(sizes[key][1])
        return abs(min(rect[2:])/72-sizes[key][0])<=tolerance and abs(max(rect[2:])/72-sizes[key][1])<=tolerance:



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

    def scalePage(self,page):
        global key
        global sizes



sizes={"A":(8.5,11),
   "B":(11,17),
   "C":(17,22),
   "D":(22,34),
   "E":(34,44),
   "F":(28,40)
   }

key="A"

pdf = PDF(open("docs/test.pdf", "rb"))

print pdf.samePageSize(0)

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