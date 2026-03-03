import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np


def transformada_fourier(im):
    
    im_DFT = cv.dft(np.float32(im),flags=cv.DFT_COMPLEX_OUTPUT)
    im_DFT_DB = 20*np.log(cv.magnitude(im_DFT[:,:,0],im_DFT[:,:,1]))
    
    im_DFT_shift = np.fft.fftshift(im_DFT)
    im_DFT_DB_shift = 20*np.log(cv.magnitude(im_DFT_shift[:,:,0],im_DFT_shift[:,:,1]))
    
    alto, ancho = im.shape
    offset = 3
    mask = np.zeros((alto,ancho,2),np.uint8)
    #mask[int(alto/2)-offset:int(alto/2)+offset, int(ancho/2)-offset:int(ancho/2)+offset] = 255
    mask[int(alto/2)-offset:int(alto/2)+offset, 0:ancho] = 255
    mask = cv.bitwise_not(mask)/255
    
    im_DFT_mascara = im_DFT_shift*mask
    im_DFT_DB_mascara = 20*np.log(cv.magnitude(im_DFT_mascara[:,:,0],im_DFT_mascara[:,:,1]))
    
    im_DFT_unshift = np.fft.ifftshift(im_DFT_mascara)
    im_iDFT = cv.idft(im_DFT_unshift)
    im_mascara = cv.magnitude(im_iDFT[:,:,0],im_iDFT[:,:,1])    # No esta normalizada (entre 0 y 255)
    
    plt.figure()
    
    plt.subplot(2,3,1)
    plt.imshow(im, cmap='gray')
    plt.title("Foto")
    
    plt.subplot(2,3,2)
    plt.imshow(im_DFT_DB, cmap='gray')
    plt.title("DFT (en DB)")
    
    plt.subplot(2,3,3)
    plt.imshow(im_DFT_DB_shift, cmap='gray')
    plt.title("DFT_shift (en DB)")
    
    plt.subplot(2,3,4)
    plt.imshow(mask[:,:,0], cmap='gray')
    plt.title("Máscara")
    
    plt.subplot(2,3,5)
    plt.imshow(im_DFT_DB_mascara, cmap='gray')
    plt.title("DFT con Máscara (en DB)")
    
    plt.subplot(2,3,6)
    plt.imshow(im_mascara, cmap='gray')
    plt.title("Imagen Filtrada")
    
    plt.show()
    

if __name__ == '__main__':
    im = cv.imread("rayas.png")
    im = cv.cvtColor(im,cv.COLOR_BGR2GRAY)

    transformada_fourier(im)
    
    
    