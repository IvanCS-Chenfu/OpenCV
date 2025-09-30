import cv2
import numpy as np
import imutils

im = cv2.imread("Gato.png")

ancho = im.shape[1]
alto = im.shape[0]
print(im.shape)

T_tras = np.float32([[1,0,-180],[0,1,100]])     # Crea una matriz de Transformación con una traslación.
T_rot = cv2.getRotationMatrix2D((ancho//2,alto//2),15,1)       # Crea una matriz de Transformación con una rotación. (Centro de la rotación, ángulo y escala).

im_tras = cv2.warpAffine(im,T_tras,(ancho,alto))    # Aplica a la imagen una matriz de Transformación y deja igual el alto y el ancho de la ventana.
im_rot = cv2.warpAffine(im,T_rot,(ancho,alto)) 
im_resize = cv2.resize(im,(600,100),interpolation=cv2.INTER_CUBIC)  # Escala la imagen.
im_altura = imutils.resize(im, height=50)
im_ancho = imutils.resize(im, width = 500)
im_recorte = im[150:300,200:400]        # Recorta la imagen
im_flip_h = cv2.flip(im, 0)         # Espejo Horizontal
im_flip_v = cv2.flip(im, 1)         # Espejo Vertical
im_flip_hv = cv2.flip(im, -1)       # Espejo Horizontal y Vertical

cv2.imshow("Traslacion", np.hstack([im,im_tras]))
cv2.imshow("Rotacion", np.hstack([im,im_rot]))
cv2.imshow("Escala1", im_resize)
cv2.imshow("Escala2", im_altura)
cv2.imshow("Escala3", im_ancho)
cv2.imshow("Recorte", im_recorte)
cv2.imshow("Rotacion", np.hstack([im,im_flip_h,im_flip_v,im_flip_hv]))


cv2.waitKey(0)
cv2.destroyAllWindows()