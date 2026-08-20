import cv2
g=cv2.imread("input.jpg",cv2.IMREAD_GRAYSCALE); assert g is not None
orb=cv2.ORB_create(nfeatures=1000,scaleFactor=1.2,nlevels=8); kp,des=orb.detectAndCompute(g,None); out=cv2.drawKeypoints(g,kp,None); print(len(kp),des.shape if des is not None else None); cv2.imwrite("output_orb.png",out)
