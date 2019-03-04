from slide import Slide
from util import *

def getBestPair(lastPhoto, remainingPhotos):
    dic = {}
    localPhotos = random_subset(remainingPhotos, Parameters.VerticalSamplePortion)
    for photo in localPhotos:
        dic[scorePhotos(lastPhoto, photo)] = photo
    selectedId = max(dic.keys())
    bestPhoto = dic[selectedId]
    photo = Slide(str(lastPhoto.getId()) + " " + str(bestPhoto.getId()), 'V', list([lastPhoto, bestPhoto]))
    return photo

def getVPairs(photoArr):
  slides =[]
  i = 1
  remainingPhotos = list(photoArr.copy().values())
  random.shuffle(remainingPhotos)
  selectedId = 0
  print("Total " + str(remainingPhotos.__len__()) + " vertical photos")
  while remainingPhotos:
      print("Comparing " + str(i) + " with " + str(remainingPhotos.__len__()) + " vertical photos")
      lastPhoto = remainingPhotos[selectedId]
      slide = getBestPair(lastPhoto, remainingPhotos);
      slides.append(slide)
      remainingPhotos.remove(slide.getPhotos()[0])
      remainingPhotos.remove(slide.getPhotos()[1])

      p = 100 * int(i)/(photoArr.__len__())
      i += 1
      print("Done " + str(i) + " Percent: " + str(format(p, '.2f')) + "%")
  return slides
