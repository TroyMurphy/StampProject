from PyPDF2 import PdfFileReader
from _dbus_bindings import String


class WorksheetPDF(PdfFileReader):
    """
    A subclass of PdfFileReader
    Allows searching of strings and can flag other important attributes 
    """
    def __init__(self, path):
        #for 2.7
        #self.PDF = super(WorksheetPDF, self).__init__(file(path, 'rb'))
        
        #for 3
        self.PDF = super().__init__(file(path, 'rb'))
        self.pages = []
        self.return_pages= []
		
        self.decrypt()
        self.populate_pages()
        
    def decrypt(self):
        decrypt_ret = self.PDF.decrypt('')
        if decrypt == 0:
            #handle no password.
            # TODO: create prompt for password
            print "Password Protected PDF: " + pdf_fp
            raise Exception("Password Protected Error")
        elif decrypt == 1 or decrypt == 2:
            print "PDF successfully decrypted with status " + decrypt 
    
    def populate_pages(self):
        for page in self.PDF.pages:
            self.pages.append(page.extractText())
		
    def pages_with_string(self, search_string):
        #for detail, search for list comprehensions
        #returns a list of indexes of pages which contain search string
        #0 <= indexes <= #pages-1)
        self.return_pages += [i for i in range(len(self.pages)) if search_string in self.pages[i]]
	
	def pages_with_size(self, page_size):
		self.return_pages += [i for i in range(len(self.pages)) if page_size == "8x11"]
		
	def run(self, filter1,):
		pass
		
