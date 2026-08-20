import cv2 as cv
import matplotlib.pyplot as plt

def bordes(im):
    
    # Todos los Métodos para Ampliar la Imagen con un borde
    TiposBorde = [
        cv.BORDER_CONSTANT,
        cv.BORDER_REFLECT,
        cv.BORDER_REPLICATE,
        cv.BORDER_WRAP
    ]

    NombresBordes = [
        "constant",
        "reflect",
        "replicate",
        "wrap"
    ]
    
    tam = (200, 100, 50, 300)   # Cuantos pixeles a añadir en cada dirección

    plt.figure()
    plt.subplot(2,3,1)
    plt.imshow(im)
    
    for i in range(len(TiposBorde)):
        plt.subplot(2,3,i+2)
        
        im_border = cv.copyMakeBorder(im, tam[0], tam[1], tam[2], tam[3], TiposBorde[i])
        
        plt.imshow(im_border)
        plt.title(NombresBordes[i])
        
    plt.show()

if __name__ == '__main__':
    im = cv.imread("Gato.png")
    im = cv.cvtColor(im,cv.COLOR_BGR2RGB)
    
    bordes(im)