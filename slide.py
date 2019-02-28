class Slide:
    # Each slide contains orientation(is h or v), photos and common tags
    def __init__(self, orientation, photos, tags):
        self.orientation = orientation
        self.photos = photos
        self.tags = tags
