from tkinter_helper import TkStampManager

###VARIABLES
PDF_FILES = ['test_pdfs/doc3.pdf']

COPIES = []

def main():
    root = TkStampManager(COPIES)
    root.tk_set_input_options()
    root.run_mainloop()
    
if __name__=="__main__":
    main()
