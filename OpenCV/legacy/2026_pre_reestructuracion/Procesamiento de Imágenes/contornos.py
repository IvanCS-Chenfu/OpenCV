import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np


def contornos(im):
    
    _,_,im_v = cv.split(im)
    
    umbral_min = 0
    umbral_max = 255
    cannyEdge = cv.Canny(im_v, umbral_min, umbral_max)
    
    umbral_bin = 100
    _, im_bin = cv.threshold(im_v, umbral_bin, 255, cv.THRESH_BINARY)
    contornos, _ = cv.findContours(im_bin,cv.RETR_TREE,cv.CHAIN_APPROX_SIMPLE)
    #contornos = [contornos[0]]
    im_contornos = np.zeros(im_v.shape)
    cv.drawContours(im_contornos, contornos, -1, (255,255,255), 2)
    
    
    
    plt.figure()
    
    plt.subplot(2,2,1)
    plt.imshow(im_v, cmap='gray')
    plt.title("Foto (Value)")
    
    plt.subplot(2,2,2)
    plt.imshow(cannyEdge, cmap='gray')
    plt.title("Canny")
    
    plt.subplot(2,2,3)
    plt.imshow(im_contornos, cmap='gray')
    plt.title("Contorno")
    
    plt.show()
    

if __name__ == '__main__':
    im = cv.imread("Figuras.png")
    im = cv.cvtColor(im,cv.COLOR_BGR2HSV)
    
    contornos(im)
    
    
    