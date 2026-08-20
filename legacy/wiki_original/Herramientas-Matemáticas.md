# Índice

- [1. Relaciones entre Píxeles](#1-Relaciones-entre-Píxeles)
   - [1.1. Explicación](#11-Explicación)
   - [1.2. Tipos](#12-Tipos)

- [2. Histogramas](#2-Histogramas)
   - [2.1. Explicación](#21-Explicación)
   - [2.2. Ejemplos](#22-Ejemplos)
   
- [3. Tablas de Consulta (LUTs)](#3-Tablas-de-Consulta-LUTs)
   - [3.1. Explicación](#31-Explicación)
   - [3.2. Ejemplos](#32-Ejemplos)

- [4. Convolución](#4-Convolución)
   - [4.1. Explicación](#41-Explicación)
   - [4.2. Ejemplos](#42-Ejemplos)

- [5. Correlación Cruzada Normalizada](#5-Correlación-Cruzada-Normalizada)
   - [5.1. Explicación](#51-Explicación)
   - [5.2. Proceso](#52-Proceso)
   - [5.3. Ejemplos](#53-Ejemplos)

- [6. Transformada de Fourier](#6-Transformada-de-Fourier)
   - [6.1. Explicación](#61-Explicación)
   - [6.2. Propiedades](#62-Propiedades)
   - [6.3. Transformada de Fourier Rápida](#63-Transformada-de-Fourier-Rápida)



# 1. Relaciones entre Píxeles
## 1.1. Explicación
Queremos obtener un objeto entero. Para ello miremos el valor de grises de un pixel y obtendremos tanto ese pixel como los pixeles del alrededor que tengan un valor de gris parecido. Esto solo es para explicar como se llaman dichas relaciones. En un futuro se utilizarán.

## 1.2. Tipos
- Vecindad: Un pixel es vecino de otro si se encuentra al lado de la siguiente forma:
   - 4-Vecinos

<p align="center">
   <img height="100" alt="image" src="https://github.com/user-attachments/assets/75a81a57-39ee-4564-849e-447a994656e8" />
</p>

   - 8-Vecinos

<p align="center">
   <img height="100" alt="image" src="https://github.com/user-attachments/assets/033289b2-67c6-4966-932e-19472bb7b6fb" />
</p>

- Distancia
   - Euclídea (Norma " $L_2$ ").

<p align="center">
  <img width="139" height="142" alt="image" src="https://github.com/user-attachments/assets/e204dd17-7d97-4e5c-92ea-72efafb03819" />
  <img width="631" height="55" alt="image" src="https://github.com/user-attachments/assets/a736118b-09f8-44f2-b4e6-e2c6d7b2eb28" />
</p>

   - Manhattan (Normal " $L_1$ ").

<p align="center">
   <img width="139" height="142" alt="image" src="https://github.com/user-attachments/assets/5cd2064b-47b8-4fc8-81ec-68424b65d363" />
   <img width="548" height="54" alt="image" src="https://github.com/user-attachments/assets/96d2fb18-3115-4272-b5ce-4e016380f8d7" />
</p>

   - Distancia 8 (Normal " $L_{\infty}$ ")

<p align="center">
   <img width="139" height="142" alt="image" src="https://github.com/user-attachments/assets/f669a028-01f1-49d2-bd17-af07ddb73246" />
   <img width="570" height="54" alt="image" src="https://github.com/user-attachments/assets/bb75fe3b-c452-46c3-b7a1-174a39a38611" />
</p>


- Conectividad: A parte de ser vecinos, dos pixeles están conectados si tienen un valor de gris parecido. Los pixeles en azul son aquellos que tienen un valor de gris parecido.

<p align="center">
   <img height="200" alt="image" src="https://github.com/user-attachments/assets/a38926e8-6b7b-4e8c-affd-ce850cfb4293" />
</p>

- Distancia: La distancia de un pixel y otro depende de si son 4-vecinos u 8-vecinos.

<p align="center">
   <img height="225" alt="image" src="https://github.com/user-attachments/assets/dddf547e-8d1b-4651-a09f-310483d575a6" />
</p>

# 2. Histogramas
## 2.1. Explicación

Se obtienen todos los valores de gris de la imagen y se ponen en una gráfica. En el eje " $x$ " se encuentra el nivel de gris y en el eje " $y$ " se encuentra el número de pixeles que tienen dicho nivel de gris. Normalmente normalizamos el histograma dividiéndolo entre el número total de píxeles (formando una función de densidad de probabilidad).

## 2.2. Ejemplos

<p align="center">
   <img height="100" alt="image" src="https://github.com/user-attachments/assets/87de2c20-593a-48f8-9069-0c0878b35785" />
</p>

# 3. Tablas de Consulta (LUTs)
## 3.1. Explicación
Una "LUT" es una función. A cada pixel (dependiendo de su nivel de gris) se le asigna una transformación dándole otro nivel de gris.

## 3.2. Ejemplos

<p align="center">
   <img height="300" alt="image" src="https://github.com/user-attachments/assets/94fd790e-6a59-4f76-b894-5075fa1f5765" />
</p>

# 4. Convolución
## 4.1. Explicación
En procesamiento de imágenes, se hace la convolución entre la imagen y una máscara (matriz de un tamaño menor a la imagen y con valores arbitrarios). Sobre cada píxel se pondrá el centro de la máscara. Finalmente, tanto el valor de ese píxel como el de los alrededores, se multiplicará por el valor correspondido por la máscara y se sumarán formando el nuevo pixel. La convolución es un operador matemático que transforma dos funciones f y g en una tercera función que en cierto sentido representa la magnitud en la que se superponen f y una versión trasladada e invertida de g.

## 4.2. Ejemplos
- Imagen más Borrosa (media).

<p align="center">
   <img height="175" alt="image" src="https://github.com/user-attachments/assets/e9f88a32-8400-4c32-aab3-85c0fc3d616d" />
</p>

- Cambios Bruscos de un Pixel a otro en el eje " $y$ ".

<p align="center">
   <img height="174" alt="image" src="https://github.com/user-attachments/assets/7bec929e-7c24-4178-b028-fbdbe64f4c70" />
</p>

# 5. Correlación Cruzada Normalizada
## 5.1. Explicación
Buscamos la similitud entre 2 imágenes (un patrón/ventana y una imagen completa). Para ello se podría restar el patrón (ventana) sobre ventanas de la imagen global y ver cual es la que más se acerca a 0. Sin embargo, esto es invariante al brillo y al contraste.

Debido a esto, se utilizará la correlación cruzada: Deslizas el patrón sobre la imagen y calculas el producto escalar de los elementos de ambas ventanas (se ponen las filas de cada ventana seguidas formando un vector). Si el producto escalar es alto, las ventanas son similares. Para ello se utilizará la convolución. 

La correlación cruzada tampoco es invariante ni al brillo ni al contraste. Por ello se podrá en cada imagen el brillo medio a 0 (media 0) y la varianza a 1 (normalizar contraste). 

<p align="center">
   <img height="150" alt="image" src="https://github.com/user-attachments/assets/c6e966b5-13da-44f1-9274-11bf59f9f6b8" />
</p>

Se utilizará el producto escalar obteniendo el coseno del ángulo entre ambos vectores. Debido a eso, los valores dados estarán entre -1 y 1 (para evitar respuestas elevadas). 

NCC no es invariante ni a escala ni a rotación.

## 5.2. Proceso
La máscara utilizada será la imagen que queremos encontrar. Se irá colocando dicha máscara sobre todos los pixeles de la imagen completa. Al aplicar convolución, cuando todos los pixeles de la máscara sean iguales a todos los pixeles de la imagen completa donde se sitúa la máscara, a ese pixel se le dará un valor de 1 (significando que son iguales).

## 5.3. Ejemplos
Buscamos la segunda imagen en la primera imagen:

<p align="center">
   <img height="250" alt="image" src="https://github.com/user-attachments/assets/a1974fb5-b5b8-4479-981e-7177e8de7973" />
</p>

# 6. Transformada de Fourier
## 6.1. Explicación
Pasamos del dominio temporal/espacial al dominio frecuencial. Tendremos en un principio una onda formada por otras ondas con distintas amplitudes y frecuencias. Con la transformada de Fourier obtendremos las amplitudes, las frecuencias y los desfases de dichas ondas.

## 6.2. Propiedades
- Separabilidad: Para el cálculo de la transformada 2D, se puede realizar la transformada en uno de los ejes y después en otro.

- Translación:

<p align="center">
   <img height="150" alt="image" src="https://github.com/user-attachments/assets/fbbae6c2-97a5-4dc3-907f-c07744fa6288" />
</p>

- Periodicidad y Simetría: Siendo " $𝑀$ " y " $𝑁$ " el número de valores de ambos ejes.

<p align="center">
   <img height="50" alt="image" src="https://github.com/user-attachments/assets/70f95b2a-fe32-4e66-8eda-9c272220655e" />
</p>

- Rotación: Una rotación en la transformada es también producida en la imagen normal.

<p align="center">
   <img height="50" alt="image" src="https://github.com/user-attachments/assets/c83dd8a0-aa00-4475-9be2-ce36c73efb3e" />
</p>

- Linealidad:

<p align="center">
   <img height="50" alt="image" src="https://github.com/user-attachments/assets/41c66bbe-ff2d-400c-a191-c0387adf67d9" />
</p>

- Convolución:

<p align="center">
   <img height="150" alt="image" src="https://github.com/user-attachments/assets/65263b4e-0eee-4895-9fb1-687d8525703c" />
</p>

- Laplaciano: Se emplea para delimitar los bordes de una imagen.

<p align="center">
   <img height="75" alt="image" src="https://github.com/user-attachments/assets/5dd5de26-15b3-49b0-8ff4-7dc6ee0ed9a0" />
</p>

## 6.3. Transformada de Fourier Rápida
Sabiendo que:

<p align="center">
   <img height="50" alt="image" src="https://github.com/user-attachments/assets/c9692fae-fdf5-469d-b059-52cd24cb406d" />
</p>


# [Bibliografía](https://github.com/user-attachments/files/25094119/Tema.4.pdf)
