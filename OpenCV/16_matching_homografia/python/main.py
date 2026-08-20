import cv2, numpy as np
a=cv2.imread("image1.jpg",0); b=cv2.imread("image2.jpg",0); assert a is not None and b is not None
orb=cv2.ORB_create(2000); k1,d1=orb.detectAndCompute(a,None); k2,d2=orb.detectAndCompute(b,None); m=cv2.BFMatcher(cv2.NORM_HAMMING).knnMatch(d1,d2,k=2); good=[x for x,y in m if x.distance<0.75*y.distance]; print("matches",len(good))
if len(good)>=4:
 p1=np.float32([k1[x.queryIdx].pt for x in good]); p2=np.float32([k2[x.trainIdx].pt for x in good]); H,mask=cv2.findHomography(p1,p2,cv2.RANSAC,3.0); print("inliers",int(mask.sum()),"H=\n",H)
