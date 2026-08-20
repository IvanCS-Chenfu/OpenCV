import cv2 as cv
import os

def readImage(imPath):
    # Obtiene la Imagen dado un Path
    img = cv.imread(imPath)
    return img


def mostrarImage(im):
    cv.imshow('titulo_de_imagen',im)

    # Tiempo que se mantiene la imagen en "ms".
    # Si se pone 0, la imagen se mantiene para siempre y hay que pulsar "Enter" para que el programa siga.
    cv.waitKey(0)   


def ImageInfo(im):
    # Tipo de Datos
    tipo_dato = im.dtype
    
    # Valores máximos y mínimos
    max = im.max()
    min = im.min()
    
    # Tamaño
    tam = im.shape
    tam_x = im.shape[0]
    tam_y = im.shape[1]
    tam_z = im.shape[2]
    
    print("Tipo de Dato: ", tipo_dato, "\n")
    print("Máximo: ", max, ". Mínimo: ", min, "\n")
    print("Tamaño: ", tam, ". Filas: ", tam_x, ". Columnas: ",tam_y, ". Colores: ", tam_z, "\n")
    

def writeImage(im, root, nombre):
    outPath = os.path.join(root, nombre)
    
    # Guarda (o sobrescribe) una Imagen en un Path
    cv.imwrite(outPath, im)


if __name__ == '__main__':
    root = os.getcwd()
    imgPath = os.path.join(root, 'Nombre_Imagen.png')
    
    img = readImage(imgPath)
    
    mostrarImage(img)
        
    ImageInfo(img)
    
    writeImage(img, root, 'Nombre_Imagen_Guardar.png')
