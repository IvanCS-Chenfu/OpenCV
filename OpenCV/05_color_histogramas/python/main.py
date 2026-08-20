import cv2
img=cv2.imread("input.jpg"); assert img is not None
hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV); gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY); eq=cv2.equalizeHist(gray); clahe=cv2.createCLAHE(2.0,(8,8)).apply(gray)
cv2.imwrite("output_hsv_h.png",hsv[:,:,0]); cv2.imwrite("output_equalized.png",eq); cv2.imwrite("output_clahe.png",clahe)
