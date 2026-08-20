# pip install opencv-contrib-python==3.4.2.16
# python 3.6.8

import cv2 as cv


def BRIEF(im):
    
    objeto_fast = cv.FastFeatureDetector_create()
    
    dif_min_intensidad = 100
    objeto_fast.setThreshold(dif_min_intensidad)
    
    objeto_brief = cv.xfeatures2d.BriefDescriptorExtractor_create()
    
    keypoints = objeto_fast.detect(im,None)
    keypoints, descriptors = objeto_brief.compute(im,keypoints)
    
    print(objeto_brief.descriptorSize())
    print(descriptors[0])
    print(' '.join([format(val,'08b') for val in descriptors[0]]))
    




if __name__ == '__main__':
    im = cv.imread("Gente.png")
    im = cv.cvtColor(im,cv.COLOR_BGR2GRAY)
    
    BRIEF(im)

    
    
    