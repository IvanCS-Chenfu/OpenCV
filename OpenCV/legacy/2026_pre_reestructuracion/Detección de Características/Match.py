import cv2 as cv
import matplotlib.pyplot as plt

def Fuerza_Bruta(im1, im2):

    objeto_orb = cv.ORB_create()
    
    keypoints1, descriptor1 = objeto_orb.detectAndCompute(im1,None)
    keypoints2, descriptor2 = objeto_orb.detectAndCompute(im2,None)
    # keypoints: posiciones (x,y) + escala/orientacion (depende)
    # descriptores: uint8 (32 bytes = 256 bits). Binario -> distancia Hamming
    
    fuerza_bruta_objeto = cv.BFMatcher(cv.NORM_HAMMING,crossCheck=True) # CrossCheck dice que si un match A->B es válido solo cuando B->A también es un match
    
    matches = fuerza_bruta_objeto.match(descriptor1, descriptor2)   # Match: 1 vecino (el más cercano)
    # matches.queryIdx: tiene el índice del descriptor 1
    # matches.trainIdx: tiene el índice del descriptor 2
    # matches.distance: tiene la distancia hamming entre ambos descriptores
    
    matches = sorted(matches,key=lambda x:x.distance)
    # reagrupa los matches según el valor de distancia (los más cercanos primero)
    
    n_matches = 10
    flags = cv.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS  # Para solo mostrar los matches
    
    im_matches = cv.drawMatches(im1,keypoints1,im2,keypoints2,matches[:n_matches], None, flags=flags)
    # Devuelve una imagen conjunta en la cual se muestran los "N" primeros matches 
    plt.figure()
    
    plt.subplot(3,1,1)
    plt.imshow(im1, cmap='gray')
    plt.title("Foto1")
    
    plt.subplot(3,1,2)
    plt.imshow(im2, cmap='gray')
    plt.title("Foto2")
    
    plt.subplot(3,1,3)
    plt.imshow(im_matches, cmap='gray')
    plt.title("Matches")

    plt.show()
    
    
    
    
def Fuerza_Bruta_KNN(im1, im2):

    objeto_sift = cv.SIFT_create()
    
    keypoints1, descriptor1 = objeto_sift.detectAndCompute(im1,None)
    keypoints2, descriptor2 = objeto_sift.detectAndCompute(im2,None)
    # keypoints: posiciones (x,y) + escala/orientacion (depende)
    # descriptores: float (128 valores). Float -> distancia Euclidea (L2)
    
    fuerza_bruta_objeto = cv.BFMatcher()
    vecinos = 2
    matches = fuerza_bruta_objeto.knnMatch(descriptor1, descriptor2, k=vecinos)  # Match: 2 vecinos (los más cercanos)
    # Para cada descriptor de una iamgen, se hace match con los 2 descriptores de la otra imagen que sean más cercanos.
    # Los más cercanos se encuentran en la primera columna y los más lejanos en la segunda
    matches_buenos = []
    testRatio = 0.75
    
    # Se comprueba si la distancia de un descriptor a sus 2 vecinos es muy diferente. Si la distancia al primer descriptor (m) 
    # es mucho mayor que la distancia al segundo (n), ese match es bueno. Si ambas distancias son parecidas es match no es bueno.
    for m,n in matches:
        if m.distance < testRatio*n.distance:
            matches_buenos.append(m)

    matches_buenos = sorted(matches_buenos,key=lambda x:x.distance)
    
    n_matches = 10
    flags = cv.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS  # Para solo mostrar los matches
    
    im_matches = cv.drawMatches(im1,keypoints1,im2,keypoints2,matches_buenos[:n_matches], None, flags=flags)
    
    plt.figure()
    
    plt.subplot(3,1,1)
    plt.imshow(im1, cmap='gray')
    plt.title("Foto1")
    
    plt.subplot(3,1,2)
    plt.imshow(im2, cmap='gray')
    plt.title("Foto2")
    
    plt.subplot(3,1,3)
    plt.imshow(im_matches, cmap='gray')
    plt.title("Matches")

    plt.show()




def FLANN(im1, im2, flag_todos):

    objeto_sift = cv.SIFT_create()
    
    keypoints1, descriptor1 = objeto_sift.detectAndCompute(im1,None)
    keypoints2, descriptor2 = objeto_sift.detectAndCompute(im2,None)
    # keypoints: posiciones (x,y) + escala/orientacion (depende)
    # descriptores: float (128 valores). Float -> distancia Euclidea (L2)
    
    FLANN_INDEX_KDTREE = 1  # Bueno para descriptores tipo Float.
    nKDtrees = 5            # Más arboles -> más precisión pero más tiempo.
    nLeafChecks = 50        # Más hojas -> más precisión pero más tiempo
    indexParams = dict(algorithm = FLANN_INDEX_KDTREE, trees = nKDtrees)
    searchParams = dict(checks = nLeafChecks)
    
    objeto_flann = cv.FlannBasedMatcher(indexParams,searchParams)
    
    vecinos = 2
    matches = objeto_flann.knnMatch(descriptor1, descriptor2, k=vecinos)
    
    testRatio = 0.75
    
    
    im_matches = []
    
    if flag_todos:
        # Esta forma de hacerlo es diferente, pero hace lo mismo que el else.
        matches_buenos = [[0,0] for i in range(len(matches))]
        for i,(m,n) in enumerate(matches):
            if m.distance < testRatio*n.distance:
                matches_buenos[i] = [1,0]
        
        drawParams = dict(matchColor = (0, 255, 0), singlePointColor = (255, 0, 0), matchesMask = matches_buenos, flags = cv.DrawMatchesFlags_DEFAULT)
        
        im_matches = cv.drawMatchesKnn(im1,keypoints1,im2,keypoints2,matches, None, **drawParams)
    else:
        matches_buenos = []
        for m,n in matches:
            if m.distance < testRatio*n.distance:
                matches_buenos.append(m)

        matches_buenos = sorted(matches_buenos,key=lambda x:x.distance)
        
        n_matches = 10
        flags = cv.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS  # Para solo mostrar los matches
        
        im_matches = cv.drawMatches(im1,keypoints1,im2,keypoints2,matches_buenos[:n_matches], None, flags=flags)
    
    plt.figure()
    
    plt.subplot(3,1,1)
    plt.imshow(im1, cmap='gray')
    plt.title("Foto1")
    
    plt.subplot(3,1,2)
    plt.imshow(im2, cmap='gray')
    plt.title("Foto2")
    
    plt.subplot(3,1,3)
    plt.imshow(im_matches, cmap='gray')
    plt.title("Matches")

    plt.show()
    



if __name__ == '__main__':
    im1 = cv.imread("facultad1.png")
    im2 = cv.imread("facultad2.png")
    im1 = cv.cvtColor(im1,cv.COLOR_BGR2GRAY)
    im2 = cv.cvtColor(im2,cv.COLOR_BGR2GRAY)
    
    Fuerza_Bruta(im1, im2)

    Fuerza_Bruta_KNN(im1, im2)
    
    FLANN(im1, im2, False)
    
    
    