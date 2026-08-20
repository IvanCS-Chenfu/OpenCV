# Cámara
## Utilizar Cámara [(1_Abrir_Camara.py)](https://github.com/IvanCS-Chenfu/OpenCV/blob/main/Tutorial/1_Abrir_Camara.py)
`cap = cv2.VideoCapture(0)`: Abre la cámara.

`ret, frame = cap.read()`: Obtiene el frame de la cámara y un booleano `ret` que indica si se ha conseguido leer el frame.

`cap.release()`: Necesario para liberar la cámara.

## Guardar Video [(2_Guardar_Video.py)](https://github.com/IvanCS-Chenfu/OpenCV/blob/main/Tutorial/2_Guardar_Video.py)
`Video = "Nombre.mp4"`: Asignar un nombre al video.

`fourcc = cv2.VideoWriter_fourcc(*"mp4v")`: Asignar formato `mp4` al video.

`fps = 30`: Asignar velocidad de fps al video.

`frame_width = int(cap.get(3))`: Asignar anchura al video.

`frame_height = int(cap.get(4))`: Asignar altura al video.

`out = cv2.VideoWriter(Video, fourcc, fps, (frame_width, frame_height))`: Crear el objeto del video.

`out.write(frame)`: Guardar cada fotograma en el objeto del video.

`out.release()`: Parar la grabación.

## Condición
`cap.isOpened()`: Devuelve "true" cuando la cámara esta abierta.

# Imágenes

## Filtros [(3_Filtros.py)](https://github.com/IvanCS-Chenfu/OpenCV/blob/main/Tutorial/3_Filtros.py)

`im_blur = cv2.GaussianBlur(im, (n,m), sigma)`: Aplica en `im` un filtro Gaussiano de tamaño `n*m` y de desviación típica `sigma`.

`im_canny = cv2.Canny(im_gray, 100, 200)`: Aplica en una imagen gris `im_gray` un filtro Canny (bordes). `100 y 200`¿?¿?¿?¿?.

`im_mb = cv2.medianBlur(im,13)`: ¿?¿?¿

## Dibujos en Imagenes [(4_Figuras_Click.py)](https://github.com/IvanCS-Chenfu/OpenCV/blob/main/Tutorial/4_Figuras_Click.py)

`cv2.line(im,(PX1, PY1),(PX2,PY2), (B, G, R), gros)`: Pinto en `im` una linea que va del punto `P1` al `P2` del color `BGR` y del grosor `gros`.

`cv2.rectangle(im,(PX1, PY1),(PX2,PY2), (B, G, R), gros)`: Pinto en `im` un rectángulo cuyas esquinas diagonales sean `P1` y `P2`, el color sea `BGR` y el grosor sea `gros`.

`cv2.circle(im,(CX, CY), r, (B, G, R), gros)`: Pinto en `im` un círculo con centro en `C`,  el color sea `BGR` y el grosor sea `gros`. Si `gros` es `-1`, el círculo se llena.

`cv2.putText(im,"Text", (PX, PY), cv2.FONT_HERSHEY_SCRIPT_COMPLEX, tam, (B, G, R), gros)`: Pinto en `im` en texto `text` empezando desde el punto `P`. Los demás parámetros son la fuente, el tamaño de la letra, el color y el grosor.

## Obtener el Punto Clicado [(4_Figuras_Click.py)](https://github.com/IvanCS-Chenfu/OpenCV/blob/main/Tutorial/4_Figuras_Click.py)

Función necesaria la cual se llamada cada vez que se clica en la imagen.
```python
def evento_mouse(evento, x, y, flags, parameters):
    if evento == cv2.EVENT_LBUTTONDOWN:
        print(f"coordenadas en x: {x}, y: {y}")
```

`cv2.namedWindow("Nombre")`: Asignar el nombre de la ventana.

`cv2.setMouseCallback("Nombre", evento_mouse)`: Asignar la ventana a la función anterior.

`cv2.imshow("Nombre", im)`: Se muestra la imagen en la cual se podrá clicar para obterner las coordenadas de la misma.

## Binarización de una Imagen
### Umbralización [(5_Umbralizacion.py)](https://github.com/IvanCS-Chenfu/OpenCV/blob/main/Tutorial/5_Umbralizacion.py)

`_,binarizada=cv2.threshold(im_gray,umbral,255,cv2.THRESH_BINARY)`: Pone a `255` todos los tonos mayores a `umbral` y a 0 los menores.

`_,binarizada_inv=cv2.threshold(im_gray,umbral,255,cv2.THRESH_BINARY_INV)`: Pone a `255` todos los tonos menores a `umbral` y a 0 los mayores.

`_,truncada=cv2.threshold(im_gray,umbral,255,cv2.THRESH_TRUNC)`: Mantiene la imagen igual excepto los tonos mayores al `umbral`, los cuales se ponen en el color del `umbral`.

`_,toz=cv2.threshold(im_gray,umbral,255,cv2.THRESH_TOZERO)`: Deja igual todos los tonos mayores a `umbral` y a 0 los menores.

`_,toz_inv=cv2.threshold(im_gray,umbral,255,cv2.THRESH_TOZERO_INV)`: Deja igual todos los tonos menores a `umbral` y a 0 los mayores.

## Colores

### Cambiar Colores [(6_Colores.py)](https://github.com/IvanCS-Chenfu/OpenCV/blob/main/Tutorial/6_Colores.py)

`rgb = cv2.cvtColor(bgr, cv2.COLOR_BGR2RGB)`: OpenCV funciona en BGR. Esto cambia de BGR a RGB.

`im_gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)`: Cambiar de BGR a Escala de Grises.

`hsv = cv2.cvtColor(bgr, cv2.COLOR_BGR2HSV)`: Cambia de BGR a HSV.

### Detectar Colores [(7_Detectar_Colores.py)](https://github.com/IvanCS-Chenfu/OpenCV/blob/main/Tutorial/7_Detectar_Colores.py)

Umbrales entre los que tienen que estar los valores de cada pixel para obtenerlo. `0 <= H <= 179`, `0 <= S <= 255` y `0 <= V <= 255`
```python
umb_abajo = np.array([0,100,20],np.uint8)
umb_arriba = np.array([8,255,255],np.uint8)
```

`maskR_1=cv2.inRange(hsv,umb_abajo,umb_arriba)`: Crea una matriz binaria. Los valores que se encuentran entre los umbrales se ponen a 1. Los que no, a 0.

`maskR = cv2.add(maskR_1,maskR_2)`: Junta varias máscaras.

`mask_aplicada = cv2.bitwise_and(im, im, mask= maskR)`: Aplica la máscara `maskR` a la imagen `im`.

## Contornos [(8_Detectar_Contornos.py)](https://github.com/IvanCS-Chenfu/OpenCV/blob/main/Tutorial/8_Detectar_Contornos.py)

`contornos,jerarquia = cv2.findContours(im_bin, cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)`: Obtiene los contornos de una imagen binarizada `im_bin`.
El segundo parámetro es el Modo: `RETR_LIST`, `RETR_EXTERNAL`, `RETR_CCOMP`y `RETR_TREE`.
El tercer parámetro es el Método: `CHAIN_APPROX_NONE` y `CHAIN_APPROX_SIMPLE`.
En cuanto a la Jerarquía: `[Next,Previous,First_Child,Parent]`. Esto muestra los contornos en el mismo nivel `Next` y `Previous`, y los de distintos niveles `First_Child` y `Parent`.

`cv2.drawContours(im,contornos, -1 ,(B,G,R), gros)`: Dibuja todos (-1) los contornos en `BGR` con grosor `gros` en la imagen `im`.

## Características

`ancho = im.shape[1]`: Devuelve el ancho de la imagen `im`.

`alto = im.shape[0]`: Devuelve el alto de la imagen `im`.

`area = cv2.contourArea(contornos)`: Area de una figura dado su contorno.

`cerco_convexo = cv2.convexHull(contorno)`: Crea el cerco convexo de un contorno.

Coordenadas del punto medio de un contorno.
```python
M = cv2.moments(contorno)
x = int(M["m10"]/M["m00"])
y = int(M["m01"]/M["m00"])
```

`x,y,w,h = cv2.boundingRect(contorno)`: Devuelve el rectángulo que envuelve el contorno en los cuales los puntos de las esquinas diagonáles son `P1 = (x,y)` y `P2 = (x+w,y+h)`.

`epsilon = beta*cv2.arcLength(contorno,True)`: Parámetro que sirve para la precisión de la aproximación siguiente. `Beta` es un parámetro que debemos variar y `True` es debido a si `contorno` es una curva cerrada. 

`approx = cv2.approxPolyDP(contorno,epsilon,True)`: Aproxima un contorno a un polígono. La longitud de `approx` es el número de vértices.

## Juntar Imágenes [(9_Juntar_Imagenes)]()

`add = cv2.add(im1,im2)`: Suma ambas. Si se pasa de 255, se queda en 255.

`add_weight = cv2.addWeighted(im1,alpha1,im2,0.5,beta)`: Cada imagen la multiplica por el numero de su derecha (`alpha1` / `alpha2`) y le suma el último número `beta`.

`sub = cv2.subtract(im1,im2)`: Resta ambas. Si se pasa de 0, se queda en 0.

`absdif = cv2.absdiff(im1,im2)`: Resta ambas y le realiza el absoluto.

## Transformar Imágenes [(11_Transformaciones)]()

`T_tras = np.float32([[1,0,-180],[0,1,100]])`: Crea una matriz de Transformación con una traslación.

`T_rot = cv2.getRotationMatrix2D((ancho//2,alto//2),angulo,escala)`: Crea una matriz de Transformación con una rotación. Los parámetros son: Centro de la rotación `ancho//2,alto//2`, `angulo` y `escala`).

`im_tras = cv2.warpAffine(im,T_tras,(ancho,alto))`: Aplica a la imagen una matriz de Transformación y deja igual el alto y el ancho de la ventana.

`im_resize = cv2.resize(im,(ancho_querido,alto_querido), interpolation=cv2.INTER_CUBIC)`: Escala la imagen sin mantener la relación entre la altura y el ancho.

`im_altura = imutils.resize(im, height=50)`: Escala la imagen manteniendo la relación altura-ancho.

`im_ancho = imutils.resize(im, width = 500)`: Escala la imagen manteniendo la relación altura-ancho.

`im_recorte = im[150:300,200:400]`: Recorta la imagen.

`im_flip = cv2.flip(im,a)`: Realiza el espejo de la imagen `im`. Si `a` es `0`, `1` o `-1`, realiza el espejo horizontal, vertical o ambas respectivamente.

# Comunes

`cv2.imshow("Nombre", im)`: Se habre una ventana llamada `Nombre` en la cual se muestra la imagen `im`

`cv2.destroyAllWindows()`: Cierra todas las ventanas.

`cv2.waitKey(n)`: espera `n` milisegundos a que el usuario presione una tecla. Si la presiona, devuelve el código ASCII de la misma y si no la prisiona, sigue el programa. Si `n` es 0, el tiempo de espera es infinito.

```python
cv2.namedWindow('Ventana')
cv2.createTrackbar('Nombre','Ventana',valor_ini,max,callback)
val = cv2.getTrackbarPos('Nombre','Ventana')
```
Crea una barra en una Ventana y se obtiene el valor de la barra. `Nombre` es el nombre de la barra, `Ventana` es en nombre de la ventana, `valor_ini` es el valor inicial de la barra, `max` es el umbral superior de la barra, y `callback` es una función que se llamará cuando se accione la barra.


# Cosas a Futuro
- Tesseract y Pytesseract