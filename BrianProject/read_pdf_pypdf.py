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

    def getPageSizeAtIndex(self, index):
        pass

    def getText(self):
        #return list of pages text string
        i=0
        content=[]
        for page in self.pages:
            content.append(self.getPage(i).extractText())
            i += 1
        return content

    def getPagesize(self):
        i=0
        #getPage(2).mediaBox[0]
        dimension=[]

        for x in range(self.getNumPages()):
            rect=self.getPage(i).trimBox

            #dimension.append((rect.[2], rect.[3]))
            dimension.append((rect[2], rect[3]))
            #dimension.append((rect.width, rect[3]))
            i=i+1
        return dimension

    def pageOrientation(self):
        i=0
        dimension=[]

        for x in range(self.getNumPages()):
            rect=self.getPage(i).trimBox
            if rect[2]>=rect[3]:
                dimension.append("l")
            elif rect[2]<rect[3]:
                dimension.append("p")
            else:
                dimension.append("?")
            i=i+1
        return dimension

    def contains_text(self, list, string):
        results=[]

        for x in list:
            if string.upper() in x.upper():
                results.append(1)
    #            print"True"
            else:
                results.append(0)
    #            print"false"
        return results

    # def containsTextReturnList(self, string):
    #     results=[]
    #     i=1
    #     j=0
    #     text=self.getText()
    #     for x in text():
    #         if string.upper() in text[j].upper():
    #             results.append(i)
    #             i+=1
    #             j+=1
    # #            print"True"
    #         else:
    #             pass
    #     return results

    def and_filter(self,list1,list2):
        filtered=[]
        for x in list1:
            filtered.append(x*list2[x])
        return filtered

    def or_filter(self,list1,list2):
        filtered=[]
        i=0
        for x in list1:
            if (x or list2[i])==1:
                filtered.append(1)
                i += 1
            else:
                filtered.append(0)
                i += 1
        return filtered

    def criteria(self,tuple):
    #return list of each critera for text or pagesize
        if not (tuple[0] or tuple[1]):
            list1=[1]*self.getNumPages()
            return list1
        #    print "exit1"
        if tuple[0]=="text":
            results=[]
            for x in self.getText():
                if tuple[1].upper() in x.upper():
                    results.append(1)
        #            print"True"
                else:
                    results.append(0)
        #            print"false"
            return results
        if tuple[0]=="page":
            #write code to return pagesize

            pass

        else:
            list1=[1]*self.getNumPages()
            return list1

    def what_to_stamp(self,crit1,crit2,condition):

        pass
        #If crit1 or input1 is null


    def pages_to_stamp(self, crit1, crit2,condition):
        pass

#tup1=("text","Machine shop")
#tup2=('page', 'size')

#tup1=("dfs","sdf")
#tup2=("","")

#condition="and"

pdf = PDF(open("docs/doc3.pdf", "rb"))


#text=pdf.getPagesize()
text=pdf.containsTextReturnList("Machine Shop")
#text=pdf.pageOrientation()
print text

#rect=pdf.getPage(6).mediaBox.getHeight()
#print rect


#text=pdf.getPage(6).mediabox
#print text


#text= pdf.contains_text(pdf.getText(),"Machine")




#abba= pdf.getPagesize()
#print abba

#abba=pdf.getPagesize()
#print abba
#print len(abba)


#getLowerLeft_x


#text= pdf.what_to_stamp(tup1,tup2,condition)
#print text

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