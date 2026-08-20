# Librerías
import cv2
import numpy as np


# Crear la Matriz de tonos de grises
grises = np.zeros((500,600),dtype = np.uint8)
grises[100:300,:200] = 130
grises[100:300,200:400] = 20
grises[100:300,400:600] = 210
grises[300:600,:200] = 35
grises[300:600,200:400] = 255
grises[300:600,400:600] = 70

# Umbralización
umbral = 130
_,binarizada=cv2.threshold(grises,umbral,255,cv2.THRESH_BINARY)     # 255 es el color en el cual se muestran los pixeles que superen el umbral.
_,binarizada_inv=cv2.threshold(grises,umbral,255,cv2.THRESH_BINARY_INV)
_,truncada=cv2.threshold(grises,umbral,255,cv2.THRESH_TRUNC)        # Pone los pixeles que superan el umbral al color del umbral. Los demás los dejan igual.
_,toz=cv2.threshold(grises,umbral,255,cv2.THRESH_TOZERO)            # Pone a 0 los valores que no superan el umbral. Los demás los dejan igual.
_,toz_inv=cv2.threshold(grises,umbral,255,cv2.THRESH_TOZERO_INV)    # Pone a 0 los valores que superan el umbral. Los demás lo dejan igual.


# Mostrar Imagenes
cv2.imshow("GRISES", grises)
cv2.imshow("BINARIZADA", binarizada)
cv2.imshow("BINARIZADA_INV", binarizada_inv)
cv2.imshow("TRUNCADA", truncada)
cv2.imshow("TOZERO", toz)
cv2.imshow("TOZERO_INV", toz_inv)


# Esperamos hasta que el usuario presione una tecla y cerramos las ventanas.
cv2.waitKey(0)
cv2.destroyAllWindows()