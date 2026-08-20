import cv2 as cv
import matplotlib.pyplot as plt

def resize(im, escalado):
    im = im[17:545,228:745,:]
    height, width, _ = im.shape
    
    # Todos los Métodos de Interpolación para realizar e Resize
    MetodosInterpolacion = [
        cv.INTER_AREA,
        cv.INTER_LINEAR,
        cv.INTER_NEAREST,
        cv.INTER_CUBIC,
        cv.INTER_LANCZOS4
    ]

    NombresMetodos = [
        "area",
        "linear",
        "nearest",
        "cubic",
        "lanczos4"
    ]

    plt.figure()
    plt.subplot(2,3,1)
    plt.imshow(im)
    
    for i in range(len(MetodosInterpolacion)):
        plt.subplot(2,3,i+2)
        
        # RESIZE
        new_tam = (int(width*escalado), int(height*escalado))
        imResize = cv.resize(im, new_tam, interpolation=MetodosInterpolacion[i])
        plt.imshow(imResize)
        plt.title(NombresMetodos[i])
        
    plt.show()

if __name__ == '__main__':
    im = cv.imread("Gato.png")
    im = cv.cvtColor(im,cv.COLOR_BGR2RGB)
    resize(im,1/16)