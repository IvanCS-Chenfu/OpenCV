import cv2 as cv
import matplotlib.pyplot as plt


def ORB(im, flag_parametros, flag_descriptores):
    
    ## Este objeto puede detectar keypoints y calcular descriptores
    objeto_orb = None
    if not flag_parametros:
        objeto_orb = cv.ORB_create()  # Sin parámetros 
    else:
        objeto_orb = cv.ORB_create(
                                    nfeatures=500,      # Máximos keypoints (los mejores por score)
                                    scaleFactor=1.2,    # Factor entre nuveles de la pirámide (más cercano a 1 es más lento pero mejor)
                                    nlevels=8,          # Número de niveles de la pirámide
                                    edgeThreshold=31,   # Detalles de implementacion: evita keypoints cerca del borde.
                                    firstLevel=0,       # Detalles de implementacion: suele se 0
                                    WTA_K=2,            # Winer Takes All en la variante del descriptor (comparaciones). Mayor número mejor pero aumenta el coste
                                    scoreType=cv.ORB_HARRIS_SCORE,  # Como se ordenan los keypoints (por score)
                                    patchSize=31,       # Tamaño del parche para rotar BRIEF. Mayor número mejor pero más coste
                                    fastThreshold=20    # Unbral FAST interno
                                )
    
    keypoints = None
    if not flag_descriptores:
        keypoints = objeto_orb.detect(im,None) # Solo resuelve los puntos (posición, escala, orientación, respuesta...)
        keypoints, _ = objeto_orb.compute(im,keypoints)
    else:
        keypoints, descriptors = objeto_orb.detectAndCompute(im,None)  # Keypoints + Descriptores
        print(descriptors)
        print(f"Descriptores shape: {descriptors.shape}  (N_keypoints x 128)")
        print(f"Descriptor ejemplo (primer keypoint, primeros 10 valores): {descriptors[0, :10]}")
               
    
    print(f"Keypoints detectados: {len(keypoints)}")
    im_keypoints = im.copy()
    
    im_keypoints = cv.drawKeypoints(im_keypoints,keypoints,im_keypoints,flags=cv.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
    
    
    
    plt.figure()
    
    plt.subplot(1,2,1)
    plt.imshow(im, cmap='gray')
    plt.title("Foto")
    
    plt.subplot(1,2,2)
    plt.imshow(im_keypoints, cmap='gray')
    plt.title("Keypoints")
    
    plt.show()
    

def SIFT(im, flag_parametros, flag_descriptores):
    

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
    im_keypoints = cv.drawKeypoints(im_keypoints,keypoints,im_keypoints,flags=flags)    # imagen_a_dibujar, keypoints, imagen_salida (se puede poner None)


if __name__ == '__main__':
    im = cv.imread("Gente.png")
    im = cv.cvtColor(im,cv.COLOR_BGR2GRAY)
    
    ORB(im, True, True)

    
    
    