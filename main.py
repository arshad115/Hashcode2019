import random
import time

import SlidesManager
from photo import Photo
from slide import Slide
import verticalPhotosManager
from slideshow import SlideShow

start_time = time.time()
print("Start time: " + str(start_time))

fileAB = "ab_example";
fileA = "a_example";
fileB = "b_lovely_landscapes";
fileC = "c_memorable_moments";
fileD = "d_pet_pictures";
fileE = "e_shiny_selfies";

file = fileD;
f = open("inputs/" + file + ".txt", "r")

N = int(f.readline())

photos = {}
horizontalPhotos = {}
verticalPhotos = {}
slides = []

for i in range(0,N):
  line = f.readline().strip()
  splits = line.split(' ')

  orientation = splits[0]
  nTags = splits[1]
  tags= set(splits[2:splits.__len__()])

  if(orientation == 'H'):
      horizontalPhotos[i] = Photo(i, orientation, nTags, tags)
      slide = Slide(str(i), orientation, list([horizontalPhotos[i]]), nTags)
      slides.append(slide)
  else:
      verticalPhotos[i] = Photo(i, orientation, nTags, tags)
  #End of for loop

print("Finished Reading, read " + str(N) + " photos")
print("Now making slides for Vertical " + str(verticalPhotos.__len__()) + " photos")
print("Vertical photos optimized, now adding them to slides")

verticalSlides = verticalPhotosManager.getVPairs(verticalPhotos)
slides.extend(verticalSlides)

# random.shuffle(slides)

sortedSlides = sorted(slides, key=lambda slide: slide.tagsLen)

# slides.sort()

optimizedSlides = SlidesManager.getInterestingSequenceWithList(sortedSlides)

slideshow = SlideShow(optimizedSlides)
slideshow.saveOutput(file)

elapsed_time = time.time() - start_time

print("Total execution time: " + str(elapsed_time))