class Photo:
    def __init__(self, id, orientation, nTags, tags):
        self.id = id
        self.orientation = orientation
        self.nTags = nTags
        # sorted(tags)
        self.tags = (tags)
    def __str__(self):
        return self.orientation + ", " + self.nTags + ", "  + ' '.join(map(str, self.tags))
    def getId(self):
        return self.id
    def getTags(self):
        return self.tags
    def getTagsLen(self):
        return self.nTags