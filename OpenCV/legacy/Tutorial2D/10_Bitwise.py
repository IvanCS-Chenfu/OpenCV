import cv2
import numpy as np

im1 = np.zeros((400,600),dtype=np.uint8)
im1[100:300,200:400] = 255

im2 = np.zeros((400,600),dtype=np.uint8)
im2 = cv2.circle(im2,(300,200),125,(255),-1)

AND = cv2.bitwise_and(im1,im2)  # Operación AND
OR = cv2.bitwise_or(im1,im2)    # Operación OR
NOT1 = cv2.bitwise_not(im1)     # Operación NOT
NOT2 = cv2.bitwise_not(im2)
XOR = cv2.bitwise_xor(im1,im2)  # Operación XOR

cv2.imshow("Add", np.hstack([im1,im2,AND]))
cv2.imshow("Or", np.hstack([im1,im2,OR]))
cv2.imshow("Not", np.hstack([im1,NOT1,im2,NOT2]))
cv2.imshow("Xor", np.hstack([im1,im2,XOR]))

cv2.waitKey(0)
cv2.destroyAllWindows()