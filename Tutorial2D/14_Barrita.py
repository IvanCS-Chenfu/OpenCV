import cv2

# No hace nada
def nothing(x):
    pass

image = cv2.imread('Gente.png')
faceClassif = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

cv2.namedWindow('Imagen')       # Nombre de la ventana a la que queremos ponerle la Barra
cv2.createTrackbar('Blur','Imagen',0,15,nothing)    # Crea una barra con un nombre. Parámetros: El nombre de la ventana, los valores que puede tomar y una función callback.
cv2.createTrackbar('Gray','Imagen',0,1,nothing)

while True:

    val = cv2.getTrackbarPos('Blur','Imagen')   # Obtiene el valor de la barra
    grayVal = cv2.getTrackbarPos('Gray','Imagen')
    if grayVal == 1:
        imageN = cv2.cvtColor(image.copy(), cv2.COLOR_BGR2GRAY) # Se pone ".copy()" para que la imagen de entrada no se modifique.
    else: imageN = image.copy()
    faces = faceClassif.detectMultiScale(image, 1.1, 5)

    for (x,y,w,h) in faces:
        if val > 0:
            imageN[y:y+h,x:x+w] = cv2.blur(imageN[y:y+h,x:x+w],(val,val))

    cv2.imshow('Imagen',imageN)
    
    if cv2.waitKey(1) == ord("q"):
        break
    
cv2.destroyAllWindows()