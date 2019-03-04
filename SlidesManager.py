import random

def f5(seq, idfun=None):
   # order preserving
   if idfun is None:
       def idfun(x): return x
   seen = {}
   result = []
   for item in seq:
       marker = idfun(item)
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

def score(slide1, slide2):
  AMinusB = slide1.getTags().difference(slide2.getTags()).__len__()
  AnB = slide1.getTags().intersection(slide2.getTags()).__len__()
  APlusB = slide2.getTags().difference(slide1.getTags()).__len__()
  if slide1.getPhotoIds() == slide2.getPhotoIds():
      return 0;
  min = smallest(AMinusB, AnB, APlusB)
  return min

def findbest(slide1, slidesArr, slide_already_selected):
  dic = {}
  for idx, slide in slidesArr.items():
      if slide.getPhotoIds() in slide_already_selected:
          continue
      dic[score(slide1, slide)] = idx
  return dic

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

def getBestSlide(lastSlide, remainingSlides):
    dic = {}
    localSlides = (remainingSlides)
    for slide in localSlides:
        dic[score(lastSlide, slide)] = slide
    selectedId = max(dic.keys())
    return dic[selectedId]

def getInterestingSequenceWithList(slidesArr):
  slides =[]
  i = 1
  remainingSlides = slidesArr.copy()
  selectedId = 0
  lastSlide = remainingSlides[selectedId]
  slides.append(lastSlide)
  remainingSlides.pop(selectedId)
  print("Total " + str(remainingSlides.__len__()) + " slides")
  while remainingSlides:
      print("Comparing " + str(i) + " with " + str(remainingSlides.__len__()) + " slides")
      lastSlide = getBestSlide(lastSlide, remainingSlides);
      slides.append(lastSlide)
      remainingSlides.remove(lastSlide)
      p = 100 * int(i)/(slidesArr.__len__())
      i += 1
      print("Done " + str(i) + " Percent: " + str(format(p, '.2f')) + "%")
  return slides
