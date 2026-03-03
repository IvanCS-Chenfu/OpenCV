import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

    
class DepthMap:
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

    def mapa_BM(self):
        nDispFactor = 26     # parámetro a ajustar
        blockSize = 21
        objeto_estereo = cv.StereoBM_create(numDisparities=16*nDispFactor, blockSize=blockSize)
        
        disparidad = objeto_estereo.compute(self.im_left, self.im_right)
        
        plt.figure()
            
        plt.imshow(disparidad, cmap='gray')
        plt.colorbar()
        plt.title("Disparidad")
        
        plt.show()
        
    def mapa_SGBM(self):
        window_size = 7
        min_disp = 16
        nDispFactor = 20        # parámetro a ajustar
        canales = 1             # Es gris
        objeto_estereo = cv.StereoSGBM_create(minDisparity=min_disp,
                                                numDisparities=16*nDispFactor,
                                                blockSize=window_size,
                                                P1 = 8*canales*window_size**2,      # Fórmula OpenCV
                                                P2 = 32*canales*window_size**2,     # Fórmula OpenCV
                                                disp12MaxDiff=1,
                                                uniquenessRatio=15,
                                                speckleWindowSize=100,
                                                speckleRange=2,
                                                preFilterCap=63,
                                                mode = cv.STEREO_SGBM_MODE_SGBM_3WAY)
        
        disparidad = objeto_estereo.compute(self.im_left, self.im_right).astype(np.float32)/16.0
        
        plt.figure()
            
        plt.imshow(disparidad, cmap='gray')
        plt.colorbar()
        plt.title("Disparidad")
        
        plt.show()
    
def demoViewPics():
    dp = DepthMap(showImages=True)
    
def demoStereoBM():
    dp = DepthMap(showImages=False)
    
    dp.mapa_BM()
    
def demoStereoSGBM():
    dp = DepthMap(showImages=False)
    
    dp.mapa_SGBM()
    
    
if __name__ == '__main__':
    #demoViewPics()
    
    #demoStereoBM()
    
    demoStereoSGBM()