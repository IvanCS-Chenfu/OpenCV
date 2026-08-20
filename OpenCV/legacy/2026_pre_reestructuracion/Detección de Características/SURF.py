# pip install opencv-contrib-python==3.4.2.16
# python 3.6.8

import cv2 as cv
import matplotlib.pyplot as plt


def SURF(im):
    
    umbral_hessiano = 3000
    objeto_surf = cv.xfeatures2d.SURF_create(umbral_hessiano)
    
    keypoints = objeto_surf.detect(im,None)
    
    im_keypoints = im.copy()
    
    im_keypoints = cv.drawKeypoints(im_keypoints,keypoints,im_keypoints,flags=cv.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
    
    
    
    plt.figure()
    
    plt.subplot(1,2,1)
    plt.imshow(im, cmap='gray')
    plt.title("Foto")
    
    plt.subplot(1,2,2)
    plt.imshow(im_keypoints, cmap='gray')
    plt.title("Keypoints")
    
    plt.show()
    




if __name__ == '__main__':
    im = cv.imread("Gente.png")
    im = cv.cvtColor(im,cv.COLOR_BGR2GRAY)
    
    SURF(im)

    
    
    