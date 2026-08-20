import cv2, glob, numpy as np
PATTERN=(9,6); square=0.024
obj=np.zeros((PATTERN[0]*PATTERN[1],3),np.float32); obj[:,:2]=np.mgrid[0:PATTERN[0],0:PATTERN[1]].T.reshape(-1,2)*square
objpoints=[]; imgpoints=[]; size=None
for f in glob.glob("data/calibration/*.png"):
    im=cv2.imread(f); gray=cv2.cvtColor(im,cv2.COLOR_BGR2GRAY); size=gray.shape[::-1]
    ok,corners=cv2.findChessboardCorners(gray,PATTERN)
    if ok: objpoints.append(obj); imgpoints.append(cv2.cornerSubPix(gray,corners,(11,11),(-1,-1),(cv2.TERM_CRITERIA_EPS+cv2.TERM_CRITERIA_MAX_ITER,30,1e-3)))
if not objpoints: raise RuntimeError("Añade imágenes de tablero en data/calibration")
rms,K,dist,_,_=cv2.calibrateCamera(objpoints,imgpoints,size,None,None)
print("RMS",rms,"\nK=\n",K,"\ndist=",dist.ravel())
