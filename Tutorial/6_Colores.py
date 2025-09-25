# Librerías
import cv2
import numpy as np



# Crear una matriz Negra
negro = np.zeros((300,300,3),dtype = np.uint8)
cv2.imshow("Negro1", negro)

# Obtener los valores separados de R, G y B
bgr = cv2.imread("RGB.png")

B1 = bgr[:,:,0]
G1 = bgr[:,:,1]
R1 = bgr[:,:,2]

cv2.imshow("BGR", bgr)
cv2.imshow("BGR1", np.hstack([B1,G1,R1]))    # Concatenar fotos en horizontal

# Cambiar de BGR a RGB
rgb = cv2.cvtColor(bgr, cv2.COLOR_BGR2RGB)

R2 = bgr[:,:,0]
G2 = bgr[:,:,1]
B2 = bgr[:,:,2]

cv2.imshow("RGB", np.hstack([R2,G2,B2]))    # Concatenar fotos en horizontal

# Cambiar a Escala de Grises
gray = cv2.cvtColor(bgr, cv2.COLOR_BGR2GRAY)

cv2.imshow("GRAY", gray)

# Cambiar a HSV
hsv = cv2.cvtColor(bgr, cv2.COLOR_BGR2HSV)

cv2.imshow("HSV", hsv)

# Esperamos hasta que el usuario presione una tecla y cerramos las ventanas.
cv2.waitKey(0)
cv2.destroyAllWindows()