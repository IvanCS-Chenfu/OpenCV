import cv2
import numpy as np
import matplotlib.pyplot as plt

## FILTROS

imG = cv2.imread('Ruidos.png', 0)
cv2.imshow("Normal",imG)

fil1 = np.array([[1,1,1],[1,1,1],[1,1,1]])
fil2 = np.array([[1,1,1],[1,2,1],[1,1,1]])
fil3 = np.array([[1,2,1],[2,4,2],[1,2,1]])

fil1 = fil1/np.sum(fil1)
fil2 = fil2/np.sum(fil2)
fil3 = fil3/np.sum(fil3)

im1 = cv2.filter2D(imG,-1,fil1)     # -1 indica que es toda la imagen. Podemos elegir una región concreta.
im2 = cv2.filter2D(imG,-1,fil2)
im3 = cv2.filter2D(imG,-1,fil3)

cv2.imshow("Filtro Pasa Bajo", np.hstack([im1,im2,im3]))


fil1 = np.array([[0,-1,0],[-1,5,-1],[0,-1,0]])
fil2 = np.array([[-1,-1,-1],[-1,9,-1],[-1,-1,-1]])
fil3 = np.array([[1,-2,1],[-2,5,-2],[1,-2,1]])

fil1 = fil1/np.sum(fil1)
fil2 = fil2/np.sum(fil2)
fil3 = fil3/np.sum(fil3)

im1 = cv2.filter2D(imG,-1,fil1)  
im2 = cv2.filter2D(imG,-1,fil2)
im3 = cv2.filter2D(imG,-1,fil3)

cv2.imshow("Filtro Pasa Alto", np.hstack([im1,im2,im3]))


## Suavizados

Media = np.array([[1,1,1],[1,1,1],[1,1,1]])
Media = Media/np.sum(Media)

im_Media = cv2.filter2D(imG,-1,Media)  
im_Mediana = cv2.medianBlur(imG,7)     # El 7 es de que la matriz en 7x7

cv2.imshow("Suavizado", np.hstack([im_Media,im_Mediana]))

cv2.waitKey(0)
cv2.destroyAllWindows()