#http://stackoverflow.com/questions/21113773/pdfminer-iterating-through-pages-and-converting-them-to-text
from PyPDF2 import PdfFileReader
#from pyPdf import PdfFileReader
#from PyPDF2.pdf import PageObject
#from PyPDF2.generic import RectangleObject
#PDF = PdfFileReader(file("docs/doc3.pdf", 'rb'))
#PDF = PageObject(PdfFileReader)

#PDF = PageObject(PdfFileReader, file("docs/doc3.pdf", 'rb'))

#Brian Changed Pypdf2 generic __repr__


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

    def isPageSize(self,pageSize):

        sizes={"A":(8.5,11),
           "B":(11,17),
           "C":(17,22),
           "D":(22,34),
           "E":(34,44),
           "F":(28,40)
           }

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

        #     #print "Page Number"+ str(j+1)
        #     if string.upper() in text[j].upper():
        #         #print j+1
        #         results.append(j+1)
        #         j+=1
        #     else:
        #         j+=1
        # return results

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

    def scalePageLandscapeHeight(self,page):
        pass
    def scalePageLandscapeWidth(self,page):
        pass
    def scalePagePortraitHeight(self,page):
        pass
    def scalePagePortraitWidth(self,page):
        pass

    def smartScale(self,page):
        pass

    def andFilter(self,list1,list2):
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

    def orFilter(self,list1,list2):
        newlist=sorted(list(set(list1+list2)))
        return newlist

        def pages_to_stamp(self, crit1, crit2,condition):
            pass

#tup1=("text","Machine shop")
#tup2=('page', 'size')

#tup1=("dfs","sdf")
#tup2=("","")

#condition="and"

pdf = PDF(open("docs/doc3.pdf", "rb"))


#text=pdf.getPagesize()
#text=pdf.containsTextReturnList("Machine Shop")
#text=pdf.pageOrientation()
#text=pdf.currentPageLandscapeHeight(2)

crit1=pdf.isPageSize("A")
crit2=pdf.containsTextReturnList("Machine Shop")

pages=pdf.orFilter(crit1,crit2)

print pages

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