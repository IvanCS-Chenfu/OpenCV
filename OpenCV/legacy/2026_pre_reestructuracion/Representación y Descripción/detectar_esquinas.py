import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np


def esquinas_harris(im):
    
    _, im = cv.threshold(im, 100, 255, cv.THRESH_BINARY)
    im = np.float32(im)
    
    block_Size = 9
    sobel_Size = 5
    k = 0.04
    harris = cv.cornerHarris(im,block_Size,sobel_Size,k)
    
    im_esquinas = np.zeros(im.shape)
    im_esquinas[harris>0.05*harris.max()] = 255
     
    plt.figure()
    
    plt.subplot(1,3,1)
    plt.imshow(im, cmap='gray')
    plt.title("Foto")
    
    plt.subplot(1,3,2)
    plt.imshow(harris, cmap='gray')
    plt.title("Harris")
    
    plt.subplot(1,3,3)
    plt.imshow(im_esquinas, cmap='gray')
    plt.title("Esquinas")
    
    plt.show()
    

def esquinas_bien(im):
    
    _, im = cv.threshold(im, 100, 255, cv.THRESH_BINARY)
    
    esquinas_maximas = 200
    calidad = 0.25
    distancia_minima = 20
    
    esquinas = cv.goodFeaturesToTrack(im,esquinas_maximas,calidad,distancia_minima)
    im_esquinas = cv.merge((im,im,im))
    
    for esquina in esquinas:
        x = int(esquina[0][0])
        y = int(esquina[0][1])
        
        cv.circle(im_esquinas,(x,y),10,(255,255,0),-1)
     
    plt.figure()
    
    plt.subplot(1,2,1)
    plt.imshow(im, cmap='gray')
    plt.title("Foto")
    
    plt.subplot(1,2,2)
    plt.imshow(im_esquinas, cmap='gray')
    plt.title("Esquinas")
    
    plt.show()
    




if __name__ == '__main__':
    im = cv.imread("Figuras.png")
    im = cv.cvtColor(im,cv.COLOR_BGR2GRAY)
    
    esquinas_harris(im)
    
    esquinas_bien(im)

    
    
    