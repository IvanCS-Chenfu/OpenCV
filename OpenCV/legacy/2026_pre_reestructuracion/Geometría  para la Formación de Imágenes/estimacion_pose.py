import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

import os
import glob
from enum import Enum

class DrawOption(Enum):
    Axes = 1
    Cube = 2
    

def dibujar_ejes(im, corners, im_pts):
    def tupleOfInts(arr):
        return tuple(int(x) for x in arr)
    
    corner = tupleOfInts(corners[0].ravel())
    
    im = cv.line(im,corner,tupleOfInts(im_pts[0].ravel()),(255,0,0),5)
    im = cv.line(im,corner,tupleOfInts(im_pts[1].ravel()),(0,255,0),5)
    im = cv.line(im,corner,tupleOfInts(im_pts[2].ravel()),(0,0,255),5)
    
    return im

def dibujar_cubo(im, im_pts):
    im_pts = np.int32(im_pts).reshape(-1,2)
    
    im = cv.drawContours(im,[im_pts[:4]],-1,(0,255,0),-3)
    
    for i in range(4):
        j = i + 4
        
        im = cv.line(im,tuple(im_pts[i]),tuple(im_pts[j]),(255),3)
        im = cv.drawContours(im,[im_pts[:4]],-1,(0,0,255),3)
        
    
    return im
    
def estimar_pose(option: DrawOption):
    
    # Obtener Calibracion
    root = os.getcwd()
    path_parametros = os.path.join(root,"calibracion.npz")
    data = np.load(path_parametros)
    camMatrix = data["camMatrix"]
    distCoeff = data["distCoeff"]
    
    path_directorio = os.path.join(root, './imagenes_calibracion')
    path_imagenes= glob.glob(os.path.join(path_directorio, "*.png"))
    
    # Inicializar
    nRows = 9
    nCols = 6
    
    termCriteria = (cv.TermCriteria_EPS + cv.TermCriteria_MAX_ITER, 30, 0.001)
    
    worldPts_Actual = np.zeros((nRows*nCols,3), np.float32)
    worldPts_Actual[:,:2] = np.mgrid[0:nRows,0:nCols].T.reshape(-1,2)
    
    ejes = np.float32([[3,0,0],[0,3,0],[0,0,-3]])
    esquinas_cubo = np.float32([[0,0,0],[0,3,0],[3,3,0],[3,0,0],[0,0,-3],[0,3,-3],[3,3,-3],[3,0,-3]])
    
    for path_imagen in path_imagenes:
        im = cv.imread(path_imagen)
        im_gray = cv.cvtColor(im, cv.COLOR_BGR2GRAY)
        
        cornersFound, cornersOrg = cv.findChessboardCorners(im_gray, (nRows, nCols), None)
        
        if cornersFound == True:
            
            cornersRefined = cv.cornerSubPix(im_gray, cornersOrg, (11,11), (-1,-1), termCriteria)
            
            _, rvecs, tvecs = cv.solvePnP(worldPts_Actual, cornersRefined, camMatrix, distCoeff)
            
            if option == DrawOption.Axes:
                im_pts, _ = cv.projectPoints(ejes,rvecs,tvecs,camMatrix,distCoeff)
                im = dibujar_ejes(im, cornersRefined, im_pts)
                
            if option == DrawOption.Cube:
                im_pts, _ = cv.projectPoints(esquinas_cubo,rvecs,tvecs,camMatrix,distCoeff)
                im = dibujar_cubo(im, im_pts)
                
            cv.imshow("ChessBoard", im)
            cv.waitKey(1000)
            
    cv.destroyAllWindows()


if __name__ == '__main__':
    
    estimar_pose(DrawOption.Cube)
    
