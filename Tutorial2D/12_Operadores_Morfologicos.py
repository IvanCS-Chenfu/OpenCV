import cv2
import numpy as np

imG = cv2.imread('Gente.png', 0)
_,im_bin = cv2.threshold(imG,127,255,cv2.THRESH_BINARY)
cv2.imshow("Normal", im_bin)


cruz = cv2.getStructuringElement(cv2.MORPH_CROSS,(5,5))
print(cruz)
elipse = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(5,5))
print(elipse)
rectangulo = cv2.getStructuringElement(cv2.MORPH_RECT,(5,5))
print(rectangulo)

erosion_cruz = cv2.erode(im_bin,cruz)
erosion_elipse = cv2.erode(im_bin,elipse)
erosion_rectangulo = cv2.erode(im_bin,rectangulo)

cv2.imshow("Erosion", np.hstack([erosion_cruz,erosion_elipse,erosion_rectangulo]))

dilatacion_cruz = cv2.dilate(im_bin,cruz)
dilatacion_elipse = cv2.dilate(im_bin,elipse)
dilatacion_rectangulo = cv2.dilate(im_bin,rectangulo)

cv2.imshow("Diilatacion", np.hstack([dilatacion_cruz,dilatacion_elipse,dilatacion_rectangulo]))

cierre_cruz = cv2.morphologyEx(im_bin, cv2.MORPH_CLOSE, cruz)
cierre_elipse = cv2.morphologyEx(im_bin, cv2.MORPH_CLOSE, elipse)
cierre_rectangulo = cv2.morphologyEx(im_bin, cv2.MORPH_CLOSE, rectangulo)

cv2.imshow("Cierre", np.hstack([cierre_cruz,cierre_elipse,cierre_rectangulo]))

apertura_cruz = cv2.morphologyEx(im_bin, cv2.MORPH_OPEN, cruz)
apertura_elipse = cv2.morphologyEx(im_bin, cv2.MORPH_OPEN, elipse)
apertura_rectangulo = cv2.morphologyEx(im_bin, cv2.MORPH_OPEN, rectangulo)

cv2.imshow("Apertura", np.hstack([apertura_cruz,apertura_elipse,apertura_rectangulo]))


cv2.waitKey(0)
cv2.destroyAllWindows()

