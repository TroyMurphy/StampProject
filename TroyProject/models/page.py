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
