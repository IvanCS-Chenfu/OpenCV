import cv2 as cv
import os
import matplotlib.pyplot as plt
import numpy as np

def colores_puros():
    tam = (100,100)
    
    zeros = np.zeros(tam)
    ones = np.ones(tam)
    
    b = cv.merge((zeros,zeros,255*ones))
    g = cv.merge((zeros,255*ones,zeros))
    r = cv.merge((255*ones,zeros,zeros))
    
    bg = cv.merge((zeros,255*ones,255*ones))
    gr = cv.merge((255*ones,255*ones,zeros))
    br = cv.merge((255*ones,zeros,255*ones))
    
    negro = cv.merge((zeros,zeros,zeros))
    blanco = cv.merge((255*ones,255*ones,255*ones))
    
    plt.figure()
    plt.subplot(331)
    plt.imshow(b)
    plt.title("b")
    plt.subplot(332)
    plt.imshow(g)
    plt.title("g")
    plt.subplot(333)
    plt.imshow(r)
    plt.title("r")
    plt.subplot(334)
    plt.imshow(bg)
    plt.title("bg")
    plt.subplot(335)
    plt.imshow(gr)
    plt.title("gr")
    plt.subplot(336)
    plt.imshow(br)
    plt.title("br")
    plt.subplot(337)
    plt.imshow(negro)
    plt.title("negro")
    plt.subplot(338)
    plt.imshow(blanco)
    plt.title("blanco")
    
    plt.show()
    
    
def separar_RGB():
    root = os.getcwd()
    imPath = os.path.join(root, 'RGB.png')
    im = cv.imread(imPath) 
    im_RGB = cv.cvtColor(im,cv.COLOR_BGR2RGB)
    
    r,g,b = cv.split(im_RGB)
    
    plt.figure()
    plt.subplot(221)
    plt.imshow(im_RGB, cmap = 'gray')
    plt.title("bgr")
    plt.subplot(222)
    plt.imshow(r, cmap = 'gray')
    plt.title("r")
    plt.subplot(223)
    plt.imshow(g, cmap = 'gray')
    plt.title("g")
    plt.subplot(224)
    plt.imshow(b, cmap = 'gray')
    plt.title("b")
    
    
    plt.show()
    
def pasar2gris():
    root = os.getcwd()
    imPath = os.path.join(root, 'RGB.png')
    im = cv.imread(imPath) 
    im_gray = cv.cvtColor(im,cv.COLOR_BGR2GRAY)
    
    cv.imshow('Imagen Gris', im_gray)
    cv.waitKey(0) 
    
if __name__ == '__main__':
    colores_puros()
    
    separar_RGB()
    
    pasar2gris()