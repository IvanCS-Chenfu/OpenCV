import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

def convolucion(im, kernel):
    
    plt.figure()
    plt.subplot(1,2,1)
    plt.imshow(im)
    
    plt.subplot(1,2,2)
    im_conv = cv.filter2D(im, -1, kernel)
    plt.imshow(im_conv)
        
    plt.show()

if __name__ == '__main__':
    im = cv.imread("Gato.png")
    im = cv.cvtColor(im,cv.COLOR_BGR2RGB)
    
    kernel1 = np.ones((100,100), np.float32) / (100*100)
    convolucion(im, kernel1)
    
    kernel2 = np.array([[1, 2, 1],
                        [0, 0, 0],
                        [-1, -2, -1]], np.float32)
    convolucion(im, kernel2)
    
    kernel3 = np.array([[1, 0, -1],
                        [2, 0, -2],
                        [1, 0, -1]], np.float32)
    convolucion(im, kernel3)
    
