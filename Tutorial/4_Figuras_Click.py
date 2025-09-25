# Librería
import cv2

# Obtener Imagen
im = cv2.imread("Gato.png")

# Dibujar Linea
cv2.line(im,(300, 60),(200,60), (0, 0, 255), 2)    # Pinto una línea del color BGR (0,0,255) y de grosor (2) que va desde el punto P1 al P2.

# Dibujar Rectángulo
cv2.rectangle(im,(500, 60),(700,500), (0, 255, 0), 5)    # Los puntos son: las esquinas del rectángulo

# Dibujar Círculo
cv2.circle(im,(300, 700), 100, (255, 0, 0), 10)    # Los parámetros son: el centro del círculo y el radioç

# Escribir Texto
cv2.putText(im,"GATETE", (500, 800), cv2.FONT_HERSHEY_SCRIPT_COMPLEX, 2, (0, 255, 255), 2)      # Los parámetros son: el texto, la posición inicial, la fuente, el tamaño de letra, el color y el grosor de la letra.

# Guardar Imagen
cv2.imwrite("Nuevo_Gato.png", im)

# FUNCIÓN CALLBACK AL CLICKAR EN LA IMAGEN
def evento_mouse(evento, x, y, flags, parameters):
    if evento == cv2.EVENT_LBUTTONDOWN:
        print(f"coordenadas en x: {x}, y: {y}")

# Asignar el CAllback a la imagen (nombre de la imagen)
cv2.namedWindow("Normal")
cv2.setMouseCallback("Normal", evento_mouse)

# Mostrar las imágenes
cv2.imshow("Normal", im)

# Esperamos hasta que el usuario presione una tecla y cerramos las ventanas.
cv2.waitKey(0)
cv2.destroyAllWindows()