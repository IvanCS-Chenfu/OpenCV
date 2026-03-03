import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt


def traslacion(im, px, py, escala):
    
    # Matriz de Transformación de Traslación
    T = np.array([[escala, 0, px],
                  [0, escala, py]],dtype=np.float32)
    
    # Aplicar Matriz de Transformación
    tam = (im.shape[1],im.shape[0])
    im_tras = cv.warpAffine(im,T,tam)
    
    plt.figure()
    
    plt.subplot(1,2,1)
    plt.imshow(im)
    plt.title("Normal")
    
    plt.subplot(1,2,2)
    plt.imshow(im_tras)
    plt.title("Traslacion")
    
    plt.show()
    
def rotacion(im, centro, angulo, escala):
    
    # Matriz de Transformación de Traslación
    T =cv.getRotationMatrix2D(centro, angulo, escala)
    
    # Aplicar Matriz de Transformación
    tam = (im.shape[1],im.shape[0])
    im_rot = cv.warpAffine(im,T,tam)
    
    plt.figure()
    
    plt.subplot(1,2,1)
    plt.imshow(im)
    plt.title("Normal")
    
    plt.subplot(1,2,2)
    plt.imshow(im_rot)
    plt.title("Rotacion")
    
    plt.show()
    

# Afinidad transformando 3 puntos en otros 3
def afinidad(im, p_antes, p_despues):
    
    # Matriz de Transformación de Afinidad
    T =cv.getAffineTransform(p_antes, p_despues)
    
    # Aplicar Matriz de Transformación
    tam = (im.shape[1],im.shape[0])
    im_afin = cv.warpAffine(im,T,tam)
    im_puntos = im.copy()
    
    plt.figure()
    plt.subplot(1,2,1)
    
    p1 = tuple(p_antes[0].astype(int))
    p2 = tuple(p_antes[1].astype(int))
    p3 = tuple(p_antes[2].astype(int))
    cv.circle(im_puntos, p1, 10, (255,0,0), -1) 
    cv.circle(im_puntos, p2, 10, (255,0,0), -1) 
    cv.circle(im_puntos, p3, 10, (255,0,0), -1) 
    
    plt.imshow(im_puntos)
    plt.title("Normal")
    
    plt.subplot(1,2,2)
    
    p1 = tuple(p_despues[0].astype(int))
    p2 = tuple(p_despues[1].astype(int))
    p3 = tuple(p_despues[2].astype(int))
    cv.circle(im_afin, p1, 10, (255,0,0), -1) 
    cv.circle(im_afin, p2, 10, (255,0,0), -1) 
    cv.circle(im_afin, p3, 10, (255,0,0), -1) 
    
    plt.imshow(im_afin)
    plt.title("Afinidad")
    
    plt.show()
    

# Normalizar mediante homografia
def homografia(im, p_antes):
    
    p_despues = np.array([[0, 0],       # P1
                          [100, 0],     # P2
                          [100, 100],   # P3
                          [0, 100]],dtype=np.float32)   # P4
    
    # Matriz de Transformación de Afinidad
    T =cv.getPerspectiveTransform(p_antes, p_despues)
    
    # Aplicar Matriz de Transformación
    tam = (100,100)
    im_hom = cv.warpPerspective(im,T,tam)
    im_puntos = im.copy()
    
    plt.figure()
    plt.subplot(1,2,1)
    
    p1 = tuple(p_antes[0].astype(int))
    p2 = tuple(p_antes[1].astype(int))
    p3 = tuple(p_antes[2].astype(int))
    p4 = tuple(p_antes[3].astype(int))
    cv.circle(im_puntos, p1, 10, (255,0,0), -1) 
    cv.circle(im_puntos, p2, 10, (255,0,0), -1) 
    cv.circle(im_puntos, p3, 10, (255,0,0), -1) 
    cv.circle(im_puntos, p4, 10, (255,0,0), -1) 
    
    plt.imshow(im_puntos)
    plt.title("Normal")
    
    plt.subplot(1,2,2)
    plt.imshow(im_hom)
    plt.title("Homografia")
    
    plt.show()




if __name__ == '__main__':
    im = cv.imread("Gato.png")
    im = cv.cvtColor(im,cv.COLOR_BGR2RGB)
    
    traslacion(im, 200, -100, 1)
    traslacion(im, 0, 0, 2)
    
    
    centro_giro = (im.shape[1]/2, im.shape[0]/2)
    rotacion(im, centro_giro, 90, 1)
    rotacion(im, (0,0), -45, 1)
    
    
    p_antes = np.array([[100, 100], # P1
                        [500, 100], # P2
                        [100, 500]],dtype=np.float32)   # P3
    p_despues = np.array([[50, 150],   # P1
                          [500, 100],   # P2
                          [150, 400]],dtype=np.float32) # P3
    afinidad(im, p_antes, p_despues)
    
    
    p_antes = np.array([[541, 286], # P1
                        [579, 287], # P2
                        [594, 351], # P3
                        [540, 340]],dtype=np.float32)   # P4
    homografia(im,p_antes)