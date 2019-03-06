from util import *

def getBestSlide(lastSlide, remainingSlides):
    dic = {}
    localSlides = (remainingSlides[ :Parameters.samplePortion])
    for slide in localSlides:
        dic[scoreSlides(lastSlide, slide)] = slide
    selectedId = max(dic.keys())
    return dic[selectedId]

def getBestSlideWithChildScoring(lastSlide, remainingSlides):
    dic = {}
    localSlides = (remainingSlides[ :Parameters.samplePortion])
    for slide in localSlides:
        bestChild = slide
        childLocalSlides = (localSlides[ :10]).copy()
        bestChild = getBestSlide(slide, childLocalSlides)
        finalScore = scoreSlides(lastSlide, slide) + scoreSlides(slide, bestChild)
        dic[finalScore] = [slide, bestChild]
    selectedId = max(dic.keys())
    return dic[selectedId]

def getBestSlideWithChild(lastSlide, remainingSlides):
    bestSlide = getBestSlide(lastSlide, remainingSlides)
    localSlides = (remainingSlides[ :Parameters.ChildSamplePortion])
    bestChild = getBestSlide(bestSlide, localSlides)

    # scoreOfNextSlide = scoreSlides(lastSlide, bestSlide)
    # scoreOfChildSlide = scoreSlides(bestChild, bestSlide)

    return bestSlide, bestChild

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
