# Librerías
import cv2
import numpy as np


## PRIMERO


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
cv2.imshow("Contorno", bgr)     
cv2.imshow("MascaraRed",maskB)

cv2.waitKey(0)
cv2.destroyAllWindows()


## SEGUNDO


im = cv2.imread("RGB.png")

im_gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)

im_canny = cv2.Canny(im_gray, 0, 100)   # Da una imagen binarizada en la que solo se encuentran bordes.

contornos,_ = cv2.findContours(im_canny, cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE) # Obtiene los contornos de la imagen binarizada

cv2.drawContours(im, contornos, -1 ,(255,255,255), 3)

cv2.imshow("Canny", im_canny)    
cv2.imshow("Contorno", im)    

cv2.waitKey(0)
cv2.destroyAllWindows()




## TERCERO



cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read() 
    
    if not ret:
        print("Error de Lectura")
        break
    
    # Aplicamos las máscaras en HSV (solo queremos lo azul)
    frame_hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    frame_maskB=cv2.inRange(frame_hsv,umbB_abajo,umbB_arriba)   # Da un 1 en los pixeles que el se encuentren entre los umbra[les

    contornos,_ = cv2.findContours(frame_maskB, cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    
    for c in contornos:
        area = cv2.contourArea(c)
        if area > 6000:
            M = cv2.moments(c)
            
            if (M["m00"]==0): M["m00"] = 1      # Para no dividir entre 0
            x = int(M["m10"]/M["m00"])          # Coordenada X del centro del contorno.
            y = int(M["m01"]/M["m00"])          # Coordenada Y del centro del contorno
            
            cv2.putText(frame,'{},{}'.format(x,y),(x+10,y), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 255, 255), 2)
            
            nuevo_c = cv2.convexHull(c)         # Crea en cerco convexo de un contorno.
            cv2.drawContours(frame, [nuevo_c], 0 ,(255,255,255), 3)   # Dibuja solo los contornos que tengan un área mayor a 6000

    cv2.imshow("Camara", frame)
    
    if cv2.waitKey(1) == ord("q"):
        break
    
    
cap.release()
cv2.destroyAllWindows()




## CUARTO


cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("NO SE ABRIÓ LA CÁMARA")
    exit()
    
i = 0

while True:
    ret, frame = cap.read()
    if not ret:
        print("Error de Lectura")
        break
    
    frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    if i == 20:
        inicio = frame_gray
        
    if i > 20:
        dif = cv2.absdiff(frame_gray, inicio)           # Obtengo la imagen inicial y la comparo continuaente con las nuevas
        _,binarizada=cv2.threshold(dif,10,255,cv2.THRESH_BINARY) 
        binarizada = cv2.medianBlur(binarizada,13)
        
        contornos,_ = cv2.findContours(binarizada, cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
        
        for c in contornos:
            area = cv2.contourArea(c)
            if area > 6000:
                cv2.drawContours(frame_gray, [c], 0 ,(255,255,255), 3)
                
                cv2.imshow("Camara", np.hstack([dif,binarizada,frame_gray]))
        

    if cv2.waitKey(1) == ord("q"):
        break
    
    i = i+1

cap.release()
cv2.destroyAllWindows()