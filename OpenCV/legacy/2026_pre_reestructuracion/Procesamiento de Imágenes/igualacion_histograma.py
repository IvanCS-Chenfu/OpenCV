import cv2 as cv
import matplotlib.pyplot as plt


def igualacion_hist(im):
    
    hist = cv.calcHist([im],[0],None,[256],[0,256])
    cumsum = hist.cumsum()
    cumsum_norm = cumsum * float(hist.max() / cumsum.max())
    
    
    im_equ = cv.equalizeHist(im)
    hist_equ = cv.calcHist([im_equ],[0],None,[256],[0,256])
    cumsum_equ = hist_equ.cumsum()
    cumsum_equ_norm = cumsum_equ * float(hist.max() / cumsum_equ.max())
    
    
    objeto_clahe = cv.createCLAHE(clipLimit=5, tileGridSize=(8,8))
    im_clahe = objeto_clahe.apply(im)
    hist_clahe = cv.calcHist([im_clahe],[0],None,[256],[0,256])
    cumsum_clahe = hist_clahe.cumsum()
    cumsum_clahe_norm = cumsum_clahe * float(hist.max() / cumsum_clahe.max())
    
    plt.figure()
    
    plt.subplot(2,3,1)
    plt.imshow(im, cmap='gray')
    plt.title("Foto")
    
    plt.subplot(2,3,4)
    plt.plot(hist)
    plt.plot(cumsum_norm, color = 'b')
    plt.title("Histograma y CumSum")
    
    
    plt.subplot(2,3,2)
    plt.imshow(im_equ, cmap='gray')
    plt.title("Igualación Histograma")
    
    plt.subplot(2,3,5)
    plt.plot(hist_equ)
    plt.plot(cumsum_equ_norm, color = 'b')
    plt.title("Histograma y CumSum")
    
    
    plt.subplot(2,3,3)
    plt.imshow(im_clahe, cmap='gray')
    plt.title("CLAHE")
    
    plt.subplot(2,3,6)
    plt.plot(hist_clahe)
    plt.plot(cumsum_clahe_norm, color = 'b')
    plt.title("Histograma y CumSum")
    
    plt.show()
    

if __name__ == '__main__':
    im = cv.imread("imagen_oscura.png")
    im = cv.cvtColor(im,cv.COLOR_BGR2GRAY)
    
    igualacion_hist(im)
    
    im = cv.imread("imagen_clara.png")
    im = cv.cvtColor(im,cv.COLOR_BGR2GRAY)
    
    igualacion_hist(im)
    
    im = cv.imread("entorno.png")
    im = cv.cvtColor(im,cv.COLOR_BGR2GRAY)
    
    igualacion_hist(im)
    
    
    