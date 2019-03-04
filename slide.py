from photo import Photo

class Slide:
    # Each slide contains orientation(is h or v), photos and common tags
    def __init__(self,ids, orientation, photos):
        self.ids = ids
        self.orientation = orientation
        self.photos = photos
    def __str__(self):
        return self.orientation + ", " + ' '.join(map(str, self.photos))
    def getTags(self):
        if(self.orientation == 'H'):
            p = self.photos[0]
            return p.getTags()
        else:
            p1 = self.photos[0].getTags()
            p2 = self.photos[1].getTags()
            commonTags = p1.union(p2)
            return commonTags
    def getSlidesLen(self):
        return self.tags.__len__()
    def getPhotoIds(self):
        return self.ids
    def getOrientation(self):
        return self.orientation