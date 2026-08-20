import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np


def seguidor_objetos(option):
    
    objeto_video = cv.VideoCapture("Video_Movil.mp4")
    _, frame = objeto_video.read()
    frame_hsv = cv.cvtColor(frame,cv.COLOR_BGR2HSV)
    
    x0 = 433
    y0 = 296
    x1 = 520
    y1 = 460
    
    im_region = frame[y0:y1, x0:x1]
    tam_region = (x0, y0, x1-x0, y1-y0)
    
    im_region_hsv = cv.cvtColor(im_region,cv.COLOR_BGR2HSV)
    
    limit1 = np.array([110, 20, 40])
    limit2 = np.array([180, 130, 160])
    marcara_region = cv.inRange(im_region_hsv, limit1, limit2)
    marcara_total = cv.inRange(frame_hsv, limit1, limit2)
    
    hist_region = cv.calcHist([im_region_hsv],[0],marcara_region,[180],[0,180])
    cv.normalize(hist_region,hist_region,0,255,cv.NORM_MINMAX)
    
    plt.figure()
    
    plt.subplot(2,4,1)
    plt.imshow(frame)
    plt.title("Foto")
    
    plt.subplot(2,4,2)
    plt.imshow(frame_hsv)
    plt.title("Foto (HSV)")
    
    plt.subplot(2,4,5)
    plt.imshow(im_region)
    plt.title("Region")
    
    plt.subplot(2,4,6)
    plt.imshow(im_region_hsv)
    plt.title("Region (HSV)")
    
    plt.subplot(2,4,3)
    plt.imshow(marcara_total)
    plt.title("Máscara Total")
    
    plt.subplot(2,4,7)
    plt.imshow(marcara_region)
    plt.title("Máscara Region")
    
    plt.subplot(2,4,8)
    plt.plot(hist_region)
    plt.title("Histograma Region (máscara)")
    
    plt.show()
    
    
    criterio_terminacion = (cv.TERM_CRITERIA_EPS | cv.TERM_CRITERIA_COUNT, 10,1)    # Cuando detener la iteracion
    color_recuadro = (0,255,0)
    
    
    while True:
        ret, videoFrame = objeto_video.read()
        
        if ret == True:
            videoFrame_hsv = cv.cvtColor(videoFrame,cv.COLOR_BGR2HSV)
            backproj = cv.calcBackProject([videoFrame_hsv], [0], hist_region, [0,180], 1)
            
            # Para mostrarlo
            marcara_video = cv.inRange(videoFrame_hsv, limit1, limit2)
            marcara_video = cv.merge((marcara_video,marcara_video,marcara_video))
            
        if option == 'meanshift':
            _, tam_region = cv.meanShift(backproj,tam_region,criterio_terminacion)
            xTopLeft, yTopLeft, w, h = tam_region
            
            # Para mostrarlo
            videoFrame = cv.rectangle(videoFrame,(xTopLeft,yTopLeft),(xTopLeft+w, yTopLeft+h),color_recuadro,2)
            marcara_video = cv.rectangle(marcara_video,(xTopLeft,yTopLeft),(xTopLeft+w, yTopLeft+h),color_recuadro,2)
            
        if option == 'camshift':
            ret, tam_region = cv.CamShift(backproj,tam_region,criterio_terminacion)
            boxPts = cv.boxPoints(ret)
            
            # Para mostrarlo
            videoFrame = cv.polylines(videoFrame,[np.int32(boxPts)],True,color_recuadro,2)
            marcara_video = cv.polylines(marcara_video,[np.int32(boxPts)],True,color_recuadro,2)
            
            
        cv.imshow("video",videoFrame)
        
        cv.imshow("video (mascara HSV)", marcara_video)
        cv.waitKey(15)
    

def lucasKanade():
    
    objeto_video = cv.VideoCapture("Video_Movil.mp4")
    
    shiTomasCornerParams = dict(maxCorners=20, qualityLevel=0.3, minDistance=50, blockSize=7)
    lucasKanadeParams = dict(winSize=(15,15), maxLevel=2, criteria=(cv.TERM_CRITERIA_EPS | cv.TERM_CRITERIA_COUNT, 10, 0.03))
    ramdomColors = np.random.randint(0,255,(100,3))
    
    _, frame = objeto_video.read()
    frame_gray_Previo = cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
    
    corners_Previo = cv.goodFeaturesToTrack(frame_gray_Previo, mask=None, **shiTomasCornerParams)
    mask = np.zeros_like(frame)
    
    while True:
        ret, videoFrame = objeto_video.read()
        
        if ret == True:
            frame_gray_Actual = cv.cvtColor(videoFrame,cv.COLOR_BGR2GRAY)
            corners_Actual, foundStatus, _ = cv.calcOpticalFlowPyrLK(frame_gray_Previo, frame_gray_Actual, corners_Previo, None, **lucasKanadeParams)
            
        if corners_Actual is not None:
            cornersMatched_Actual = corners_Actual[foundStatus==1]
            cornersMatched_Previo = corners_Previo[foundStatus==1]
            
        for i, (corners_Actual, corners_Previo) in enumerate(zip(cornersMatched_Actual, cornersMatched_Previo)):
            x_Actual, y_Actual = corners_Actual.ravel()
            x_Previo, y_Previo = corners_Previo.ravel()
            
            p_Actual = (int(x_Actual), int(y_Actual))
            p_Previo = (int(x_Previo), int(y_Previo))
            
            mask = cv.line(mask, p_Actual, p_Previo, ramdomColors[i].tolist(),2)
            videoFrame = cv.circle(videoFrame, p_Actual, 5, ramdomColors[i].tolist(),2)
            
            im = cv.add(videoFrame,mask)
            
            
        cv.imshow("video",im)
        cv.waitKey(15)
        
        frame_gray_Previo = frame_gray_Actual.copy()
        corners_Previo = cornersMatched_Actual.reshape(-1,1,2)
        




if __name__ == '__main__':
    
    option = "meanshift"
    option = "camshift"
    #seguidor_objetos(option)
    
    lucasKanade()
    
    
    