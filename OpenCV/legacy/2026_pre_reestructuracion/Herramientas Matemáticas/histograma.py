import cv2 as cv
import matplotlib.pyplot as plt


def histograma_gris(im):
    
    lista_imagenes = [im]   # Solo una imagen pero se pueden más
    lista_canales = [0]     # La imagen gris solo tiene un canal
    mascara = None
    lista_tam = [256]       # Número de valores del histograma
    rango = [0,256]         # No incluye el ultimo: (0-255)
    
    hist = cv.calcHist(lista_imagenes,lista_canales,mascara,lista_tam,rango)
    
    
    plt.figure()
    
    plt.subplot(1,2,1)
    plt.imshow(im, cmap='gray')
    plt.title("Foto")
    
    plt.subplot(1,2,2)
    plt.plot(hist)
    plt.title("Histograma Gris")
    plt.show()
    
def histograma_rgb(im):
    lista_imagenes = [im]   # Solo una imagen pero se pueden más
    mascara = None
    lista_tam = [256]       # Número de valores del histograma
    rango = [0,256]         # No incluye el ultimo: (0-255)
    
    
    
    
    plt.figure()
    
    plt.subplot(2,2,1)
    plt.imshow(im)
    plt.title("Foto")
    
    colors = ['r', 'g', 'b']
    
    for i in range(len(colors)):
        
        lista_canales = [i]     # Cada uno de los canales
        hist = cv.calcHist(lista_imagenes,lista_canales,mascara,lista_tam,rango)
        
        plt.subplot(2,2,i+2)
        plt.plot(hist, colors[i])
        plt.title(colors[i])
        
    plt.show()

if __name__ == '__main__':
    im = cv.imread("Gato.png")
    
    im = cv.cvtColor(im,cv.COLOR_BGR2RGB)
    histograma_rgb(im)
    
    im = cv.cvtColor(im,cv.COLOR_RGB2GRAY)
    histograma_gris(im)
    
    
    