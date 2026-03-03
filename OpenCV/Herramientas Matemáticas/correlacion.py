import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np


def correlacion(im, color):

    # Todos los Métodos para Realizar la Correlación
    TiposCorrelacion = [
        cv.TM_CCOEFF,       
        cv.TM_CCOEFF_NORMED,
        cv.TM_CCORR,
        cv.TM_CCORR_NORMED,
        cv.TM_SQDIFF,
        cv.TM_SQDIFF_NORMED
    ]

    NombresCorrelacion = [
        "C. Media Eliminada",
        "C. Media Eliminada Normalizada",
        "C. Cruzada",
        "C. Cruzada Normalizada",
        "C. Diferencia Cuadrática",
        "C. Diferencia Cuadrática Normalizada"
    ]

    region = np.zeros((200, 200))
    
    if (color == "Rojo"):
        region = im[25:225, 35:235]
        
    elif (color == "Amarillo"):
        region = im[25:225, 230:430]
        
    elif (color == "Verde"):
        region = im[25:225, 430:630]
        
    elif (color == "Morado"):
        region = im[250:450, 40:240]
        
    elif (color == "Rosa"):
        region = im[240:440, 240:440]

    elif (color == "Naranja"):
        region = im[210:450, 430:630]
    
    fig1 = plt.figure()
    sub1 = fig1.add_subplot(2,4,1)
    sub1.imshow(im)
    sub1 = fig1.add_subplot(2,4,2)
    sub1.imshow(region)
    sub1.set_title("Region")
    
    fig2 = plt.figure()
    sub2 = fig2.add_subplot(2,4,1)
    sub2.imshow(im)
    sub2 = fig2.add_subplot(2,4,2)
    sub2.imshow(region)
    sub2.set_title("Region")
    
    for i in range(len(TiposCorrelacion)):
        
        im_actual = im.copy()
        
        im_corr = cv.matchTemplate(im_actual,region,TiposCorrelacion[i])
        
        _,_,minLoc,maxLoc = cv.minMaxLoc(im_corr)
        
        if TiposCorrelacion[i] == cv.TM_SQDIFF or TiposCorrelacion[i] == cv.TM_SQDIFF_NORMED:
            topLeft = minLoc
        else:
            topLeft = maxLoc
            
        bottomRight = (topLeft[0]+region.shape[1],topLeft[1]+region.shape[0])
        cv.rectangle(im_actual,topLeft,bottomRight,(255,0,0),10)
        
        sub1 = fig1.add_subplot(2,4,i+3)
        sub1.imshow(im_corr)
        sub1.set_title(NombresCorrelacion[i])
        
        sub2 = fig2.add_subplot(2,4,i+3)
        sub2.imshow(im_actual)
        sub2.set_title(NombresCorrelacion[i])
        
        
    plt.show()
    

if __name__ == '__main__':
    im = cv.imread("Figuras.png")
    im = cv.cvtColor(im,cv.COLOR_BGR2RGB)

    correlacion(im, "Verde")
    
    
    