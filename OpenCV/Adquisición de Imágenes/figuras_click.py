import cv2 as cv
import numpy as np

# Dibujar Linea
def dibujar_linea(im):
    p1 = (300, 60)
    p2 = (200, 60)
    color = (0, 0, 255)
    grosor = 2
    
    cv.line(im, p1, p2, color, grosor)

# Dibujar Rectángulo
def dibujar_rectangulo(im):

    p1 = (500, 60)
    p2 = (700, 500)
    color = (0, 255, 0)
    grosor = 5          # si "-1", entonces, rectangulo relleno
    
    cv.rectangle(im, p1, p2, color, grosor)

# Dibujar Círculo
def dibujar_circulo(im):
    centro = (300,700)
    radio = 100
    color = (255, 0, 0)
    grosor = 10         # si "-1", entonces, circulo relleno
    
    cv.circle(im, centro, radio, color, grosor) 

# Dibujar Elipse
def dibujar_elipse(im):
    centro = (150,300)
    radios = (30, 100)
    # Los ángulos son sobre "z" y "z" mira hacia adentro (ya que "x" hacia derecha, e "y" hacia abajo)
    giro_elipse = 45     
    angulo_inicial = 45
    angulo_final = 235
    color = (255, 255, 0)
    grosor = -1         # si "-1", entonces, elipse rellena
    
    cv.ellipse(im, centro, radios, giro_elipse, angulo_inicial, angulo_final, color, grosor)
    
# Dibujar Elipse
def dibujar_poligono(im):
    p1 = [10, 900]
    p2 = [10, 730]
    p3 = [70, 730]
    p4 = [200, 830]
    p5 = [830, 830]
    p6 = [830, 900]
    
    pts = np.array([p1, p2, p3, p4, p5, p6])
    cerrar_contorno = True
    color = (255, 0, 255)
    grosor = 5
    
    cv.polylines(im, [pts], cerrar_contorno, color, grosor)

# Escribir Texto
def escribir_texto(im):
    texto = "GATETE"
    punto_partida = (500, 800)
    fuente = cv.FONT_HERSHEY_SCRIPT_COMPLEX
    tam_letra = 2
    color = (0, 255, 255)
    grosor = 2
    
    cv.putText(im, texto, punto_partida, fuente, tam_letra, color, grosor)




# Función Callback para Evento 1
def evento_mouse(evento, x, y, flags, parameters):
    if evento == cv.EVENT_LBUTTONDOWN:
        print(f"coordenadas en x: {x}, y: {y}")

# Clase para Evento 2
class Dibujar_Lineas:
    # Constructor: Declara las variables a usar en las otras funciones
    def __init__(self,im):
        self.im = im
        self.startX = 0
        self.startY = 0
        self.dibujando = False
        
    # Función Callback para Evento 2
    def dibujar_linea(self, evento, x, y, flags, parameters):
        im = parameters
        
        if evento == cv.EVENT_LBUTTONDOWN:
            self.dibujando = True
            self.startX = x
            self.startY = y
            print(f"coordenadas en x: {x}, y: {y}")
            
        elif evento == cv.EVENT_MOUSEMOVE and self.dibujando:
            cv.line(self.im, (self.startX, self.startY), (x,y), (255,255,255), 3)
            print(f"cordis en x: {x}, y: {y}")
            
        elif evento == cv.EVENT_LBUTTONUP:
            self.dibujando = False
            print(f"terminado en x: {x}, y: {y}")
    
    # Run: Crea el evento con la función callback
    def run(self):
        nombre_ventana = "Nombre_Evento"
        cv.namedWindow(nombre_ventana)
        cv.setMouseCallback(nombre_ventana, self.dibujar_linea)

        while True:
            cv.imshow(nombre_ventana, self.im)
            if cv.waitKey(1) == ord('q'):
                break

        
if __name__ == '__main__':
    im = cv.imread("Gato.png")
    
    dibujar_linea(im)
    
    dibujar_rectangulo(im)
    
    dibujar_circulo(im)
    
    dibujar_elipse(im)
    
    dibujar_poligono(im)
    
    escribir_texto(im)
    
    
    # Evento 1: Asignar el Callback a la imagen
    """
    nombre_ventana = "Nombre_Evento"    # Tiene que coincidir en las 3 funciones siguientes
    cv.namedWindow(nombre_ventana)
    cv.setMouseCallback(nombre_ventana, evento_mouse)   # Crea el evento con la función callback
    
    cv.imshow(nombre_ventana, im)
    cv.imwrite("Nuevo_Gato.png", im)
    
    cv.waitKey(0)
    cv.destroyAllWindows()
    """
    
    # Evento 2: con Clase
    objeto_linea = Dibujar_Lineas(im)   # Llama al constructor con imagen para declarar variables
    objeto_linea.run()                  # Llama a run que crea el evento con la función callback
    
    