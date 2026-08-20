import cv2, numpy as np
g=cv2.imread("input.jpg",cv2.IMREAD_GRAYSCALE); assert g is not None
e=cv2.Canny(g,80,160); lines=cv2.HoughLinesP(e,1,np.pi/180,80,minLineLength=50,maxLineGap=10); print("lineas",0 if lines is None else len(lines))
