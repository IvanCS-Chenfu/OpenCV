import cv2 as cv
import matplotlib.pyplot as plt


def FAST(im, flag_parametros):
    
    ## Este objeto puede detectar keypoints
    objeto_fast = None
    if not flag_parametros:
        objeto_fast = cv.FastFeatureDetector_create()  # Sin parámetros 
        
        dif_min_intensidad = 100    # Umbral a superar
        objeto_fast.setThreshold(dif_min_intensidad)
    else:
        dif_min_intensidad = 100    # Umbral a superar
        nonmax = True       # Usar "Non-Maximun Suppresion (NMS). Si no se utiliza puede marcar varios puntos donde solo hay 1"
        type = cv.FAST_FEATURE_DETECTOR_TYPE_9_16   # Significa que de 16 pixeles, tiene que haber 9 consecutivos que cumplan la condición.
        
        objeto_fast = cv.FastFeatureDetector_create(threshold=dif_min_intensidad, nonmaxSuppression=nonmax, type=type)
    
    
    keypoints = objeto_fast.detect(im)
    print(f"Keypoints detectados: {len(keypoints)}")
    
    im_keypoints = im.copy()
    
    im_keypoints = cv.drawKeypoints(im_keypoints,keypoints,im_keypoints,color=(0,255,0))
    
    
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
    
    FAST(im, True)

    
    
    