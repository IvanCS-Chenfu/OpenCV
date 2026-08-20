import cv2
img=cv2.imread("input.jpg"); assert img is not None
gauss=cv2.GaussianBlur(img,(7,7),1.5); median=cv2.medianBlur(img,7); bilateral=cv2.bilateralFilter(img,9,75,75)
cv2.imwrite("output_gaussian.png",gauss); cv2.imwrite("output_median.png",median); cv2.imwrite("output_bilateral.png",bilateral)
