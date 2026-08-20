# Librería
import cv2
import numpy as np

# Iniciar la cámara
cap = cv2.VideoCapture(0)       # 0 indica la cámara predeterminada del sistema (se puede cambiar por otro número si tienes más cámaras)

# Verificar si la Ccmara se abrió
if not cap.isOpened():
    print("NO SE ABRIÓ LA CÁMARA")
    exit()

# Umbrales de color. En HSV: H va de 0 a 179 ; S va de 0 a 255 ; V va de 0 a 255
umbR_abajo1 = np.array([0,100,20],np.uint8)
umbR_abajo2 = np.array([8,255,255],np.uint8)

umbR_arriba1 = np.array([175,100,20],np.uint8)
umbR_arriba2 = np.array([179,255,255],np.uint8)

# Bucle infinito para mostrar los fotogramas
while True:
    ret, frame = cap.read()     # "ret" es un booleano que dice si la lectura fue existos. "frame" es el fotograma actual.
    
    # Verificar si se ha podido leer.
    if not ret:
        print("Error de Lectura")
        break
    
    # Aplicamos las máscaras en HSV (solo queremos lo rojo)
    frameHSV=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    maskR_abajo=cv2.inRange(frameHSV,umbR_abajo1,umbR_abajo2)   # Da un 1 en los pixeles que el se encuentren entre los umbrales
    maskR_arriba=cv2.inRange(frameHSV,umbR_arriba1,umbR_arriba2)
    maskR = cv2.add(maskR_abajo,maskR_arriba)       # Se aplican ambas máscaras
    mask_aplicada = cv2.bitwise_and(frame, frame, mask= maskR)
    
    # Mostrar el fotograma
    cv2.imshow("Camara", frame)     # Se habre una pestaña llamada "Camara" en la cual se muestra el fotograma
    cv2.imshow("MascaraRed",maskR)
    cv2.imshow("MascaraAplicada",mask_aplicada)
    
    # Salir del bucle pulsando una tecla
    if cv2.waitKey(1) == ord("q"):      # Se espera un "ms" para ver y devuelve el codigo ASCII de la tecla pulsada. Esto se compara con el codigo ASCII de la tecla "q" 
        break
    
    
# Liberar los recursos y cerrar las ventanas
cap.release()
cv2.destroyAllWindows()