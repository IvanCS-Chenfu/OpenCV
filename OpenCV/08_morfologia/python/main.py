import cv2
img=cv2.imread("binary.png",cv2.IMREAD_GRAYSCALE); assert img is not None
k=cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(5,5)); opening=cv2.morphologyEx(img,cv2.MORPH_OPEN,k); closing=cv2.morphologyEx(img,cv2.MORPH_CLOSE,k); grad=cv2.morphologyEx(img,cv2.MORPH_GRADIENT,k)
cv2.imwrite("opening.png",opening); cv2.imwrite("closing.png",closing); cv2.imwrite("gradient.png",grad)
