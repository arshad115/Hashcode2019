from util import *
from more_itertools import split_after

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
        listToSplit = localSlides.copy()
        childScore = 0
        if listToSplit.__len__() > 1:
            try:
                childLocalSlides = list(split_after(listToSplit, lambda x: x == slide))[1]
                # childLocalSlides = (childLocalSlides[:Parameters.ChildSamplePortion]).copy()
                childLocalSlides = random_subset(childLocalSlides, Parameters.ChildSamplePortion).copy()
                bestChild = getBestSlide(slide, childLocalSlides)
                childScore = scoreSlides(slide, bestChild)
            except:
                print('last slide has no child')
        finalScore = scoreSlides(lastSlide, slide) + childScore
        dic[finalScore] = [slide, bestChild]
    selectedId = max(dic.keys())
    return dic[selectedId]

def getBestSlideWithChild(lastSlide, remainingSlides):
    dic = {}
    bestSlide = getBestSlide(lastSlide, remainingSlides)
    bestChild = bestSlide
    localSlides = (remainingSlides[:Parameters.ChildSamplePortion]).copy()
    # localSlides = random_subset(remainingSlides, Parameters.ChildSamplePortion).copy()
    if (localSlides.__len__() > 1):
        scoreOfNextSlide = scoreSlides(lastSlide, bestSlide)
        for slide in localSlides:
            scoreOfChildSlide = scoreSlides(slide, bestSlide)
            dic[scoreOfNextSlide + scoreOfChildSlide] = slide
        selectedId = max(dic.keys())
        bestChild = dic[selectedId]
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
      lastSlide, bestChild  = getBestSlideWithChildScoring(lastSlide, remainingSlides);
      slides.append(lastSlide)
      remainingSlides.remove(lastSlide)
      if(remainingSlides.__len__()  > 1 and lastSlide!=bestChild):
          slides.append(bestChild)
          remainingSlides.remove(bestChild)
          lastSlide = bestChild
      p = 100 * int(i)/(slidesArr.__len__())
      i += 1
      print("Done " + str(i) + " Percent: " + str(format(p, '.2f')) + "%")
  return slides
