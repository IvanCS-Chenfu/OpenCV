import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np


def hist_back_projection(im, color):
    
    # Obtengo imagen, Obtengo región, Paso región a HSV (y saco H), Calculo histograma de H de la región,
    # Muestro H de imagen global, muestro back project (con el fin de comprobar si las zonas claras son las que tienen
    # valores altos del histograma). 6 imágenes.
    
    region = np.zeros((50, 50))
    
    # 135, 125 ! 330, 125 ! 530, 125 ! 135, 350 ! 330, 350 ! 530, 350 (radio 25)
    if (color == "Rojo"):
        region = im[100:150, 110:160]      # y: 125-25 .. 125+25, x: 135-25 .. 135+25
        
    elif (color == "Amarillo"):
        region = im[100:150, 305:355]      # centro (330,125)
        
    elif (color == "Verde"):
        region = im[100:150, 505:555]      # centro (530,125)
        
    elif (color == "Morado"):
        region = im[325:375, 110:160]      # centro (135,350)
        
    elif (color == "Rosa"):
        region = im[325:375, 305:355]      # centro (330,350)

    elif (color == "Naranja"):
        region = im[325:375, 505:555]      # centro (530,350)
    
    region_HSV = cv.cvtColor(region,cv.COLOR_RGB2HSV)
    hist_region = cv.calcHist([region_HSV],[0],None,[180],[0,180])
    
    im_HSV = cv.cvtColor(im,cv.COLOR_RGB2HSV)
    im_h,_,_ = cv.split(im_HSV)
    
    cv.normalize(hist_region, hist_region, 0, 255, cv.NORM_MINMAX)      # Es necesario Normalizar el histograma entre 0 y 255
    backproj = cv.calcBackProject([im_HSV], [0], hist_region, [0,180], 1)   # Se puede realizar con histogramas 2D
    
    plt.figure()
    
    plt.subplot(2,3,1)
    plt.imshow(im) 
    plt.title("Foto")
    
    plt.subplot(2,3,2)
    plt.imshow(region)
    plt.title("Region")
    
    
    plt.subplot(2,3,3)
    plt.plot(hist_region)
    plt.title("Histograma Region (HUE)")
    
    plt.subplot(2,3,4)
    plt.imshow(im_h, cmap='gray')
    plt.title("Hue de la Imagen")
    
    plt.subplot(2,3,5)
    plt.imshow(backproj, cmap='gray')
    plt.title("Back Projection")
    
    plt.show()
    

if __name__ == '__main__':
    im = cv.imread("Figuras.png")
    im = cv.cvtColor(im,cv.COLOR_BGR2RGB)

    hist_back_projection(im, "Naranja")
    
    
    