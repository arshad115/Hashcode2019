import random
from itertools import islice

# For C:
# samplePortion = 1000
# VerticalSamplePortion = 3

class Parameters:
    samplePortion = 1000
    VerticalSamplePortion = 3

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

def scoreSlides(slide1, slide2):
  AMinusB = slide1.getTags().difference(slide2.getTags()).__len__()
  AnB = slide1.getTags().intersection(slide2.getTags()).__len__()
  APlusB = slide2.getTags().difference(slide1.getTags()).__len__()
  if slide1.getPhotoIds() == slide2.getPhotoIds():
      return 0;
  min = smallest(AMinusB, AnB, APlusB)
  return min

def scorePhotos(photo1, photo2):
  AMinusB = photo1.getTags().difference(photo2.getTags()).__len__()
  AnB = photo1.getTags().intersection(photo2.getTags()).__len__()
  APlusB = photo2.getTags().difference(photo1.getTags()).__len__()
  if photo1.getId() == photo2.getId():
      return 0;
  min = smallest(AMinusB, AnB, APlusB)
  return min

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

def chunks(data, SIZE=10000):
    it = iter(data)
    for i in range(0, len(data), SIZE):
        yield {k:data[k] for k in islice(it, SIZE)}

def split_dict_equally(input_dict, chunks=3):
    "Splits dict by keys. Returns a list of dictionaries."
    # prep with empty dicts
    return_list = [dict() for idx in range(chunks)]
    idx = 0
    for k,v in input_dict.items():
        return_list[idx][k] = v
        if idx < chunks-1:  # indexes start at 0
            idx += 1
        else:
            idx = 0
    return return_list

def split_list_equally(input_dict, chunks=3):
    return_list = [dict() for idx in range(chunks)]
    idx = 0
    for k,v in enumerate(input_dict):
        return_list[idx][k] = v
        if idx < chunks-1:  # indexes start at 0
            idx += 1
        else:
            idx = 0
    return return_list