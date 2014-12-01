class Stamp(object):
    """
    A stamp can be either a text stamp or an icon.
    It is what will be appended to a generated PDF in
    order to produce the marked pages.
    
    Depending on issue number 1, stamps can have their own vertical and horizontal offset.
    """
    #===========================================================================
    # def __init__(self, text="", image_path = "", x_offset=0, y_offset=0):
    #     self.text = text
    #     self.image_path = image_path
    #===========================================================================
    def __init__(self, text="", image_path = ""):
        self.text = text
        self.image_path = image_path
        