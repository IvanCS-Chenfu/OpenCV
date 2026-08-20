import cv2 as cv
import matplotlib.pyplot as plt

def umbralize(im):
    
    # Todos los Métodos de Umbralización
    MetodosUmbralizacion = [
        cv.THRESH_BINARY,       # 255 es el color en el cual se muestran los pixeles que superen el umbral.
        cv.THRESH_BINARY_INV,   # 255 es el color en el cual se muestran los pixeles que no superen el umbral.
        cv.THRESH_TOZERO,       # Pone a 0 los valores que no superan el umbral. Los demás los dejan igual.
        cv.THRESH_TOZERO_INV,   # Pone a 0 los valores que superan el umbral. Los demás lo dejan igual.
        cv.THRESH_TRUNC         # Pone los pixeles que superan el umbral al color del umbral. Los demás los dejan igual.
    ]

    NombresMetodos = [
        "binary",
        "binary_inv",
        "tozero",
        "tozero_inv",
        "trunc"
    ]

    plt.figure()
    plt.subplot(2,4,1)
    plt.imshow(im, cmap='gray')
    
    umbral = 130
    color_mostrar = 180 # Como quiero que se muestre el pixel que se va a mostrar tras la umbralización (binaria)
    hist = cv.calcHist([im],[0],None,[256],[0,256])
    
    plt.subplot(2,4,2)
    plt.plot(hist)
    plt.axvline(x=umbral, color='r')
    plt.title("Histograma Gris")

    for i in range(len(MetodosUmbralizacion)):
        plt.subplot(2,4,i+3)
        
        _, im_umbr = cv.threshold(im, umbral, color_mostrar, MetodosUmbralizacion[i])
        
        plt.imshow(im_umbr, cmap='gray')
        plt.title(NombresMetodos[i])
        
    plt.show()



def adaptative_umbralize(im):
    
    plt.figure()
    plt.subplot(1,3,1)
    plt.imshow(im, cmap='gray')
    
    max_value = 255
    block_size = 17
    offsetC = 2
    
    # Sobre un entorno [block_size x block_size] se calcula un valor realizando la media de los valores.
    # A ese valor se le resta el offset siendo este el umbral de la zona.
    im_umbr = cv.adaptiveThreshold(im, max_value, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, block_size, offsetC)
    
    plt.subplot(1,3,2)
    plt.imshow(im_umbr, cmap='gray')
    plt.title("Mean")
    
    im_umbr = cv.adaptiveThreshold(im, max_value, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, block_size, offsetC)
    
    plt.subplot(1,3,3)
    plt.imshow(im_umbr, cmap='gray')
    plt.title("Gauss")
    
    plt.show()
    

def umbralize_OTSU(im):
    
    plt.figure()
    plt.subplot(1,3,1)
    plt.imshow(im, cmap='gray')
    
    _, im_umbr = cv.threshold(im, 130, 255, cv.THRESH_BINARY)
    
    plt.subplot(1,3,2)
    plt.imshow(im_umbr, cmap='gray')
    plt.title("Binario Normal")
    
    umbral_cualquiera = 0
    _, im_umbr = cv.threshold(im, umbral_cualquiera, 255, cv.THRESH_BINARY+cv.THRESH_OTSU)
    
    plt.subplot(1,3,3)
    plt.imshow(im_umbr, cmap='gray')
    plt.title("OTSU")
    
    plt.show()
    
    
if __name__ == '__main__':
    im = cv.imread("Gato.png")
    im = cv.cvtColor(im,cv.COLOR_BGR2GRAY)
    
    umbralize(im)
    
    adaptative_umbralize(im)
    
    umbralize_OTSU(im)