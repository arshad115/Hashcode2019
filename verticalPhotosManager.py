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

def score(photo1, photo2):
  # max = list(set(photo1.getTags()) - set(photo2.getTags())) + list(set(photo2.getTags()) - set(photo1.getTags()))
  # print((photo1.getTags()) + (photo2.getTags()))
  max = photo1.getTags().intersection(photo2.getTags())
  # max = (f5(photo1.getTags() + photo2.getTags()))
  # max = list(set(photo1.getTags()) - set(photo2.getTags())) + list(set(photo2.getTags()) - set(photo1.getTags()))
  AMinusB = photo1.getTags().difference(photo2.getTags()).__len__()
  AnB = photo1.getTags().intersection(photo2.getTags()).__len__()
  APlusB = photo2.getTags().difference(photo1.getTags()).__len__()
  if photo1.getId() == photo2.getId():
      return 0;
  max = biggest(AMinusB, AnB, APlusB)
  return max
  # print(max)
  # return max

def findbest(photo1, photoArr, pic_already_selected):
  # ids = []
  dic = {}
  for idx, photo in photoArr.items():
      if photo.getId() in pic_already_selected:
          continue
      # ids.append(idx)
      # dic[idx] = score(photo1, photo)
      dic[score(photo1, photo)] = idx
  return dic

# Make combinations
def getVPairs(photoArr):
  # dic = {}
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
      # print(listScores)
      bestPicId = max(listScores, key=listScores.get)
      bestPicId = listScores[bestPicId]
      if bestPicId == idx:
          print('wtf')
          continue
      # print(bestPicId)
      # if(listScores.__len__() == 2):
      #     keysList = list(listScores)
      #     if(listScores[keysList[0]] == listScores[keysList[1]]):
      #         bestPicId = keysList[1]
      pic_already_selected.append(photo.getId())
      pic_already_selected.append(bestPicId)
      # pic_already_selected.sort()
      try:
          del minPhotolist[photo.getId()]
          del minPhotolist[bestPicId]
      except KeyError:
           print("Key " + str(bestPicId) + " not found")
      # dic[idx] = bestPicId
      slide = Slide(str(idx) + " " + str(bestPicId), 'V', list([photoArr[idx], photoArr[bestPicId]]))
      slides.append(slide)
      p = 100 * (int(i) / photoArr.__len__())
      print("Done " + str(idx) + " Percent: " + str(format(p,'.2f')) + "%")
  # print(dic)
  return slides
