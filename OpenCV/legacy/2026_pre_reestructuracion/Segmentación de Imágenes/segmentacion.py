import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

def segmentacion(im):
    
    im_gray = cv.cvtColor(im,cv.COLOR_BGR2GRAY)
    
    mask = np.zeros(im_gray.shape,np.uint8)
    bgdModel = np.zeros((1,65),np.float64)
    fgdModel = np.zeros((1,65),np.float64)
    x0 = 130
    y0 = 40
    x1 = 670
    y1 = 850
    region = (x0, y0, x1-x0, y1-y0)
    iteraciones = 1
    
    cv.grabCut(im,mask,region,bgdModel,fgdModel,iteraciones,cv.GC_INIT_WITH_RECT)
    
    mascara_gato = np.where((mask == 2) | (mask == 0),0,1).astype('uint8')  # Convierte los valores de 2 y 0 a 0. Lo demás a 1.
    im_gato = im*mascara_gato[:,:,np.newaxis]
    
    plt.figure()
    
    plt.subplot(2,4,1)
    plt.imshow(im, cmap='gray')
    plt.title("Foto")
    
    plt.subplot(2,4,2)
    plt.imshow(mask, cmap='gray')
    plt.title("Mascara")

    plt.subplot(2,4,3)
    plt.imshow(im_gato)
    plt.title("Gato")
        
    plt.show()
    
    
    




    
    
if __name__ == '__main__':
    im = cv.imread("Gato.png")
    im = cv.cvtColor(im,cv.COLOR_BGR2RGB)
    
    segmentacion(im)