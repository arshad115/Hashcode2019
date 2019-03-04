import random

from slide import Slide

def f5(seq, idfun=None):
   # order preserving
   if idfun is None:
       def idfun(x): return x
   seen = {}
   result = []
   for item in seq:
       marker = idfun(item)
       # in old Python versions:
       # if seen.has_key(marker)
       # but in new ones:
       if marker in seen: continue
       seen[marker] = 1
       result.append(item)
   return result

def biggest(a, y, z):
    Max = a
    if y > Max:
        Max = y
    if z > Max:
        Max = z
        if y > z:
            Max = y
    return Max

def smallest(a, y, z):
    Min = a
    if y < Min:
        Min = y
    if z < Min:
        Min = z
        if y < z:
            Min = y
    return Min

def random_subset( iterator, K ):
    result = []
    N = 0

    for item in iterator:
        N += 1
        if len( result ) < K:
            result.append( item )
        else:
            s = int(random.random() * N)
            if s < K:
                result[ s ] = item

    return result

def score(photo1, photo2):
  AMinusB = photo1.getTags().difference(photo2.getTags()).__len__()
  AnB = photo1.getTags().intersection(photo2.getTags()).__len__()
  APlusB = photo2.getTags().difference(photo1.getTags()).__len__()
  if photo1.getId() == photo2.getId():
      return 0;
  min = smallest(AMinusB, AnB, APlusB)
  return min

def findbest(photo1, photoArr, pic_already_selected):
  dic = {}
  for idx, photo in photoArr.items():
      if photo.getId() in pic_already_selected:
          continue
      dic[score(photo1, photo)] = idx
  return dic

def getBestSlide(lastSlide, remainingSlides):
    dic = {}
    localSlides = random_subset(remainingSlides, 300)
    for slide in localSlides:
        dic[score(lastSlide, slide)] = slide
    selectedId = max(dic.keys())
    return dic[selectedId]

# Make combinations
def getVPairs(photoArr):
  pic_already_selected = []
  slides =[]
  i = 0
  minPhotolist = {**photoArr}
  print("Total " + str(photoArr.__len__()) + " vertical photos")
  for idx, photo in photoArr.items():
      print("Comparing " + str(idx) + " with " + str(minPhotolist.__len__()) + " vertical photos")
      i += 1
      if idx in pic_already_selected:
          continue
      if len(minPhotolist)==0:
          continue
      listScores = findbest(photo, minPhotolist, pic_already_selected);
      bestPicId = max(listScores, key=listScores.get)
      bestPicId = listScores[bestPicId]
      pic_already_selected.append(photo.getId())
      pic_already_selected.append(bestPicId)
      try:
          del minPhotolist[photo.getId()]
          del minPhotolist[bestPicId]
      except KeyError:
           print("Key " + str(bestPicId) + " not found")
      slide = Slide(str(idx) + " " + str(bestPicId), 'V', list([photoArr[idx], photoArr[bestPicId]]))
      slides.append(slide)
      p = 100 * (int(i) / photoArr.__len__())
      print("Done " + str(idx) + " Percent: " + str(format(p,'.2f')) + "%")
  return slides
