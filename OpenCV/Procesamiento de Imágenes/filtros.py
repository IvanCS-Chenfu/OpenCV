import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

def filtros(im):
    
    plt.figure()
    
    plt.subplot(2,3,1)
    plt.imshow(im)
    plt.title("Foto")
    
    
    plt.subplot(2,3,2)
    
    tam_kernel = (5,5)
    im_blur = cv.blur(im,tam_kernel)
    
    plt.imshow(im_blur)
    plt.title("Media (Blur)")
    
    plt.subplot(2,3,3)
    
    tam_kernel = 9
    im_medianblur = cv.medianBlur(im,tam_kernel)
    
    plt.imshow(im_medianblur)
    plt.title("Mediana (Median_Blur)")
    
    plt.subplot(2,3,4)
    
    tam_kernel = (9,15)
    sigma = 4
    kernel_gauss1D_1 = cv.getGaussianKernel(tam_kernel[0], sigma)
    kernel_gauss1D_2 = cv.getGaussianKernel(tam_kernel[1], sigma)
    kernel_gauss2D = np.outer(kernel_gauss1D_1, kernel_gauss1D_2)
        
    plt.imshow(kernel_gauss2D)
    plt.title("Kernel Gaussiano")
    
    plt.subplot(2,3,5)
    
    im_gausianblur = cv.GaussianBlur(im, tam_kernel, sigma)
        
    plt.imshow(im_gausianblur)
    plt.title("Gausiano (Gausian_Blur)")
    
    plt.subplot(2,3,6)
    
    dist = 9
    delta_color = 25
    delta_dist =  25
    
    # Útil para mantener bordes ya que calcula una media ponderada en la cual los pixeles más cercanos
    # o más parecidos tienen más peso que los más alejados o diferentes.
    im_bilateral = cv.bilateralFilter(im, dist, delta_color, delta_dist)    
        
    plt.imshow(im_bilateral)
    plt.title("Bilateral")
    
    plt.show()
    

if __name__ == '__main__':
    im = cv.imread("ruidos.png")
    im = cv.cvtColor(im,cv.COLOR_BGR2RGB)
    
    filtros(im)
    
    
    