from tkinter_helper import TkStampManager

###VARIABLES
COPIES = []

def main():
    root = TkStampManager(COPIES)
    root.run_mainloop()
    
if __name__=="__main__":
    main()
