import cv2, numpy as np
K=np.array([[700.,0,320],[0,700,240],[0,0,1]])
rvec=np.array([0.05,-0.1,0.02]); tvec=np.array([0.,0.,4.])
pts=np.float32([[-1,-1,0],[1,-1,0],[1,1,0],[-1,1,0],[0,0,1]])
uv,_=cv2.projectPoints(pts,rvec,tvec,K,None)
print(uv.reshape(-1,2))
