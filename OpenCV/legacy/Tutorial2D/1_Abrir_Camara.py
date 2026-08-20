# Librería
import cv2

# Iniciar la cámara
cap = cv2.VideoCapture("http://172.20.10.13:8080/video")       # 0 indica la cámara predeterminada del sistema (se puede cambiar por otro número si tienes más cámaras)

# Verificar si la Ccmara se abrió
if not cap.isOpened():
    print("NO SE ABRIÓ LA CÁMARA")
    exit()
    
# Bucle infinito para mostrar los fotogramas
while True:
    ret, frame = cap.read()     # "ret" es un booleano que dice si la lectura fue existos. "frame" es el fotograma actual.
    
    # Verificar si se ha podido leer.
    if not ret:
        print("Error de Lectura")
        break
    
    # Mostrar el fotograma
    cv2.imshow("Camara", frame)     # Se habre una pestaña llamada "Camara" en la cual se muestra el fotograma
    
    # Salir del bucle pulsando una tecla
    if cv2.waitKey(1) == ord("q"):      # Se espera un "ms" para ver y devuelve el codigo ASCII de la tecla pulsada. Esto se compara con el codigo ASCII de la tecla "q" 
        break
    
    
# Liberar los recursos y cerrar las ventanas
cap.release()
cv2.destroyAllWindows()

