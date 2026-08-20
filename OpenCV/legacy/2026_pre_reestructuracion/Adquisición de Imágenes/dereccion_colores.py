import cv2 as cv
import os
import matplotlib.pyplot as plt
import numpy as np

def detectar(color):
    root = os.getcwd()
    imPath = os.path.join(root, 'Figuras.png')
    im = cv.imread(imPath) 
    im_HSV = cv.cvtColor(im,cv.COLOR_BGR2HSV)
    
    H, S, V = cv.split(im_HSV)
    imagen_binaria = np.zeros(H.shape, dtype=bool)
    
    plt.figure()
    plt.imshow(im_HSV)
    plt.show()
    
    if (color == "Rojo"):
        imagen_binaria = ((H < 5) & (V > 50)) | (H > 175) 
        
    elif (color == "Amarillo"):
        imagen_binaria = (H > 20) & (H < 30)
        
    elif (color == "Verde"):
        limite_bajo = np.array([45, 0, 0])
        limite_arriba = np.array([55, 255, 255])
        imagen_binaria = cv.inRange(im_HSV,limite_bajo,limite_arriba).astype(bool)  # sin ".astype(bool)" devuelve o 0 o 255.
        
    elif (color == "Morado"):
        imagen_binaria = (H > 125) & (H < 135)
        
    elif (color == "Rosa"):
        limite_bajo = np.array([160, 0, 0])
        limite_arriba = np.array([170, 255, 255])
        imagen_binaria = cv.inRange(im_HSV,limite_bajo,limite_arriba).astype(bool)
    
    elif (color == "Naranja"):
        imagen_binaria = (H > 10) & (H < 15)
        
    imagen_binaria = imagen_binaria.astype(np.uint8)*255
    cv.imshow('Figura',imagen_binaria)
    cv.waitKey(0) 
    
    
if __name__ == '__main__':
    detectar("Rosa")