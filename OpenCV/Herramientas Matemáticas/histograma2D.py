import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

def histograma2D(im):
    
    imHSV = cv.cvtColor(im,cv.COLOR_RGB2HSV)
    
    lista_imagenes = [imHSV]
    lista_canales = [0,2]   # De la imagen HSV utilizamos 2 maginutdes (H y S) para observar en histograma 2D
    mascara = None
    lista_tam = [180, 256]  # H tiene 180 valores y S tiene 256
    rango = [0,180, 0,256]  # Ambos rangos
    
    hist = cv.calcHist(lista_imagenes,lista_canales,mascara,lista_tam,rango)
    
    
    plt.figure()
    
    plt.subplot(2,2,1)
    plt.imshow(im)
    plt.title("Foto")
    
    plt.subplot(2,2,2)
    cv.rectangle(hist, (15, 0), (50, 25), (255, 255, 0), 1)
    cv.rectangle(hist, (70, 100), (180, 110), (255, 255, 0), 1)
    plt.imshow(hist)
    plt.title("Histograma 2D")
    
    limite_bajo = np.array([0, 0, 15])
    limite_arriba = np.array([25, 255, 50])
    imagen_binaria = cv.inRange(imHSV,limite_bajo,limite_arriba)   # devuelve o 0 o 255.
    
    plt.subplot(2,2,3)
    plt.imshow(imagen_binaria, cmap='gray')
    plt.title("Primer Recuadro")
    
    limite_bajo = np.array([100, 0, 70])
    limite_arriba = np.array([110, 255, 180])
    imagen_binaria = cv.inRange(imHSV,limite_bajo,limite_arriba)   # devuelve o 0 o 255.
    
    plt.subplot(2,2,4)
    plt.imshow(imagen_binaria, cmap='gray')
    plt.title("Segundo Recuadro")
    
    plt.show()

if __name__ == '__main__':
    im = cv.imread("entorno.png")
    
    im = cv.cvtColor(im,cv.COLOR_BGR2RGB)
    histograma2D(im)
    