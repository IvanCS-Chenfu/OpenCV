import cv2
img=cv2.imread("input.jpg",cv2.IMREAD_GRAYSCALE); assert img is not None
gx=cv2.Sobel(img,cv2.CV_32F,1,0,ksize=3); gy=cv2.Sobel(img,cv2.CV_32F,0,1,ksize=3); canny=cv2.Canny(img,80,160)
cv2.imwrite("output_canny.png",canny)
