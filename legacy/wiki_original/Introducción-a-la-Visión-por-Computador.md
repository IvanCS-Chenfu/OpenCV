# Índice

- [1. Obtener Distancia con Imágenes](#1-Obtener-Distancia-con-Imágenes)

- [2. Imagen Digitalizada](#2-Imagen-Digitalizada)
   - [2.1. Blanco y Negro](#21-Blanco-y-Negro)
   - [2.2. Color](#22-Color)

- [3. Factores que Intervienen en una Imágen](#3-Factores-que-Intervienen-en-una-Imágen)
   - [3.1. Al Obtener la Imagen](#31-Al-Obtener-la-Imagen)
   - [3.2. Al Procesar la Imagen](#32-Al-Procesar-la-Imagen)

- [4. Etapas de un Proceso de Visión por Computador](#4-Etapas-de-un-Proceso-de-Visión-por-Computador)

- [5. Código](#5-Código)
   - [5.1. Leer y Escribir Imágenes](#51-Leer-y-Escribir-Imágenes)
   - [5.2. Leer y Escribir Videos](#52-Leer-y-Escribir-Videos)
   - [5.3. Manipular Píxeles](#52-Manipular-Píxeles)
   - [5.4. RGB y Gray](#54-RGB-y-Gray)
 
# 1. Obtener Distancia con Imágenes
- Error: Plasma una imagen 2D de un espacio 3D. No tenemos profundidad.
- Solución: Si ponemos dos cámaras separadas, realizamos 2 fotos y nos enfocamos en el mismo objeto en ambas fotos, si sabemos la distancia entre ambas cámaras podremos saber la distancia a la que las cámaras están de dicho objeto.

<p align="center">
   <img height="150" alt="image" src="https://github.com/user-attachments/assets/254cbf06-c933-42a1-8aa7-d8747c2c134a" />
</p>

# 2. Imagen Digitalizada
## 2.1. Blanco y Negro
- Cámara: El sensor utilizado es sensible a la cantidad de luz que entra. Si entra poca luz (píxel negro), la señal dada es pequeña. Si entra mucha luz (píxel blanco), la señal dada es alta.

- Explicación Digital: Se divide la imagen en Pixeles. A cada píxel se le asigna un valor desde el 0 (ausencia de luz o negro absoluto) al 255 (luz máxima o blanco absoluto). Finalmente se crea una matriz bidimensional (cada celda representa a un píxel) en la cual se escriben dichos valores.

<p align="center">
   <img height="350" alt="image" src="https://github.com/user-attachments/assets/19f152bf-e8c2-4093-874d-9c730b5c42df" />
</p>

## 2.2. Color
- Cámara: El sensor utilizado es sensible a la cantidad de rojo, azul y verde que entra. Esto se puede conseguir de varias formas las cuales veremos en [Asquisición de Imágenes](https://github.com/IvanCS-Chenfu/OpenCV/wiki/Adquisici%C3%B3n-de-Im%C3%A1genes#43-De-Estado-S%C3%B3lido).

- Explicación Digital: El mecanismo es prácticamente igual que utilizando. Como la cámara es sensible a 3 colores en vez de a la cantidad de luz, en vez de tener un valor para cada pixel tendremos 3 valores (tendremos finalmente 3 matrices bidimensionales para cada imagen).

<p align="center">
   <img height="350" alt="image" src="https://github.com/user-attachments/assets/23f5d2e6-5e92-4cc2-8b62-8c02ce3149a5" />
</p>

# 3. Factores que Intervienen en una Imágen
## 3.1. Al Obtener la Imagen

- Iluminación de la Escena.
- La Geometría del Objeto.
- Color y Textura del Objeto.
- Distorsión de los Sistemas de Adquisición: En algunas lentes se puede apreciar un error y alargar los extremos al realizar la fotografía (por eso las fotos se hacen desde el centro).
- Ruido Externo.

## 3.2. Al Procesar la Imagen
- Gran Cantidad de Datos: Una imagen muy simple puede ocupar más que 100 páginas de texto.

<p align="center">
   <img height="150" alt="image" src="https://github.com/user-attachments/assets/ba48b830-7762-419e-ac49-13b866fc6b6d" />
</p>

- Gran Capacidad de Procesamiento: Puede obtener información muy precisa en grandes cantidades y a una gran velocidad. El ojo humano procesa una imagen de forma relativa, sin embargo, un ordenador lo hace de forma absoluta.

<p align="center">
   <img height="150" alt="image" src="https://github.com/user-attachments/assets/be756e85-37e9-442f-a514-3d08c1e7ad3a" />
</p>

- Espectro de la Luz: Nosotros solo observamos en el espectro visible, sin embargo, una cámara puede ser sensible a cualquier frecuencia del espectro de la luz. 

<p align="center">
   <img height="150" alt="image" src="https://github.com/user-attachments/assets/f708e6c6-cc79-42d5-aaf4-cd0cecc3314a" />
</p>

# 4. Etapas de un Proceso de Visión por Computador
- Todos los Niveles

<p align="center">
   <img height="300" alt="image" src="https://github.com/user-attachments/assets/0a3589ba-473e-4c59-a254-4cddad870d4e" />
   <img height="300" alt="image" src="https://github.com/user-attachments/assets/4bb1a1ad-0205-4690-829a-ba3a3fffa1d4" />
</p>

- Nivel Bajo (Adquisición y Digitalización)

<p align="center">
   <img height="300" alt="image" src="https://github.com/user-attachments/assets/9106d3c2-ff6c-49f9-a697-65be21f64724" />
</p>


# [Bibliografía](https://github.com/user-attachments/files/25093461/Tema.1.pdf)


# 5. Código
## 5.1. Leer y Escribir Imágenes
En el código [read_write_im.py](https://github.com/IvanCS-Chenfu/OpenCV/blob/main/OpenCV/Introducci%C3%B3n%20a%20la%20Visi%C3%B3n%20por%20Computador/read_write_im.py) se realiza lo siguiente.

Se obtiene el "Path" de una imagen
```python
root = os.getcwd()
imgPath = os.path.join(root, 'Nombre_Imagen.png')
```

Se obtiene la imagen (matriz de numpy)
```python
img = cv.imread(imgPath)
```

Se muestra la imagen
```python
cv.imshow('titulo_de_imagen',img)
```

Se guarda esa imagen en un path dado y con otro nombre.
```python
root = os.getcwd()
imgPath = os.path.join(root, 'Nombre_Imagen_Guardar.png')
cv.imwrite(outPath, img)
```

También se muestran ciertos datos de la imagen
```pyhton
# Tipo de Datos
tipo_dato = img.dtype

# Valores máximos y mínimos
max = img.max()
min = img.min()

# Tamaño
tam = img.shape
tam_x = img.shape[0]
tam_y = img.shape[1]
tam_z = img.shape[2]
```

## 5.2. Leer y Escribir Videos
En el código [read_write_video.py](https://github.com/IvanCS-Chenfu/OpenCV/blob/main/OpenCV/Introducci%C3%B3n%20a%20la%20Visi%C3%B3n%20por%20Computador/read_write_video.py) se realiza lo siguiente.

Una vez obtenido el "Path" de un video, se obtiene el objeto de dicho video. Si ```videoPath``` es un número, estamos abriendo una webcam del ordenador.
```python
video = cv.VideoCapture(videoPath)
```

Se muestra cada frame del video (o los frames mostrados por la webcam) y se guardan en un array.
```python
frames = [] # Array para guardar el video

if not video.isOpened(): # Da "false" cuando no encuentra la cámara
    exit()

ret = True
while ret:          
    ret, frame = video.read()   # Obtiene un booleano (ret) que dice si se ha leido bien la imagen (al terminar el video devuelve false). Obtiene cada imagen del video (frame)
    
    fps = 30.0
    delay = int(1000/(fps*2))   # Tiempo de espera en "ms" entre frames (se multiplica x2 para que cuadre)
    
    if ret:
        cv.imshow('Nombre_Video',frame)     # Muestra cada imagen del video (formando el video)
        frames.append(frame)                # Guarda cada frame del video
    
    if cv.waitKey(delay) == ord('q'):       # si el usuario pulsa "q", sale del bucle (se para el video)
        break
```

Finalmente se guarda el video (los frames obtenidos) en un nuevo "Path".
```python
fourcc = cv.VideoWriter_fourcc(*'XVID')     # Formato del video (MP4)
fps = 30.0                                  # FPS que quiero guardarlo
frame_size = (640,480)                      # Tamaño del Frame a guardar

out = cv.VideoWriter(outPath,fourcc,fps,frame_size)     # Objeto del video a Guardar

# Se lee el video que queremos guardar y guardamos cada uno de sus frames
for frame in frames:

    out.write(frame)    # Guardamos (o sobrescribimos) los frames en el path mencionado
        
out.release()       # Obligatorio cerrar el objeto del video a guardar
```

Es oligatorio siempre cerrar el objeto del video (para no dejar la webcam abierta)
```python
video.release()     # Obligatorio cerrar el objeto del video
cv.destroyAllWindows()  # Cerrar todas las ventanas
```

## 5.3. Manipular Píxeles
En el código [manipular_pixeles.py](https://github.com/IvanCS-Chenfu/OpenCV/blob/main/OpenCV/Introducci%C3%B3n%20a%20la%20Visi%C3%B3n%20por%20Computador/manipular_pixeles.py) se realiza lo siguiente.

Se muestra como OpenCV utiliza color BGR (la matriz "Blue" primer, "Green" segundo y "Red" tercero) mientras que MatPlotLib usa RGB.

<p align="center">
   <img height="300" alt="image" src="https://github.com/user-attachments/assets/f7559c84-7a85-4c17-8a9c-5411e1394b52" />
   <img height="300" alt="image" src="https://github.com/user-attachments/assets/51835316-a677-4dcb-b910-faad6e15ea6f" />
</p>

Se obtienen subimagenes de la imagen principal
```python
ojos = im_RGB[274:372, 203:602]  # Los pixeles en MatPlotLib están alreves "[y,x]"
```

<p align="center">
   <img height="150" alt="image" src="https://github.com/user-attachments/assets/bbee7916-ce0d-47bb-8169-16893122f88a" />
</p>

Se edita la imagen principal
```python
im_RGB[311, 347] = (255, 0, 0)
im_RGB[274:372, 203:602] = (0, 255, 0)
```
<p align="center">
   <img height="300" alt="image" src="https://github.com/user-attachments/assets/37e2cc2e-c3cb-4fb0-9ce8-882944420e89" />
   <img height="300" alt="image" src="https://github.com/user-attachments/assets/3ff70e14-974d-4411-9357-d8a95f39acd8" />
</p>

## 5.4. RGB y Gray
En el código [RGB_gray.py](https://github.com/IvanCS-Chenfu/OpenCV/blob/main/OpenCV/Introducci%C3%B3n%20a%20la%20Visi%C3%B3n%20por%20Computador/RGB_gray.py) se realiza lo siguiente.

Se muestran como los colores son matrices con distintos valores.
```python
tam = (100,100)

zeros = np.zeros(tam)
ones = np.ones(tam)

b = cv.merge((zeros,zeros,255*ones))
g = cv.merge((zeros,255*ones,zeros))
r = cv.merge((255*ones,zeros,zeros))

bg = cv.merge((zeros,255*ones,255*ones))
gr = cv.merge((255*ones,255*ones,zeros))
br = cv.merge((255*ones,zeros,255*ones))

negro = cv.merge((zeros,zeros,zeros))
blanco = cv.merge((255*ones,255*ones,255*ones))
```

<p align="center">
   <img height="350" alt="image" src="https://github.com/user-attachments/assets/55a27c9d-b5b3-4ebc-9c84-b64403c65afd" />
</p>

Se separa la imagen RGB en submatrices R, G y B. 
```python
r,g,b = cv.split(im_RGB)
```

<p align="center">
   <img height="350" alt="image" src="https://github.com/user-attachments/assets/925dcd64-dd11-4f6f-bb40-d5210d719acc" />
</p>

Se pasa una imagen a escala de grises
```python
im_gray = cv.cvtColor(im,cv.COLOR_BGR2GRAY)
```
<p align="center">
   <img height="300" alt="image" src="https://github.com/user-attachments/assets/5fba20e2-4cff-45b3-9689-abb0d6effdba" />
</p>
