import cv2
import numpy as np

im1 = cv2.imread("Gato.png")
im2 = cv2.imread("Nuevo_Gato.png")

add = cv2.add(im1,im2)      # Suma ambas. Si se pasa de 255, se queda en 255.
add_weight = cv2.addWeighted(im1,0.5,im2,0.5,0)        # Cada imagen la multiplica por el numero de su derecha (0.5 / 0.9) y le suma el último número (0)
sub = cv2.subtract(im1,im2)     # Resta ambas. Si se pasa de 0, se queda en 0.
absdif = cv2.absdiff(im1,im2)   # Resta ambas y le realiza el absoluto.

cv2.imshow("Add", np.hstack([im1,im2,add]))
cv2.imshow("Add_Weight", np.hstack([im1,im2,add_weight]))
cv2.imshow("Substract", np.hstack([im1,im2,sub]))
cv2.imshow("Absdiff", np.hstack([im1,im2,absdif]))

cv2.waitKey(0)
cv2.destroyAllWindows()