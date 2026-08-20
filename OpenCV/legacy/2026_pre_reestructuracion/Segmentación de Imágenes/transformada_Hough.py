import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

def rectas(im):
    
    _, im = cv.threshold(im, 100, 255, cv.THRESH_BINARY)
    bordes = cv.Canny(im, 0, 255)
    
    dist_resolucion = 1
    angulo_resolucion = np.pi/180
    umbral = 50
    
    lineas = cv.HoughLines(bordes,dist_resolucion, angulo_resolucion, umbral)
    
    k = 3000
    
    im_lineas = np.zeros(im.shape)
    im_lineas = cv.merge((im_lineas,im_lineas,im_lineas))
    
    for linea in lineas:
        rho, theta = linea[0]
        
        dhat = np.array([[np.cos(theta)],[np.sin(theta)]])
        d = rho*dhat
        
        lhat = np.array([[-np.sin(theta)],[np.cos(theta)]])
        p1 = d + k*lhat
        p1 = p1.astype(int)
        p2 = d - k*lhat
        p2 = p2.astype(int)
        
        cv.line(im_lineas, (p1[0][0],p1[1][0]), (p2[0][0],p2[1][0]), (255,255,0), 10)
        
    plt.figure()
    
    plt.subplot(1,3,1)
    plt.imshow(im, cmap='gray')
    plt.title("Foto")
    
    plt.subplot(1,3,2)
    plt.imshow(bordes, cmap='gray')
    plt.title("Canny")
    
    plt.subplot(1,3,3)
    plt.imshow(im_lineas)
    plt.title("Lineas")

        
    plt.show()
    
    
    
def circulos(im):
    
    circulos = cv.HoughCircles(im,cv.HOUGH_GRADIENT, dp=1, minDist=600, param1=200, param2=15, minRadius=50, maxRadius=150)
    
    im_circulos = np.zeros(im.shape)
    im_circulos = cv.merge((im_circulos,im_circulos,im_circulos))
    
    for circulo in circulos[0,:]:
        
        centro = (int(circulo[0]), int(circulo[1]))
        radio = int(circulo[2])
        cv.circle(im_circulos, centro, radio, (255,255,0), 10)
        
    plt.figure()
    
    plt.subplot(1,2,1)
    plt.imshow(im, cmap='gray')
    plt.title("Foto")
    
    plt.subplot(1,2,2)
    plt.imshow(im_circulos)
    plt.title("Circulos")

        
    plt.show()



    
    
if __name__ == '__main__':
    im = cv.imread("Figuras.png")
    im = cv.cvtColor(im,cv.COLOR_BGR2GRAY)
    
    rectas(im)
    
    circulos(im)