import cv2 as cv
import os
import matplotlib.pyplot as plt



# Tenemos que tener en cuenta que OpenCV funciona con BGR y Matplotlib en RGB
def cambios_matplotVSopencv():
    
    root = os.getcwd()
    imPath = os.path.join(root, 'Nombre_Imagen.png')
    im = cv.imread(imPath)  # Imagen en BGR
    im_RGB = cv.cvtColor(im,cv.COLOR_BGR2RGB)

    cv.imshow('Imagen BGR OpenCV',im)
    cv.waitKey(0) 
    cv.destroyAllWindows()
    plt.figure()
    plt.imshow(im)
    plt.title('Imagen BGR Matplotlib')
    plt.show()  # Se queda bloqueado hasta que cierres la pestaña

    cv.imshow('Imagen RGB OpenCV',im_RGB)
    cv.waitKey(0) 
    cv.destroyAllWindows()
    plt.figure()
    plt.imshow(im_RGB)
    plt.title('Imagen RGB Matplotlib')
    plt.show()


# Se utiliza matplotlib ya que podemos ver la posición de los píxeles
def posicionPixeles():
    root = os.getcwd()
    imPath = os.path.join(root, 'Nombre_Imagen.png')
    im = cv.imread(imPath)  # Imagen en BGR
    im_RGB = cv.cvtColor(im,cv.COLOR_BGR2RGB)
    
    plt.figure()
    plt.imshow(im_RGB)
    plt.title('Gato')
    plt.show()

    ojos = im_RGB[274:372, 203:602]
    plt.figure()
    plt.imshow(ojos)
    plt.title('Ojos de Gato')
    plt.show()
    
    im_RGB[311, 347] = (255, 0, 0)      # Los pixeles de im_RGB están alreves "[y,x]"
    plt.figure()
    plt.imshow(im_RGB)
    plt.title('Gato con Pixel Rojo en el Ojo')
    plt.show() 

    im_RGB[274:372, 203:602] = (0, 255, 0)
    plt.figure()
    plt.imshow(im_RGB)
    plt.title('Gato con Antifaz Verde')
    plt.show()



if __name__ == '__main__':
    cambios_matplotVSopencv()
     
    posicionPixeles()