class Stamp(object):
    """
    A stamp can be either a text stamp or an icon.
    It is what will be appended to a generated PDF in
    order to produce the marked pages.
    """
    def __init__(self, text="", image_path = ""):
        self.text = text
        self.image_path = image_path
        self.height = "2cm" #will be required for reportlab

    def get_height(self):
        return self.height

        
    
        