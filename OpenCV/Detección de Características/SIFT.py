import cv2 as cv
import matplotlib.pyplot as plt


def SIFT(im, flag_parametros, flag_descriptores):
    
    ## Este objeto puede detectar keypoints y calcular descriptores
    objeto_sift = None
    if not flag_parametros:
        objeto_sift = cv.SIFT_create()  # Sin parámetros 
    else:
        nfeatures = 100  # Número máximo de keypoints (con el fin de limitar ya que SIFT puede devolver muchísimos)
        contrastThreshold = 0.04  # Umbral mínimo para aceptar un extremo en el DoG (punto 3 de teoría)
        edgeThreshold = 10  # Elimina puntos en bordes usando la matriz Hessiana
        sigma = 1.6   # Sigma inicial
        
        objeto_sift = cv.SIFT_create(nfeatures=nfeatures, contrastThreshold=contrastThreshold, edgeThreshold=edgeThreshold, sigma=sigma)
    
    
    keypoints = None
    if not flag_descriptores:
        keypoints = objeto_sift.detect(im,None) # Solo resuelve los puntos (posición, escala, orientación, respuesta...)
    else:
        keypoints, descriptors = objeto_sift.detectAndCompute(im,None)  # Keypoints + Descriptores
        print(descriptors)
        print(f"Descriptores shape: {descriptors.shape}  (N_keypoints x 128)")
        print(f"Descriptor ejemplo (primer keypoint, primeros 10 valores): {descriptors[0, :10]}")
               
    
    print(f"Keypoints detectados: {len(keypoints)}")
    im_keypoints = im.copy()
    
    flags = cv.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS   # Hace que el círculo represente la escala del keypoint y la linea la orientación
    im_keypoints = cv.drawKeypoints(im_keypoints,keypoints,im_keypoints,flags=flags)    # imagen_a_dibujar, keypoints, imagen_salida (se puede poner None), flags
    
    
    
    plt.figure()
    
    plt.subplot(1,2,1)
    plt.imshow(im, cmap='gray')
    plt.title("Foto")
    
    plt.subplot(1,2,2)
    plt.imshow(im_keypoints, cmap='gray')
    plt.title("Keypoints")
    
    plt.show()
    




if __name__ == '__main__':
    im = cv.imread("Gente.png")
    im = cv.cvtColor(im,cv.COLOR_BGR2GRAY)
    
    SIFT(im, True, True)

    
    
    