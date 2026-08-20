import cv2
import numpy as np
import matplotlib.pyplot as plt

imG = cv2.imread('Gente.png', 0)

LUT_igual = np.arange(256).astype(np.uint8)
LUT_inv = (255 - np.arange(256)).astype(np.uint8)

umbral = 127
LUT_umbral = np.zeros(256,dtype=np.uint8)
LUT_umbral[umbral:] = 255


im_igual = cv2.LUT(imG, LUT_igual)
im_inv = cv2.LUT(imG, LUT_inv)
im_umbral = cv2.LUT(imG, LUT_umbral)


cv2.imshow("LUTS", np.hstack([im_igual,im_inv,im_umbral]))


cv2.waitKey(0)
cv2.destroyAllWindows()