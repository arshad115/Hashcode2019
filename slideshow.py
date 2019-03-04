class SlideShow:
    def __init__(self, slides):
        self.slides = slides
    def saveOutput(self, filename):
        print("Starting slideshow file output: " + filename)
        file = open("outputs/output-" + filename + ".txt", "w")
        slidesFile = open("outputs/slides-" + filename + ".txt", "w")
        print("Total slides: " + str(self.slides.__len__()))

        file.write(str(self.slides.__len__()) + "\n")
        slidesFile.write(str(self.slides.__len__()) + "\n")
        for slide in self.slides:
            file.write(slide.getPhotoIds() + "\n")
            slidesFile.write(str(slide) + "\n")
        file.close()
        slidesFile.close()
        print("Done writing file")
