import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

import os
import glob

def readImages(path_imagenes):

    # Inicializar
    nRows = 9
    nCols = 6
    
    termCriteria = (cv.TermCriteria_EPS + cv.TermCriteria_MAX_ITER, 30, 0.001)
    
    worldPtsCur = np.zeros((nRows*nCols,3), np.float32)
    worldPtsCur[:,:2] = np.mgrid[0:nRows,0:nCols].T.reshape(-1,2)
    WorldPtsList = []
    imgPtsList = []
    
    for path_imagen in path_imagenes:
        im = cv.imread(path_imagen)
        im_gray = cv.cvtColor(im, cv.COLOR_BGR2GRAY)
        
        cornersFound, cornersOrg = cv.findChessboardCorners(im_gray, (nRows, nCols), None)
        
        if cornersFound == True:
            WorldPtsList.append(worldPtsCur)
            
            cornersRefined = cv.cornerSubPix(im_gray, cornersOrg, (11,11), (-1,-1), termCriteria)
            imgPtsList.append(cornersRefined)
            
            cv.drawChessboardCorners(im,(nRows,nCols), cornersRefined, cornersFound)
            cv.imshow("ChessBoard", im)
            cv.waitKey(500)
            
    cv.destroyAllWindows()

    repError, camMatrix, distCoeff, rvecs, tvecs = cv.calibrateCamera(WorldPtsList, imgPtsList, im_gray.shape[::-1], None, None)
    print("Camera Matrix: \n", camMatrix)
    print("Reproj Error (pixels): {:.4f}".format(repError))
    
    # Guardar
    path_directorio = os.path.dirname(os.path.abspath(__file__))
    path_guardar = os.path.join(path_directorio, "calibracion.npz")
    np.savez(path_guardar, repError=repError, camMatrix=camMatrix, distCoeff=distCoeff, rvecs=rvecs, tvecs=tvecs)
    
    return camMatrix, distCoeff





def EliminarDistorsion(camMatrix, distCoeff, im_distorsionada):
    h, w = im_distorsionada.shape[:2]
    
    nuevo_camMatrix, roi = cv.getOptimalNewCameraMatrix(camMatrix,distCoeff, (w,h), 1, (w,h))
    
    im = cv.undistort(im_distorsionada,camMatrix,distCoeff,None,nuevo_camMatrix)

    cv.line(im_distorsionada, (1000, 100), (900, 1000), (255, 0, 0), 2)
    cv.line(im, (1000, 100), (900, 1000), (255, 0, 0), 2)
    
    plt.figure()
    
    plt.subplot(1,2,1)
    plt.imshow(im_distorsionada)
    plt.title("Distorsion")
    
    plt.subplot(1,2,2)
    plt.imshow(im)
    plt.title("Sin Distorsion")
    
    plt.show()



if __name__ == '__main__':
    root = os.getcwd()
    path_directorio = os.path.join(root, './imagenes_calibracion')
    path_imagenes= glob.glob(os.path.join(path_directorio, "*.png"))
    
    camMatrix, distCoeff = readImages(path_imagenes)
    
    im = cv.imread("a_calibrar.png")
    EliminarDistorsion(camMatrix, distCoeff, im)
    
