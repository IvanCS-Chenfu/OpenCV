import cv2 as cv
import matplotlib.pyplot as plt


def gradiente_laplaciana(im):
    
    _,_,im_v = cv.split(im)
    
    tam = 21
    
    sobelX = cv.Sobel(im_v, cv.CV_64F, 1, 0, ksize=tam)
    sobelY = cv.Sobel(im_v, cv.CV_64F, 0, 1, ksize=tam)
    laplacian = cv.Laplacian(im_v, cv.CV_64F, ksize=tam)
    
    kx, ky = cv.getDerivKernels(1,0,tam)
    print(ky@kx.T)
    
    plt.figure()
    
    plt.subplot(2,2,1)
    plt.imshow(im_v, cmap='gray')
    plt.title("Foto (Value)")
    
    plt.subplot(2,2,2)
    plt.imshow(sobelX, cmap='gray')
    plt.title("SobelX")
    
    
    plt.subplot(2,2,3)
    plt.imshow(sobelY, cmap='gray')
    plt.title("SobelY")
    
    plt.subplot(2,2,4)
    plt.imshow(laplacian, cmap='gray')
    plt.title("Laplacian")
    
    plt.show()
    

if __name__ == '__main__':
    im = cv.imread("Figuras.png")
    im = cv.cvtColor(im,cv.COLOR_BGR2HSV)
    
    gradiente_laplaciana(im)
    
    
    