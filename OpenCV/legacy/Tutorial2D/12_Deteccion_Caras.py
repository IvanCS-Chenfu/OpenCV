import cv2
import numpy as np

# https://github.com/opencv/opencv/tree/master/data/haarcascades


faceClassif = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")      # El xml que nos ayudará a clasificar lo que queramos.

im = cv2.imread("Gente.png")
im_gray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)

faces = faceClassif.detectMultiScale(im_gray, scaleFactor=1.1, minNeighbors=5, minSize=(30,30), maxSize=(200,200))
# ScaleFator hace que detecte más o menos caras
# Un filtro va buscando rostros. Si encuentra uno lo dice. Para que sea verdadero, mínimo 5 rostros encontrados deben tocarse.

for (x,y,w,h) in faces:
    cv2.rectangle(im,(x,y),(x+w,y+h),(0,255,0),2)
    
    
cv2.imshow("Imagen", im)


cv2.waitKey(0)
cv2.destroyAllWindows()