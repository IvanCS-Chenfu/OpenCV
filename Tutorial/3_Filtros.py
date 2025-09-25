# Librería
import cv2

# Obtener Imagen
im = cv2.imread("Gato.png")

# RGB to Gray
im_gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)

# Filtro de Desenfoque TIPO:Gaussiano
im_blur = cv2.GaussianBlur(im, (15,15), 0)      # El tamaño de la malla (15 x 15) y el sigma (0) de la gaussiana

# Filtro de Desenfoque TIPO:Canny (bordes de una imagen en blanco y negro)
im_canny = cv2.Canny(im_gray, 100, 200)  

# Mostrar las imágenes
cv2.imshow("Normal", im)
cv2.imshow("Gris", im_gray)
cv2.imshow("Gauss", im_blur)
cv2.imshow("Canny", im_canny)

# Esperamos hasta que el usuario presione una tecla y cerramos las ventanas.
cv2.waitKey(0)
cv2.destroyAllWindows()