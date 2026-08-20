import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np


def descriptores(im,i):
    
    _,_,im_v = cv.split(im)
    
    _, im_bin = cv.threshold(im_v, 100, 255, cv.THRESH_BINARY)
    contornos, _ = cv.findContours(im_bin,cv.RETR_TREE,cv.CHAIN_APPROX_SIMPLE)
    contorno_i = [contornos[i]]  # Solo cojo un Contorno
    im_contorno = np.zeros(im_v.shape)
    cv.drawContours(im_contorno, contorno_i, -1, (255,255,255), 2)
    
    contorno = contorno_i[0]
    M = cv.moments(contorno)
    Cx = int(M['m10']/M['m00'])
    Cy = int(M['m01']/M['m00'])
    
    area = cv.contourArea(contorno)
    perimeter = cv.arcLength(contorno,True)
    print("Area:", area)
    print("Perímetro:",perimeter)
    
    epsilon = 0.01*perimeter
    poligono_approx = cv.approxPolyDP(contorno,epsilon,True)
    poligono_approx = np.array(poligono_approx)
    poligono_approx = np.concatenate((poligono_approx,poligono_approx[:1]),axis=0)
    
    cerco_convexo = cv.convexHull(contorno)
    cerco_convexo = cerco_convexo[:,0,:]
    cerco_convexo = np.concatenate((cerco_convexo,cerco_convexo[:1]),axis=0)
    
    x,y,w,h = cv.boundingRect(contorno)
    
    aspectRatio = w/h
    extent = area/(w*h)
    solidity = area/cv.contourArea(cerco_convexo)
    equiDIa = np.sqrt(4*area/np.pi)
    _,_,_angle = cv.fitEllipse(contorno)
    
    print("AspectRatio:", aspectRatio)
    print("Extent:", extent)
    print("Solidity:", solidity)
    print("EquiDIa:", equiDIa)
    print("Angle:", _angle)
    
    plt.figure()
    
    plt.subplot(2,3,1)
    plt.imshow(im_v, cmap='gray')
    plt.title("Foto (Value)")
    
    plt.subplot(2,3,2)
    plt.imshow(im_contorno, cmap='gray')
    plt.title("Contorno")
    
    plt.subplot(2,3,3)
    plt.imshow(im_contorno, cmap='gray')
    plt.plot(Cx,Cy,'r*')
    plt.title("Centro")
    
    plt.subplot(2,3,4)
    plt.imshow(im_bin, cmap='gray')
    plt.plot(poligono_approx[:,0,0],poligono_approx[:,0,1],'r')
    plt.title("Aproximación Poligonal")
    
    plt.subplot(2,3,5)
    plt.imshow(im_bin, cmap='gray')
    plt.plot(cerco_convexo[:,0],cerco_convexo[:,1],'r')
    plt.title("Cerco Convexo")
    
    plt.subplot(2,3,6)
    im_cerco = cv.merge((im_bin,im_bin,im_bin))
    cv.rectangle(im_cerco,(x,y),(x+w,y+h),(255,0,0),6)
    plt.imshow(im_cerco)
    plt.title("Cerco Rectangular")
    
    plt.show()
    

if __name__ == '__main__':
    im = cv.imread("Figuras.png")
    im = cv.cvtColor(im,cv.COLOR_BGR2HSV)
    
    descriptores(im,0) # 5, 4, 3, 1, 0, 2

    
    
    