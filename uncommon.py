
str = []
str.append(["aa", "bb", "cc", "dd"])
str.append(["aa", "bb", "ee", "dd"])
str.append(["aa", "bb", "ee", "dd"])
str.append(["ff", "gg", "ee", "dd"])

def score(photo1, photo2):
  max = list(set(photo1) - set(photo2)) + list(set(photo2) - set(photo1))
  return max.__len__()


def findbest(photo1, photoArr, pic_already_selected):
  ids = []
  dic = {}
  for idx, photo in enumerate(photoArr):
      if idx in pic_already_selected:
          continue
      ids.append(idx)
      dic[idx] = score(photo1, photo)
  return dic

# Make combinations
def getVPairs(photoArr):
  dic = {}
  pic_already_selected = []

  for idx, photo in enumerate(photoArr):
      if idx in pic_already_selected:
          continue
      listScores = findbest(photo, photoArr, pic_already_selected);
      bestPicId = max(listScores, key=listScores.get)
      if(listScores.__len__() == 2):
          keysList = list(listScores)
          if(listScores[keysList[0]] == listScores[keysList[1]]):
              bestPicId = keysList[1]
      pic_already_selected.append(idx)
      pic_already_selected.append(bestPicId)
      dic[idx] = bestPicId
  return dic

# Make combinations

print(getVPairs(str))

