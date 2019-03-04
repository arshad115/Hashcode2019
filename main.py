import random
import time

import SlidesManager
from photo import Photo
from slide import Slide
import verticalPhotosManager
from slideshow import SlideShow
from itertools import islice
import multiprocessing.pool

start_time = time.time()
print("Start time: " + str(start_time))

fileAB = "ab_example";
fileA = "a_example";
fileB = "b_lovely_landscapes";
fileC = "c_memorable_moments";
fileD = "d_pet_pictures";
fileE = "e_shiny_selfies";

file = fileC;
f = open("inputs/" + file + ".txt", "r")

N = int(f.readline())

# Photos dictionary
photos = {}
horizontalPhotos = {}
verticalPhotos = {}

slides = []

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
    "Splits dict by keys. Returns a list of dictionaries."
    # prep with empty dicts
    return_list = [dict() for idx in range(chunks)]
    idx = 0
    for k,v in enumerate(input_dict):
        return_list[idx][k] = v
        if idx < chunks-1:  # indexes start at 0
            idx += 1
        else:
            idx = 0
    return return_list

for i in range(0,N):
  line = f.readline().strip()
  splits = line.split(' ')

  orientation = splits[0]
  nTags = splits[1]
  tags= set(splits[2:splits.__len__()])

  if(orientation == 'H'):
      horizontalPhotos[i] = Photo(i, orientation, nTags, tags)
      slide = Slide(str(i), orientation, list([horizontalPhotos[i]]))
      slides.append(slide)
  else:
      verticalPhotos[i] = Photo(i, orientation, nTags, tags)

  # photo = Photo(orientation, nTags, tags)
  # photos[i] = photo
  #End of for loop
# print(verticalPhotos)

# Now make slides of vertical photos
# Best case vertical photo pairs

print("Finished Reading, read " + str(N) + " photos")
print("Now making slides for Vertical " + str(verticalPhotos.__len__()) + " photos")

# print(sorted(verticalPhotos))

chunksNProcesses = 15

print("Vertical photos optimized, now adding them to slides")

verticalSlides = verticalPhotosManager.getVPairs(verticalPhotos)
# add vertical slides to horizontal slides
slides.extend(verticalSlides)

# verticalPhotosChunks = split_dict_equally(verticalPhotos, chunksNProcesses)
#
# for item in verticalPhotosChunks:
#     print(item)
#
# # six threads
# # a thread pool that implements the process pool API.
# pool = multiprocessing.pool.ThreadPool(processes=chunksNProcesses)
# return_list = pool.map(verticalPhotosManager.getVPairs, verticalPhotosChunks, chunksize=1)
# pool.close()
#
# # print(return_list)
# for data in return_list:
#     print(data)
#     slides.extend(data)



# items=slides.copy() # List of tuples
# random.shuffle(items)

# slidesDic = {k: v for k, v in enumerate(slides)}
#
# optimizedSlides = SlidesManager.getInterestingSequence(slidesDic)

random.shuffle(slides)

# slides.sort()


optimizedSlides = SlidesManager.getInterestingSequenceWithList(slides)

# optimizedSlidesChunks = split_list_equally(slides, chunksNProcesses)
#
# optimizedSlides = []
#
# # six threads
# # a thread pool that implements the process pool API.
# pool = multiprocessing.pool.ThreadPool(processes=chunksNProcesses)
# return_list = pool.map(SlidesManager.getInterestingSequenceWithList, optimizedSlidesChunks, chunksize=1)
# pool.close()
#
# # print(return_list)
# for data in return_list:
#     print(data)
#     optimizedSlides.extend(data)


# slide = Slide('V', list([verticalPhotos[1], verticalPhotos[2]]))
# print(slides)
slideshow = SlideShow(optimizedSlides)
slideshow.saveOutput(file)

elapsed_time = time.time() - start_time

print("Total execution time: " + str(elapsed_time))