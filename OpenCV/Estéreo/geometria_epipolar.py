import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

    
class EpipolarGeometry:
    def __init__(self,showImages):
        
        self.im_left = cv.imread("mueble_izq.png", cv.IMREAD_GRAYSCALE)
        self.im_right = cv.imread("mueble_der.png", cv.IMREAD_GRAYSCALE)
        
        if showImages:
            plt.figure()
            
            plt.subplot(1,2,1)
            plt.imshow(self.im_left, cmap='gray')
            plt.title("Izquierda")
            
            plt.subplot(1,2,2)
            plt.imshow(self.im_right, cmap='gray')
            plt.title("Derecha")
            
            plt.show()

    def dibujar_lineas_epipolar(self):
        
        objeto_sift = cv.SIFT_create()
        
        keypoints_left, descriptor_left = objeto_sift.detectAndCompute(self.im_left,None)
        keypoints_right, descriptor_right = objeto_sift.detectAndCompute(self.im_right,None)
        
        FLANN_INDEX_KDTREE = 1
        nKDtrees = 5
        nLeafChecks = 50
        indexParams = dict(algorithm = FLANN_INDEX_KDTREE, trees = nKDtrees)
        searchParams = dict(checks = nLeafChecks)
        objeto_flann = cv.FlannBasedMatcher(indexParams,searchParams)
    
        vecinos = 2
        matches = objeto_flann.knnMatch(descriptor_left, descriptor_right, k=vecinos)
        
        ptsLeft = []
        ptsRight = []
        
        testRatio = 0.75
        
        for i,(m,n) in enumerate(matches):
            if m.distance < testRatio*n.distance:
                ptsLeft.append(keypoints_left[m.queryIdx].pt)
                ptsRight.append(keypoints_right[m.trainIdx].pt)
                
        # Una vez obtenidos los keypoints que hacen match, se calcula la Matriz Fundamental mediante "Least Median of Squares"
        # la máscara devuelve 1 si el match es coherente con F (inlier). En caso de outlier es 0.
        ptsLeft = np.int32(ptsLeft)
        ptsRight = np.int32(ptsRight)
        F, mask = cv.findFundamentalMat(ptsLeft,ptsRight,cv.FM_LMEDS)
        
        ptsLeft = ptsLeft[mask.ravel()==1]
        ptsRight = ptsRight[mask.ravel()==1]
        
        # Solo para reducir el numero de puntos en el gráfico
        step = 10
        ptsLeft = ptsLeft[::step,:]
        ptsRight = ptsRight[::step,:]
        
        # Devuelve los coeficientes [a,b,c] de "ax + by + c = 0" de la linea epipolar de la imagen "2" (derecha)
        linesLeft = cv.computeCorrespondEpilines(ptsRight.reshape(-1,1,2),2,F)
        linesLeft = linesLeft.reshape(-1,3)
        im_lines_left, _ = EpipolarGeometry.drawLines(self.im_left,self.im_right,linesLeft,ptsLeft,ptsRight)
        
        # Devuelve los coeficientes [a,b,c] de "ax + by + c = 0" de la linea epipolar de la imagen "1" (izquierda)
        linesRight = cv.computeCorrespondEpilines(ptsLeft.reshape(-1,1,2),1,F)
        linesRight = linesRight.reshape(-1,3)
        im_lines_right, _ = EpipolarGeometry.drawLines(self.im_right,self.im_left,linesRight,ptsRight,ptsLeft)
        
        plt.figure()
        
        plt.subplot(1,2,1)
        plt.imshow(im_lines_left, cmap='gray')
        plt.title("Izquierda")
        
        plt.subplot(1,2,2)
        plt.imshow(im_lines_right, cmap='gray')
        plt.title("Derecha")
        
        plt.show()
    
    @staticmethod
    def drawLines(im_left, im_right, lines, pts_left, pts_right):
        r,c = im_left.shape
        
        im_left = cv.cvtColor(im_left, cv.COLOR_GRAY2BGR)
        im_right = cv.cvtColor(im_right, cv.COLOR_GRAY2BGR)
        
        for r,pt1,pt2 in zip(lines,pts_left,pts_right):
            color = tuple(np.random.randint(0,255,3).tolist())
            
            x0,y0 = map(int,[0,-r[2]/r[1]])
            x1,y1 = map(int,[c,-(r[2]+r[0]*c)/r[1]])
            
            im_left = cv.line(im_left, (x0, y0), (x1, y1), color, 1)
            im_left = cv.circle(im_left, tuple(pt1), 5, color, -1)
            im_right = cv.circle(im_right, tuple(pt2), 5, color, -1)
            
        return im_left, im_right
    
    
def demoViewPics():
    eg = EpipolarGeometry(showImages=True)
    
def demoDrawEpilines():
    eg = EpipolarGeometry(showImages=False)
    
    eg.dibujar_lineas_epipolar()
    
    
if __name__ == '__main__':
    #demoViewPics()
    
    demoDrawEpilines()
    