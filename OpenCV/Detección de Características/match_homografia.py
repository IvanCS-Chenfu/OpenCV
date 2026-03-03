import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np


def match_homografia(im1, im2):

    objeto_sift = cv.SIFT_create()
    
    keypoints1, descriptor1 = objeto_sift.detectAndCompute(im1,None)
    keypoints2, descriptor2 = objeto_sift.detectAndCompute(im2,None)
    
    FLANN_INDEX_KDTREE = 1
    nKDtrees = 5
    nLeafChecks = 50
    vecinos = 2
    indexParams = dict(algorithm = FLANN_INDEX_KDTREE, trees = nKDtrees)
    searchParams = dict(checks = nLeafChecks)
    
    objeto_flann = cv.FlannBasedMatcher(indexParams,searchParams)
    matches = objeto_flann.knnMatch(descriptor1, descriptor2, k=vecinos)
    matches_buenos = []
    testRatio = 0.75
    
    for m,n in matches:
        if m.distance < testRatio*n.distance:
            matches_buenos.append(m)

    minGoodMatches = 20
    
    if len(matches_buenos) > minGoodMatches:
        srcPts = np.float32([keypoints1[m.queryIdx].pt for m in matches_buenos]).reshape(-1,1,2)
        dstPts = np.float32([keypoints2[m.trainIdx].pt for m in matches_buenos]).reshape(-1,1,2)
        # Obtengo los puntos (x,y) de los matches buenos
        
        # Utiliza RANSAC como se enseña en la teoría
        errorThreshold = 5
        M,mask = cv.findHomography(srcPts,dstPts,cv.RANSAC,errorThreshold)  # mask muestra con 1 los inliers y con 0 los outliers
        
        # Utiliza los inliers como máscara para no mostrar los outliers
        matchesMask = mask.ravel().tolist()
        
        # Muestra un borde en negro el cual muestra la homografía
        h,w = im1.shape
        imBorder = np.float32([[0,0],[0,h-1],[w-1,h-1],[w-1,0]]).reshape(-1,1,2)
        warpedImgBorder = cv.perspectiveTransform(imBorder,M)
        im2 = cv.polylines(im2,[np.int32(warpedImgBorder)],True,0,3,cv.LINE_AA)
    else:
        print("Not enough matches")
        matchesMask = None
        
    drawParams = dict(matchColor = (0, 255, 0), singlePointColor = None, matchesMask = matchesMask, flags = cv.DRAW_MATCHES_FLAGS_NOT_DRAW_SINGLE_POINTS)
    
    im_matches = cv.drawMatches(im1,keypoints1,im2,keypoints2, matches_buenos, None, **drawParams)
    
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
    
    match_homografia(im1, im2)
    
    
    