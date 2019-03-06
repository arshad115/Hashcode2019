from slide import Slide
from util import *

def getBestPair(lastPhoto, remainingPhotos):
    dic = {}
    localPhotos = (remainingPhotos[ : Parameters.VerticalSamplePortion]).copy()
    localPhotos.remove(lastPhoto)
    for photo in localPhotos:
        dic[scorePhotos(lastPhoto, photo)] = photo
    selectedId = min(dic.keys())
    bestPhoto = dic[selectedId]
    slide = Slide(str(lastPhoto.getId()) + " " + str(bestPhoto.getId()), 'V', list([lastPhoto, bestPhoto]), lastPhoto.getTagsLen() + bestPhoto.getTagsLen())
    return slide

def getVPairs(photoArr):
  slides =[]
  i = 1
  remainingPhotos = list(photoArr.copy().values())
  # random.shuffle(remainingPhotos)
  remainingPhotos = sorted(remainingPhotos, key=lambda photo: photo.nTags)
  selectedId = 0
  print("Total " + str(remainingPhotos.__len__()) + " vertical photos")
  while remainingPhotos:
      print("Comparing " + str(i) + " with " + str(remainingPhotos.__len__()) + " vertical photos")
      lastPhoto = remainingPhotos[selectedId]
      slide = getBestPair(lastPhoto, remainingPhotos);
      slides.append(slide)
      try:
          remainingPhotos.remove(slide.getPhotos()[0])
          remainingPhotos.remove(slide.getPhotos()[1])
      except:
          print("error with v slide: "+ str(i))

      p = 100 * int(i)/(photoArr.__len__())
      i += 1
      print("Done " + str(i) + " Percent: " + str(format(p, '.2f')) + "%")
  return slides
