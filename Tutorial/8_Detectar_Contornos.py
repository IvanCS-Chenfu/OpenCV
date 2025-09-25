# Librerías
import cv2
import numpy as np


umbB_abajo = np.array([100,100,20],np.uint8)
umbB_arriba = np.array([125,255,255],np.uint8)

bgr = cv2.imread("RGB.png")

# Aplicamos las máscaras en HSV (solo queremos lo azul)
hsv=cv2.cvtColor(bgr,cv2.COLOR_BGR2HSV)
maskB=cv2.inRange(hsv,umbB_abajo,umbB_arriba)   # Da un 1 en los pixeles que el se encuentren entre los umbrales

# Obtenemos los contornos de la mascara
contornos,_ = cv2.findContours(maskB, cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(bgr,contornos, -1 ,(255,255,255), 3)   # Se dibujan todos (-1) los contornos en la imagen (bgr) de color blanco (255*3 y de 3 de grosor

# Mostrar imagenes
cv2.imshow("Camara", bgr)     
cv2.imshow("MascaraRed",maskB)

cv2.waitKey(0)
cv2.destroyAllWindows()