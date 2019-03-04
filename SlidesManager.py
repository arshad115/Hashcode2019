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

def score(slide1, slide2):
  AMinusB = slide1.getTags().difference(slide2.getTags()).__len__()
  AnB = slide1.getTags().intersection(slide2.getTags()).__len__()
  APlusB = slide2.getTags().difference(slide1.getTags()).__len__()
  if slide1.getPhotoIds() == slide2.getPhotoIds():
      return 0;
  max = biggest(AMinusB, AnB, APlusB)
  return max
  # print(max)
  # return max

def findbest(slide1, slidesArr, slide_already_selected):
  # ids = []
  dic = {}
  for idx, slide in slidesArr.items():
      if slide.getPhotoIds() in slide_already_selected:
          continue
      # ids.append(idx)
      # dic[idx] = score(slide1, slide)
      dic[score(slide1, slide)] = idx
  return dic

def findbestWithList(slide1, slidesArr, slide_already_selected):
  # ids = []
  dic = {}
  localSlides = slidesArr.copy()
  idx = 0
  while localSlides:
      if slide1 in slide_already_selected:
          dic[0] = 0
          return dic
      dic[score(slide1, localSlides[0])] = idx
      localSlides.pop(0)
      idx += 1
  return dic

# Make combinations
def getInterestingSequence(slidesArr):
  # dic = {}
  slide_already_selected = []
  slides =[]
  i = 0
  minSlidelist = {**slidesArr}
  bestNextSlide = slidesArr[0]
  slides.append(bestNextSlide)
  slide_already_selected.append(0)
  del minSlidelist[0]
  print("Total " + str(slidesArr.__len__()) + " slides")
  for idx in minSlidelist.items():
      print("Comparing " + str(idx) + " with " + str(minSlidelist.__len__()) + " slides")
      i += 1
      if idx in slide_already_selected:
          continue
      if len(minSlidelist)==0:
          continue
      listScores = findbest(bestNextSlide, minSlidelist, slide_already_selected);
      # print(listScores)
      bestPicId = max(listScores.values())
      bestNextSlide = minSlidelist[bestPicId]
      # print(bestPicId)
      # if(listScores.__len__() == 2):
      #     keysList = list(listScores)
      #     if(listScores[keysList[0]] == listScores[keysList[1]]):
      #         bestPicId = keysList[1]
      slide_already_selected.append(bestPicId)
      if idx == bestPicId:
          slides.append(minSlidelist[idx])
      else:
          # slides.append(slide)
          slides.append(bestNextSlide)
      try:
          # del minSlidelist[idx]
          del minSlidelist[bestPicId]
      except KeyError:
           print("Key " + str(bestPicId) + " not found")
      # dic[idx] = bestPicId
      # slide = Slide(str(idx) + " " + str(bestPicId), slide.getOrientation(), list([slidesArr[idx], slidesArr[bestPicId]]))
      p = 100 * (int(i) / slidesArr.__len__())
      print("Done " + str(idx) + " Percent: " + str(format(p,'.2f')) + "%")
  # print(dic)
  if minSlidelist.__len__() == 1:
      l = list(minSlidelist)
      slides.append(minSlidelist[l[0]])
  return slides

def getInterestingSequenceWithList(slidesArr):
  # dic = {}
  slide_already_selected = []
  slides =[]
  i = 0
  minSlidelist = slidesArr.copy()
  bestPicId = 0
  bestNextSlide = slidesArr[0]
  slides.append(bestNextSlide)
  # slide_already_selected.append(0)
  minSlidelist.pop(0)
  print("Total " + str(slidesArr.__len__()) + " slides")
  while minSlidelist:
      print("Comparing " + str(bestPicId) + " with " + str(minSlidelist.__len__()) + " slides")
      # print(minSlidelist[0])
      listScores = findbestWithList(bestNextSlide, minSlidelist, slides);
      bestPicId = max(listScores.values())
      bestNextSlide = minSlidelist[bestPicId]
      slides.append(bestNextSlide)

      minSlidelist.pop(bestPicId)
      p = 100 * (int(i) / slidesArr.__len__())
      print("Done " + str(bestPicId) + " Percent: " + str(format(p, '.2f')) + "%")
  del slides[-1]
  # for idx in minSlidelist:
  #     print("Comparing " + str(idx) + " with " + str(minSlidelist.__len__()) + " slides")
  #     i += 1
  #     if idx in slide_already_selected:
  #         continue
  #     if len(minSlidelist)==0:
  #         continue
  #     listScores = findbestWithList(bestNextSlide, minSlidelist, slide_already_selected);
  #     # print(listScores)
  #     bestPicId = max(listScores.values())
  #     bestNextSlide = minSlidelist[bestPicId]
  #     # print(bestPicId)
  #     # if(listScores.__len__() == 2):
  #     #     keysList = list(listScores)
  #     #     if(listScores[keysList[0]] == listScores[keysList[1]]):
  #     #         bestPicId = keysList[1]
  #     slide_already_selected.append(bestPicId)
  #     if idx == bestPicId:
  #         slides.append(minSlidelist[idx])
  #     else:
  #         # slides.append(slide)
  #         slides.append(bestNextSlide)
  #     try:
  #         # del minSlidelist[idx]
  #         minSlidelist.pop(bestPicId)
  #     except KeyError:
  #          print("Key " + str(bestPicId) + " not found")
  #     # dic[idx] = bestPicId
  #     # slide = Slide(str(idx) + " " + str(bestPicId), slide.getOrientation(), list([slidesArr[idx], slidesArr[bestPicId]]))
  #     p = 100 * (int(i) / slidesArr.__len__())
  #     print("Done " + str(idx) + " Percent: " + str(format(p,'.2f')) + "%")
  # print(dic)
  # if minSlidelist.__len__() == 1:
  #     l = list(minSlidelist)
  #     slides.append(minSlidelist[l[0]])
  return slides
