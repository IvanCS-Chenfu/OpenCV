import cv2
b=cv2.imread("binary.png",cv2.IMREAD_GRAYSCALE); assert b is not None
contours,_=cv2.findContours(b,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE); print("contornos",len(contours));
for i,c in enumerate(contours[:10]): print(i,"area",cv2.contourArea(c),"perimetro",cv2.arcLength(c,True),"M00",cv2.moments(c)["m00"])
