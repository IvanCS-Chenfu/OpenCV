import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

def etiquetas(im):
    
    im_gray = cv.cvtColor(im,cv.COLOR_BGR2GRAY)
    _, im_bin = cv.threshold(im_gray, 150, 255, cv.THRESH_BINARY_INV)
        
    im_dist = cv.distanceTransform(im_bin,cv.DIST_L2,5)
    
    _, im_centro_monedas = cv.threshold(im_dist, 20, 255, cv.THRESH_BINARY)
    
    im_centro_monedas = np.uint8(im_centro_monedas)
    _, etiquetas = cv.connectedComponents(im_centro_monedas)
    
    etiquetas_monedas = np.int32(etiquetas.copy())
    etiquetas_monedas = cv.watershed(im, etiquetas_monedas)
    
    plt.figure()
    
    plt.subplot(2,4,1)
    plt.imshow(im, cmap='gray')
    plt.title("Foto")
    
    plt.subplot(2,4,2)
    plt.imshow(im_bin, cmap='gray')
    plt.title("Binarizada")
    
    plt.subplot(2,4,3)
    plt.imshow(im_dist, cmap='gray')
    plt.title("Distancia a pixel 0")

    plt.subplot(2,4,4)
    plt.imshow(im_centro_monedas, cmap='gray')
    plt.title("Centro Monedas")
    
    plt.subplot(2,4,5)
    plt.imshow(etiquetas)
    plt.title("Etiquetas")
    
    plt.subplot(2,4,6)
    plt.imshow(etiquetas_monedas)
    plt.title("Monedas Etiquetadas")
    
    plt.subplot(2,4,7)
    im[etiquetas_monedas==-1] = [255, 0, 0]
    plt.imshow(im)
    plt.title("Monedas Imagen")
        
    plt.show()
    
    
    




    
    
if __name__ == '__main__':
    im = cv.imread("monedas.png")
    
    etiquetas(im)