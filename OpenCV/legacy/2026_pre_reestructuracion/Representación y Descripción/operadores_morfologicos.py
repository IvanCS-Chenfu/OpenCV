import cv2 as cv
import matplotlib.pyplot as plt

def operadores(im, kernel):
    
    _,im_bin = cv.threshold(im,10,255,cv.THRESH_BINARY)

    plt.figure()
    plt.subplot(2,4,1)
    plt.imshow(im_bin, cmap='gray')
    
    im_erosion = cv.erode(im_bin,kernel)

    plt.subplot(2,4,2)
    plt.imshow(im_erosion, cmap='gray')
    plt.title("Erosion")
    
    im_dilatacion = cv.dilate(im_bin,kernel)

    plt.subplot(2,4,3)
    plt.imshow(im_dilatacion, cmap='gray')
    plt.title("Dilatacion")

    # Todos los Operadores Morfológicos
    OperadoresMorfologicos = [
        cv.MORPH_OPEN,          # dilate(erode(im))
        cv.MORPH_CLOSE,         # erode(dilate(im))
        cv.MORPH_GRADIENT,      # dilate(im) - erode(im)
        cv.MORPH_TOPHAT,        # im - open(im)
        cv.MORPH_BLACKHAT       # close(im) - im
    ]

    NombresOperadores = [
        "open",
        "close",
        "gradient",
        "tophat",
        "blackhat"
    ]
    
    
    for i in range(len(OperadoresMorfologicos)):
        
        im_op = cv.morphologyEx(im_bin, OperadoresMorfologicos[i], kernel)
        
        plt.subplot(2,4,i+4)
        plt.imshow(im_op, cmap='gray')
        plt.title(NombresOperadores[i])
    
    plt.show()


    
if __name__ == '__main__':
    im = cv.imread("binarizada.png")
    im = cv.cvtColor(im,cv.COLOR_BGR2GRAY)
    
    tam_kernel = (4,4)
    cruz = cv.getStructuringElement(cv.MORPH_CROSS,tam_kernel)
    elipse = cv.getStructuringElement(cv.MORPH_ELLIPSE,tam_kernel)
    rectangulo = cv.getStructuringElement(cv.MORPH_RECT,tam_kernel)
    
    operadores(im, rectangulo)