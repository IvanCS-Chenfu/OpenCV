# Índice

- [1. Ruidos en la Imagen](#1-Ruidos-en-la-Imagen)
   - [1.1. Objetivo](#11-Objetivo)
   - [1.2. Fuentes de Ruido](#12-Fuentes-de-Ruido)
   - [1.3. Tipos de Ruido](#13-Tipos-de-Ruido)

- [2. Suavizado de Imágenes](#2-Suavizado-de-Imágenes)
   - [2.1. Dominio Espacial](#21-Dominio-Espacial)
   - [2.2. Dominio Frecuencial](#22-Dominio-Frecuencial)

- [3. Realce de Imágenes](#3-Realce-de-Imágenes)
   - [3.1. Explicación](#31-Explicación)
   - [3.2. Transformaciones Básicas](#32-Transformaciones-Básicas)
   - [3.3. Igualación de Histograma](#33-Igualación-de-Histograma)
   - [3.4. Especificación de Histograma](#34-Especificación-de-Histograma)
   - [3.5. Realce Local](#35-Realce-Local)
   - [3.6. Dominio Frecuencial](#36-Dominio-Frecuencial)

- [4. Detección de Discontinuidades](#4-Detección-de-Discontinuidades)
   - [4.1. Explicación](#41-Explicación)
   - [4.2. Derivada](#42-Derivada)
   - [4.3. Gradiente](#43-Gradiente)
   - [4.4. Laplaciana](#44-Laplaciana)
   - [4.5. Algoritmo de Canny](#45-Algoritmo-de-Canny)



# 1. Ruidos en la Imagen
## 1.1. Objetivo
Mejorar la imagen inicial para evitar problemas y mejorar a la hora de procesarla. Se puede realizar tanto en espacial como en el dominio frecuencial.

<p align="center">
   <img height="250" alt="image" src="https://github.com/user-attachments/assets/e275fc00-5fee-43b2-914f-092283455cf9" />
</p>

## 1.2. Fuentes de Ruido
- Adquisición: Depende de la calidad y temperatura alcanzada por el CCD empleado.

- Transmisión: Interferencias durante la transmisión.

- Ambiental: Partículas en el entorno.

## 1.3. Tipos de Ruido
- Ruido Blanco (espectro de Fourier uniforme).
   - Gaussiano.
   - Gamma.
   - Exponencial.
   - Uniforme.
   - Impulso ("Salt and Pepper").

<p align="center">
   <img height="275" alt="image" src="https://github.com/user-attachments/assets/a0335c68-eb97-4793-9719-b64e43dad355" />
</p>

- Ruido Periódico Espacial

<p align="center">
   <img height="275" alt="image" src="https://github.com/user-attachments/assets/26fa15f8-7463-4813-bb72-f94d0c22bc27" />
</p>

# 2. Suavizado de Imágenes
## 2.1. Dominio Espacial
### 2.1.1. Filtros de Media
- Aritmética: Se realiza una convolución con una máscara en la que todas sus celdas sean iguales y su suma sea igual a 1.

<p align="center">
   <img height="200" alt="image" src="https://github.com/user-attachments/assets/f77da63e-ab62-401e-8a8a-e49ca4028bbc" />
</p>

- Aritmética Modificada: Se aplica solo en ciertos píxeles que cumplan una condición.

<p align="center">
   <img height="350" alt="image" src="https://github.com/user-attachments/assets/ee6d6e93-d98d-437f-be5c-6b8755a8dde8" />
</p>

### 2.1.2. Filtrado Gaussiano
La máscara empleada no tiene todas sus celdas iguales, sino que le da más valor a las céntricas como si de una campana de gauss se tratase. El tamaño depende de "\sigma"

<p align="center">
   <img height="225" alt="image" src="https://github.com/user-attachments/assets/a6151b99-2f64-4889-b6bb-b0a8080eac00" />
</p>

La gaussiana en 2 dimensiones es separable. Esto es útil para reducir el costo.

<p align="center">
   <img height="150" alt="image" src="https://github.com/user-attachments/assets/16831d3c-bb07-4f3e-9244-33b133375cd8" />
   <img height="150" alt="image" src="https://github.com/user-attachments/assets/b235079d-2ad7-41d3-b607-4e1364a8f911" />
</p>

### 2.1.3. Filtros Estadísticos
- Mediana: Colocas tanto un pixel como los de su alrededor de menor a mayor. De esa lista, eliges la del centro.

<p align="center">
   <img height="200" alt="image" src="https://github.com/user-attachments/assets/01f03a50-9b56-463d-b8b3-ab3e1b3a8e7f" />
</p>

### 2.1.4. Filtros Adaptables

Dependiendo del entorno de vecindad de un píxel se le aplicará un filtro u otro.

<p align="center">
   <img height="75" alt="image" src="https://github.com/user-attachments/assets/6fc2f0af-1c11-47e6-bb91-da289aaa434e" />
</p>

- $f(x,y)$ : el valor de gris de un píxel situado en $(x, y)$ .
- $\sigma_\eta^2$ : varianza del ruido en la imagen.
- $\sigma_L^2$ : varianza de los pixeles en un entorno de vecindad de $(x, y)$ .
- $m_L$ : media de los pixeles en el entorno de vecindad.
   - Para evitar valores negativos, si $\sigma_\eta^2 > \sigma_L^2 \rightarrow \sigma_\eta^2 = \sigma_L^2 \rightarrow f(x,y) = m_L$ .

### 2.1.5. Promediado de Imágenes
Se obtienen "N" imágenes de la misma forma. Cada una de estas imágenes tendrá un ruido diferente, pero mantendrán la esencia de la foto. Al hacer una media entre todas las fotos obtendremos esa esencia sin errores.

<p align="center">
   <img height="250" alt="image" src="https://github.com/user-attachments/assets/ec509919-0e45-46ed-ae88-aba866208f7f" />
</p>

## 2.2. Dominio Frecuencial
Pasaremos nuestra imagen al dominio frecuencial, le aplicaremos un filtro (normalmente tendremos que centrar la imagen) y devolveremos la imagen al dominio espacial.

<p align="center">
   <img height="325" alt="image" src="https://github.com/user-attachments/assets/da080cb5-7c1f-4000-a669-296de07a769e" />
</p>

### 2.2.1. Filtros Paso Bajo
- Ideal

<p align="center">
   <img height="150" alt="image" src="https://github.com/user-attachments/assets/bf6e1303-f12d-48f1-839e-3e06d909ce3d" />
</p>

- Butterworth

<p align="center">
   <img height="150" alt="image" src="https://github.com/user-attachments/assets/39e57a6d-e6cf-4242-b874-877b056813a9" />
</p>

### 2.2.2. Filtros Rechazo Banda
- Ideal

<p align="center">
   <img height="150" alt="image" src="https://github.com/user-attachments/assets/cb81763b-5915-4488-80bc-19999967cdcd" />
</p>

- Butterworth

<p align="center">
   <img height="150" alt="image" src="https://github.com/user-attachments/assets/07ab3241-76c6-4d9d-95ba-25299a55e579" />
</p>

### 2.2.3. Otros Filtros
Se pueden aplicar filtros no centrados en la imagen:

<p align="center">
   <img height="250" alt="image" src="https://github.com/user-attachments/assets/3886a2eb-094b-419d-b1c6-a90e196d2e0f" />
</p>

# 3. Realce de Imágenes
## 3.1. Explicación
Aumenta el contraste redistribuyendo los niveles de grises de una imagen.
## 3.2. Transformaciones Básicas
Aplicar LUTs.

<p align="center">
   <img height="275" alt="image" src="https://github.com/user-attachments/assets/7c1bd3a9-18d1-4d39-9b5f-4f9d07b1f42b" />
   <img height="275" alt="image" src="https://github.com/user-attachments/assets/9c5e326f-c583-4d46-9968-d0c276a428d6" />
</p>



## 3.3. Igualación de Histograma
Igualación de Histograma: Se intenta aprovechar todo el rango de niveles de grises. Si un histograma está muy centrado a la izquierda (imagen muy oscura) o a la derecha (imagen muy clara) se intentan repartir por todo el rango de grises.

<p align="center">
   <img height="275" alt="image" src="https://github.com/user-attachments/assets/07c20340-267d-4a81-812b-524a9c92b43b" />
</p>

Crearemos una LUT explicita para la imagen que queremos realizar. Esta LUT se realizará de la siguiente forma:
- Normalizar el histograma: Dividir el histograma entre su número de elementos con el fin de tener una función de densidad (la suma de todos los elementos nuevos es igual a 1).

- Suma acumulada de todos los elementos del histograma normalizado: Esto realizará una LUT que vaya de "0" a "1", que no sea multievaluada y que sea monótona creciente.

- Multiplicar la LUT por 255.

## 3.4. Especificación de Histograma
Queremos que una imagen tenga un histograma específico. 

- Utilizaremos otra imagen la cual tenga el histograma que nosotros queremos.

- Mediante el método de igualación de histograma crearemos dos imágenes igualadas (la de la imagen con el histograma requerido y la de nuestra imagen).

- Utilizaremos la inversa de la LUT que hemos aplicado a la imagen con el histograma requerido. Esta se aplicará sobre la imagen igualada proveniente de nuestra imagen inicial.

<p align="center">
   <img height="250" alt="image" src="https://github.com/user-attachments/assets/3886a2eb-094b-419d-b1c6-a90e196d2e0f" />
</p>

## 3.5. Realce Local
Aplicamos lo anterior pero solo a una zona de la imagen
- Si hay mucho contraste me quedo con la media y si hay poco contraste le doy más contraste.

<p align="center">
   <img height="300" alt="image" src="https://github.com/user-attachments/assets/2c9f721d-4979-4794-a6eb-c629d7983b2c" />
</p>

- Aumento de nitidez: Tengo una imagen, la suavizo, la resto por la imagen original, entonces, le sumo a la imagen original la resta.

## 3.6. Dominio Frecuencial
Los contornos y cambios abruptos se asocian con las altas frecuencias. Si queremos realzar los contornos de una imagen podremos utilizar filtros paso alto.

# 4. Detección de Discontinuidades
## 4.1. Explicación
Las discontinuidades son representadas por pixeles en los que alrededor suyo existe una variación brusca en los niveles de grises. Las discontinuidades no son perfectas (escalón), sino que se realizan de forma gradual. Para realizar una buena detección de la discontinuidad deberemos eliminar el ruido en un principio.

<p align="center">
   <img height="300" alt="image" src="https://github.com/user-attachments/assets/2862c188-4d58-4e1d-baf3-daa388ee2ba7" />
</p>

En la detección de discontinuidades hay 3 problemas típicos: Errores en la detección (falsos positivos y falsos negativos), errores en la localizacion y múltiples respuestas para un mismo borde.

<p align="center">
   <img height="175" alt="image" src="https://github.com/user-attachments/assets/3c92ac94-ebe4-4e75-b149-7f5bca1b36e6" />
</p>

## 4.2. Derivada
Proporciona información de la velocidad de variación de los niveles de grises. El ruido afecta demasiado. Al tratarse de imágenes, todas las derivadas son discretas y se aproximan por diferencias.

- Primera Derivada: Es "0" en las regiones con intensidad constante y tiene un valor constante en la transición de intensidad. (La discontinuidad es el máximo).

- Segunda Derivada: Es "0" en todos los puntos menos al comienzo y al final de una transición. (La discontinuidad es un paso por cero de un máximo a un mínimo relativo y viceversa)

<p align="center">
   <img height="350" alt="image" src="https://github.com/user-attachments/assets/0d240f75-818a-4f19-9714-e5f97b9e6ea7" />
</p>

## 4.3. Gradiente
Vector formado por las derivadas parciales. Su dirección apunta a la máxima variación de los niveles de grises (perpendicular a la dirección de la discontinuidad). Son interesantes el módulo y la dirección del vector gradiente.

<p align="center">
   <img height="75" alt="image" src="https://github.com/user-attachments/assets/58aeb25e-3833-4f34-8d70-e339594baf92" />
</p>

Procedimiento: Tenemos una imagen normal y aplicando la máscara gradiente obtenemos la imagen gradiente. Vemos que valores superan un umbral, los volvemos a "1" y todos los demás los volvemos a "0" obteniendo una imagen binaria ("1" representa discontinuidad y "0" no). Finalmente adelgazamos los píxeles haciendo que nuestra discontinuidad sea del tamaño de 1 píxel.

<p align="center">
   <img height="325" alt="image" src="https://github.com/user-attachments/assets/7758f3da-9747-4e99-9edf-2b8968821834" />
</p>

Tipos de Máscara Gradiente: Relación inmunidad ante el ruido, coste computacional y precisión de la localización. Cuanto mayor es el tamaño menor es la inmunidad ante el ruido y la precisión, pero mayor es el coste. Por otro lado, por convolución podremos obtener una máscara que suavice y a la vez detecte discontinuidades.

- Diferencia: Poco coste computacional pero sensible al ruido.

<p align="center">
   <img height="225" alt="image" src="https://github.com/user-attachments/assets/b9d38a8c-f339-4ae6-b30c-74d00d4b0e9c" />
</p>

- Operador de PreWitt: Mayor coste computacional pero más inmune al ruido.

<p align="center">
   <img height="200" alt="image" src="https://github.com/user-attachments/assets/38a007d5-378b-4e5e-a501-c57670f29f68" />
</p>

- Operador de Sobel

<p align="center">
   <img height="200" alt="image" src="https://github.com/user-attachments/assets/4b17c02f-d556-475b-afe4-affcbc25ff23" />
</p>

- Operador de Frei-Chen

<p align="center">
   <img height="200" alt="image" src="https://github.com/user-attachments/assets/5da56f52-2131-4e89-9281-42125395147e" />
</p>

- Suavizar y encontrar Discontinuidades: Existen 2, con media y con gausiana (DroG). DroG (Diferencia de Gauusianas) es separable

<p align="center">
   <img height="225" alt="image" src="https://github.com/user-attachments/assets/91b5d66b-bd9e-4dd3-ae0a-ee01c75986af" />
   <img height="175" alt="image" src="https://github.com/user-attachments/assets/94e838e0-4aad-44fc-b71d-c278b7ad4bfb" />
   <img height="175" alt="image" src="https://github.com/user-attachments/assets/9d1fd656-2942-4b3f-87e8-760d28b44a03" />
</p>

Adelgazamiento: Me sitúo en un píxel y miro la dirección del vector gradiente en ese punto. Si el módulo de su vector gradiente es menor que alguno de sus dos vecinos en la dirección del gradiente, lo ponemos a "0". Solo detecta un píxel por borde (no hay problema de múltiple respuesta)

<p align="center">
   <img height="225" alt="image" src="https://github.com/user-attachments/assets/7139977e-9203-4a7e-a617-0cdb41875851" />
</p>

## 4.4. Laplaciana
Prácticamente igual que lo anterior, pero utilizando la segunda derivada en vez de la primera. No es un vector así que no obtendremos información acerca de la dirección del contorno. Extremadamente sensible al ruido. Al ser la segunda derivada, se necesita un algoritmo que detecte los pasos por 0.

<p align="center">
   <img height="75" alt="image" src="https://github.com/user-attachments/assets/5e5c4d8f-8aea-4ad1-b457-242ad8c48796" />
</p>

Tipos de Máscara:
- 4 vecinos

<p align="center">
   <img height="150" alt="image" src="https://github.com/user-attachments/assets/252ec46b-a14f-4464-9add-f603113b754d" />
</p>

- 8 Vecinos

<p align="center">
   <img height="150" alt="image" src="https://github.com/user-attachments/assets/7d6ada0d-ba72-4113-8e0e-920d686647ae" /></p>
</p>

Como es muy sensible al ruido, se suavizaa y se encuentran discontinuidades mediante el laplaciano de la gaussiana (LoG):

<p align="center">
   <img height="225" alt="image" src="https://github.com/user-attachments/assets/0b3e0998-6ce7-4409-8d58-70fecfd32390" />
   <img height="225" alt="image" src="https://github.com/user-attachments/assets/857c2349-9d65-491f-aff7-adfbf2426c39" />
</p>

LoG no es separable y es costoso computacionalmente. Debido a eso existe una aproximación restando 2 gaussianas (DoG). El ratio $\sigma_1 / \sigma_2 = 1.6$ es la mejor aproximación del LoG.

<p align="center">
   <img width="328" height="256" alt="image" src="https://github.com/user-attachments/assets/8bac5495-42fc-4585-b556-60ec9d5d4d19" />
</p>

Dominio Frecuencial:

<p align="center">
   <img height="75" alt="image" src="https://github.com/user-attachments/assets/62d7bdff-9df2-4d13-b0bb-1a919651eb8c" />
</p>


## 4.5. Algoritmo de Canny
El algoritmo completo sigue estos 3 pasos:

- Cálculo del gradiente (intensidad y dirección): Se calcula el gradiente usando DroG (suavizando y derivando). 
- Supresión de no-máximos: Se adelgaza utilizando la dirección del gradiente (como se ha explicado anteriormente).
- Umbralización con histéresis: Se utiliza histéresis ya que queremos los puntos cuyo gradiente sea máximo pero prevenir la desconexión del contorno. Los bordes que superan el umbral fuerte, se mantienen. Los bordes que están entre ambos umbrales pero están conectados a píxeles fuertes, se mantienen. Los píxeles que están entre los dos umbrales pero no se conectan a píxeles fuertes, se eliminan. Los píxeles menores al umbral menor, se eliminan.

<p align="center">
   <img height="250" alt="image" src="https://github.com/user-attachments/assets/b5378117-f031-4963-8889-063953138641" />
</p>


# [Bibliografía](https://github.com/user-attachments/files/25095445/Tema.5.pdf)
