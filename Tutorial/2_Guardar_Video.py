# Librería
import cv2

# Variable que guarda el Video
Video = "AWEONAO.mp4"     # Nombre
fourcc = cv2.VideoWriter_fourcc(*"mp4v")    # Poner en formato "mp4"
fps = 30        # FPS a los que queremos que se guarde el video.

# Iniciar la cámara
cap = cv2.VideoCapture(0)       # 0 indica la cámara predeterminada del sistema (se puede cambiar por otro número si tienes más cámaras). Si pones el nombre de un video, muestra el video.

# Obtenemos el Ancho y el Alto del video.
frame_width = int(cap.get(3))
frame_height = int(cap.get(4))

# Guardamos el Video
out = cv2.VideoWriter(Video, fourcc, fps, (frame_width, frame_height))

# Bucle infinito para mostrar los fotogramas
while True:
    ret, frame = cap.read()     # "ret" es un booleano que dice si la lectura fue existos. "frame" es el fotograma actual.
    
    # Verificar si se ha podido leer.
    if not ret:
        print("Error de Lectura")
        break
    
    # Escribir cada fotograma en el archivo de video (ir añadiendo fotogramas).
    out.write(frame)
    
    # Mostrar el fotograma
    cv2.imshow("Camara", frame)     # Se habre una pestaña llamada "Camara" en la cual se muestra el fotograma
    
    # Salir del bucle pulsando una tecla
    if cv2.waitKey(1) == ord("q"):      # Se espera un "ms" para ver y devuelve el codigo ASCII de la tecla pulsada. Esto se compara con el codigo ASCII de la tecla "q" 
        break
    
    
# Liberar los recursos y cerrar las ventanas
cap.release()
out.release()
cv2.destroyAllWindows()