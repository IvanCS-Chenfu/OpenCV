import cv2, numpy as np
p1=np.loadtxt("points1.txt",dtype=np.float32); p2=np.loadtxt("points2.txt",dtype=np.float32); F,mask=cv2.findFundamentalMat(p1,p2,cv2.FM_RANSAC,1.0,0.999); print("F=\n",F,"\ninliers",int(mask.sum()))
