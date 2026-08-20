# Índice
- [1. Introducción](#1-Introducción)
- [2. Detector de Harris](#2-Detector-de-Harris)
- [3. Operador KLT](#3-Operador-KLT)
- [4. SIFT](#4-SIFT)
- [5. SURF](#5-SURF)
- [6. FAST Corner](#6-FAST-Corner)
- [7. BRIEF](#7-BRIEF)
- [8. ORB](#8-ORB)
- [9. Emparejamiento](#9-Emparejamiento)
- [10. Estéreo](#10-Estéreo)

# 1. Introducción
Los keypoints son puntos clave de la imágen (esquinas, blobs...). No solo es necesario saber donde estan (Detección) si no también describirlos (cómo es su entorno) para poder relacionarlos. Estas descripciones deberían ser invariantes.

<p align="center">
   <img height="125" alt="image" src="https://github.com/user-attachments/assets/5184d707-6eba-4c6c-beb4-637ddf9e7e26" />
</p>

En las predicciones, como cualquier predicción, tiene su matriz de confusión, es decir, existen falsos positivos (puntos detectados como keypoints que no son keypoints) y falsos negativos (puntos keypoints no detectados).

Los descriptores debern ser invariantes a la iluminación (brillo y contraste) y al punto de vista (escala, rotación, distorsión...). También deben ser eficientes.


# 2. Detector de Harris

El detector de harris es un detector de keypoints (aunque no los describe). Es simple, eficiente y robusto al ruido. Aunque es invariante a la rotación y al brillo, no lo es en cuanto a la escala.

Harris utiliza ventana "W" para saber si es una región plana (zona uniforme, al desplazar la ventana a penas cambia la intensidad), un borde (al desplazarla sobre un eje, cambia mucho la intensidad pero en el otro eje no), o una esquina (hay cambio fuerte en ambas direcciones).

<p align="center">
  <img height="250" alt="image" src="https://github.com/user-attachments/assets/e8d6fdde-6548-4b78-abb7-5089ffc588df" />
</p>

Este "error" entre al desplazar la ventana $(\Delta x, \Delta y)$ se obtiene:

<p align="center">
   <img width="782" height="177" alt="image" src="https://github.com/user-attachments/assets/a801076f-074a-417e-b9e9-83b1d93b8a56" />
</p>

Esta ecuación se puede aproximar por taylor quedando lo siguiente:

<p align="center">
   <img height="75" alt="image" src="https://github.com/user-attachments/assets/b94b801d-4431-450e-850e-6dd077f619fe" />
   <img height="75" alt="image" src="https://github.com/user-attachments/assets/282d6e9e-982c-4b35-adb6-2f6a14a48f18" />
</p>

Observando la matriz "M" se puede ver si la superficie es plana, si es un borde o si es una esquina:

<p align="center">
   <img height="125" alt="image" src="https://github.com/user-attachments/assets/b861426b-da60-48f9-bbbd-2d6ea70aae6c" />
   <img height="125" alt="image" src="https://github.com/user-attachments/assets/2368f8ac-7c54-400c-b063-036ff6bb085b" />
</p>

Para facilitarlo, se puede diagonalizar "M" obteniendo:

<p align="center">
   <img height="75" alt="image" src="https://github.com/user-attachments/assets/f4ee7732-98a3-467f-b884-79ca464dfd04" />
   <img height="400" alt="image" src="https://github.com/user-attachments/assets/b080b4de-8ed7-440c-84f9-1a16ecf26ecf" />
</p>

Para programarlo, es mejor utilizar una variable que 2, debido a eso:

<p align="center">
   <img height="75" alt="image" src="https://github.com/user-attachments/assets/83cf3335-1ea0-4c1f-ac7c-a7241fa71708" />
   <img height="400" alt="image" src="https://github.com/user-attachments/assets/c32af12b-2213-4632-b867-86c86d9456db" />
</p>

Algebraicamente el determinante y la traza de "D" son iguales que el determinante y al traza de "M". Debido a eso:

<p align="center">
   <img height="80" alt="image" src="https://github.com/user-attachments/assets/8163112b-d344-4753-9b3a-97b0dd31db8a" />
</p>

Finalmente se realiza la supresión de "No Máximos".

Harris no tiene descriptores, debido a eso se utiliza mucho la correlación cruzada con una ventana alrededor de cada keypoint.


# 3. Operador KLT

Está diseñado para encontrar puntos que luego puendan seguirse en una imagen a la siguiente. En un video, entre 2 fotogramas cercanos, los puntos se mueven poco. 

Es parecido a Harris ya que los keypoints usados son aquellos que presentan una variación fuerte de intensidad en dos direcciones.

KLT en vez de usar la función "R", usa diréctamente los autovalores de "M" y acepta un punto si $min(\lambda_1,\lambda_2) > threshold$. Esto obliga a que las dos direcciones sean "buenas".

Usar los autovalores, en vez de usar la aproximación "R", da un mejor comportamiento bajo deformación afín.



# 4. SIFT
## 4.1. Introducción
El algoritmo SIFT (Scale-Invariant Feature Transform) es un algoritmo de detección y descripción de características locales en imágenes.

Detecta puntos clave (keypoints) en una imagen y los describe de manera que sean invariantes a escala, rotación, cambios de iluminación y perspectiva. SIFT detecta blobs (estructuras) en múltiples escalas, no solo esquinas.

SIFT detecta puntos y los describe.

## 4.2. Funcionamiento
1. Crea múltiples versiones suavizadas de la imagen usando filtros Gaussianos. Cada imagen tiene una $\sigma$ mayor.

$$
L(x,y,\sigma) = G(x,y,\sigma) *  I(x,y)
$$

- $\sigma$: controla la escala.
- $G$: es el kernel gaussiano.
- $I$: es la imagen.

2. Cada 8 imágenes filtradas se reduce la resolución de la imagen y se vuelve a repetir formando una pirámida de escalas en la que cada octava tiene la misma resolución (mismo número de píxeles). La última imagen de una octava y la primera de la siguiente son la misma imágen pero cambiando solamente su resolución.

<p align="center">
   <img height="375" alt="image" src="https://github.com/user-attachments/assets/ef9309e9-1cfd-4ae9-b2a2-51636b6c7d9c" />
   <img height="400" alt="image" src="https://github.com/user-attachments/assets/f2d0347e-7a9d-4f5e-a471-6e452eec17c2" />
</p>

3. Para encontrar los blobs, en vez de usar el Laplaciano (costoso), SIFT utiliza la aproximación DoG permitiendo detectar extremos (máximos y mínimos locales).

$$
DoG = L(x,y,\sigma_1) - L(x,y,\sigma_2)
$$

<p align="center">
   <img height="375" alt="image" src="https://github.com/user-attachments/assets/86f0630d-667d-4815-8df9-626902444f47" />
</p>

Cada pixel se compara con 8 vecinos de la misma escala (misma imagen), 9 vecinos de la escala superior ($\sigma$ mayor) y 9 vecinos de la escala inferior ($\sigma$ menor). Total 26 vecinos. Si es extremo, es candidato a keypoint

<p align="center">
   <img height="300" alt="image" src="https://github.com/user-attachments/assets/36d8dbd0-f7dc-493e-87cf-a51e0813d6a1" />
</p>

3. Eliminación de puntos inestables como puntos de bajo contraste y puntos en bordes (utilizando la matriz Hessiana) mejorando la estabilidad y la robusted. Los bordes, al tener solo información en una dirección, son inestables para matching.

4. Asignar la orientación de un entorno. Para ello se emplea el gradiente local (en un entorno) obteniendo bordes, esquinas, texturas, patrones... Se crea un histograma en intervalos de 10º y en cada intervalo (bin) se suma el valor de la magnitud del gradiente (es decir, si un borde está a 15º y la magnitud del gradiente en ese pixel es de 2, se suma 2 al intervalo 10º-20º). Respecto al bin con mayor valor es el que se rota el sistema de referencia local y se calculan los descriptores relativos a dicha orientación.

5. Se toma una región alrededor del keypoint (normalmente de 16 x 16) y se divide en 4 x 4 celdas. En cada subregión se calcula un histograma de 8 orientaciones (4 x 4 x 8 = 128 dimesiones).

<p align="center">
   <img height="200" alt="image" src="https://github.com/user-attachments/assets/ed4994ac-43eb-4544-9809-1fa243430e3e" />
   <img height="200" alt="image" src="https://github.com/user-attachments/assets/55981302-bef5-4fc0-ba8f-8c710c51999b" />
</p>

6. Finalmente el descriptor se normaliza para dar invarianza a la iluminación.

# 5. SURF
## 5.1. Introducción
El algoritmo SURF (Speed-Up Robust Features) es un algoritmo de detección y descripción de características locales en imágenes.

El objetivo es lograr una alternativa más rápida que SIFT manteniendo robustez a escala y rotación.

## 5.2. Funcionamiento
1. En lugar de unsar DoG, se usa la matriz Hessiana

$$
H =
\begin{bmatrix}
L_{xx} & L_{xy} \\
L_{xy} & L_{yy}
\end{bmatrix}
$$

- $L_{xx}$ es la segunda derivada respecto a "X".
- $L_{yy}$ es la segunda derivada respecto a "Y".
- $L_{xy}$ es la derivada mixta (primero sobre uno y luego sobre otro).

El determinante del Hesiano tiene valores muy grandes cuando hay estructuras de esquina o de blob. Es muy estable matemáticamente.

$$
det(H) = L_{xx}*L_{yy} - L_{xy}^2
$$

2. Como las derivadas de una Gaussiana son muy costosas, se utilizan cajas:

<p align="center">
   <img height="350" alt="image" src="https://github.com/user-attachments/assets/dad17718-9268-43ac-9e12-a8bfcd572e9e" />
</p>

3. Se calcula una imagen integral de la imagen actual. Para ello el valor de cada pixel será la suma de todos los pixeles de encima y de la izquerda.

$$
\begin{bmatrix}
1 & 2 & 3 & 4 \\
5 & 6 & 7 & 8 \\
9 & 10 & 11 & 12 \\
13 & 14 & 15 & 16 \\
\end{bmatrix}
$$

$$
\begin{bmatrix}
1 & 3 & 6 & 10 \\
6 & 14 & 24 & 36 \\
15 & 33 & 54 & 78 \\
28 & 60 & 96 & 136 \\
\end{bmatrix}
$$

Esto es útil porque para saber cuanto es la suma de los pixeles de una region cuadrada cualquiera (de la imagen original), solo tienes que realizar el siguiente cálculo de la imagen integral.

$$
S_{region} = BD - AD - BI + AI
$$

Esta ecuación solo se sigue si una esquina no es el (0,0). En ese caso $S_{region} = BD$
 
Por ejemplo: $1 + 2 + 3 + 5 + 6 + 7 = 24$

Por ejemplo: $6 + 7 + 10 + 11 = 54 - 6 - 15 + 1 = 34$

4. Las cajas multiplican una región por un número, por lo que se suma la región con el método de la imagen integral y se multiplica por el número dado por la caja con el fin de crear el hessiano y obtener su determinante.

5. En SIFT se reduce la imagen (pirámide Gaussiana) mientras que en SURF se mantiene la imagen original y se aumenta el tamaño del filtro (más eficiente).

<p align="center">
   <img height="150" alt="image" src="https://github.com/user-attachments/assets/7d23d2fb-ef9f-47de-b89c-a61a525d4236" />
</p>

6. Para conseguir la invarianza en cuanto a rotación, se calcula el "gradiente" de intensidad de dicho pixel utilizando "wavelet Harr" (diferencia entre dos regiones rectangulares).

<p align="center">
   <img height="150" alt="image" src="https://github.com/user-attachments/assets/04a06768-e424-4870-a6f8-5dd536e60b13" />
</p>

Esto da varios vectores "gradiente". Se elegirá la dirección dominante realizando "bins" de 60º y utilizando el módulo de dichos vectores.

7. Para obtener los descriptores se toma una región alrededor del keypoint. Se divide dicha región en 4x4 subregiones y en cada subregión se calculan los sumatorios de $d_x, d_y, |d_x|, |d_y|$. Esto da un vector de (4 x 4 x 4 = 64).

<p align="center">
   <img height="300" alt="image" src="https://github.com/user-attachments/assets/23042d58-26c2-4f74-b626-9ce3169fe60f" />
</p>

# 6. FAST Corner
## 6.1. Introducción
El algoritmo FAST (Features from Accelerated Segment Test) es un algoritmo de detección de esquinas extremadamente rápido.

Es muy útil para tiempo real debido a su bajo coste computacional, su velocidad y a la posibilidad de ejecutarlo en un hardware limitado.

## 6.2. Funcionamiento
1. Se consideran 16 pixeles alrededor de un pixel formando un círculo de radio 3.

<p align="center">
   <img height="250" alt="image" src="https://github.com/user-attachments/assets/497e07f2-f525-43fd-9518-ac92627a1f44" />
</p>

2. Se declara un umbral.

3. Si un número "N" de píxeles conscutivos son más "brillantes" que el pixel del centro más el umbral ( $I(p) + t$ ) se considera esquina (también si son menos "brillantes" que el píxel del centro menos el umbral).

<p align="center">
   <img height="250" alt="image" src="https://github.com/user-attachments/assets/443bb467-8c1b-4dc2-bc10-92cddb9e3b29" />
</p>


# 7. BRIEF
## 7.1. Introducción
El algoritmo BRIEF (Binary Robust Independent Elementary Features) es un descriptor binario el cual se crea extremadamente rápido. Es muy útil para matching.

En SURF y SIFT los descriptores son muy grandes y están hechos de flotantes. Esto es costoso, por lo que BRIEF utiliza comparaciones binarias en lugar de valores continuos.

## 7.2. Funcionamiento
1. Selecciona una ventana alrededor del keypoint (por ejemplo de 31 x 31).

2. Si $p_i$ es el pixel "i", se hacen parejas de pixeles por toda la región. Por ejemplo: $p_1$ con $p_2$, $p_4$ con $p_5$...

3. Se compara la intensidad de cada pareja. Si $I(p_1) > I(p_2)$, entonces obtenemos un 1. En caso contrario un 0.

4. Haciendo "N" comparaciones tenemos un vector de "N" bits con el cual se puede hacer un buen matching utilizando la "Distancia Hamming".

# 8. ORB
## 8.1. Introducción
El algoritmo ORB (Oriented FAST and Rotated BRIEF) es un algoritmo de detección y descripción de características locales en imágenes.

Combina la velocidad de FAST y BRIEF, dando invariancia de rotación a BRIEF. Da una buena aproximación a incariancia a escala y devuelve un descriptor binario eficiente.

## 8.2. Funcionamiento
1. Utiliza FAST para detectar esquinas. Como FAST no es invariante a escala ni orientación, ORB añade mejoras.

2. ORB construye una pirámide de imágenes (va reduciendo la imagen en cada nivel). Esto lo vuelve invariante a escala.

<p align="center">
   <img width="320" height="320" alt="image" src="https://github.com/user-attachments/assets/fc2f8af3-5911-41ec-874c-5a6664bf42a6" />
</p>

3. Utiliza momentos para la orientación.

<p align="center">
   <img width="287" height="100" alt="image" src="https://github.com/user-attachments/assets/8b8870b2-5c61-47f9-9603-e65a29bcb46b" />
   <img width="287" height="100" alt="image" src="https://github.com/user-attachments/assets/90687c09-ecd8-40dd-8c63-63dfa60efbaa" />
   <img width="284" height="50" alt="image" src="https://github.com/user-attachments/assets/04932fc5-db73-494f-afec-b6bbebe2ebed" />
</p>

4. BRIEF no es invariante a la rotación, por lo que lo rota según la orientación obtenida anteriomente.

5. Cada keypoint en ORB tiene los siguientes datos: posición, escala (nivel de la pirámide), orientación, y descriptor binario de 256 bits (normalmente).

# 9. Emparejamiento
## 9.1. Fuerza Bruta
1. Obtiene descriptores y keypoints utilizando algún método (ORB o SIFT)

2. BFMatcher (Brute Force) compara cada descriptor de una imagen con todos los descriptores de la otra imagen.

3. Los descriptores cuya distancia sea menor, serán los matches

4. Finalmente se ordenan los matches por menor distancia. Estos matches tienen los índices de los descriptores de cada imagen (que también corresponden con los índices de los keypoints de cada imagen).

## 9.2. Fuerza Bruta KNN
Es igual al anterior pero en vez de que cada match sea entre 2 descirptores cuyas distancias sean mínimas, cada descriptor tiene 2 matches (los 2 cuyas distancias sean menores). De ambos se comprueba si su distancia es muy diferente. En el caso de que la distancia entre el más cercano y el segundo sean parecidas, ese no será un buen match.

## 9.3. FLANN
En vez de comparar todo con todo, FLANN hace una búsqueda aproximada de vecinos (ANN: Approximate Nearest Neighbors). Es más rápido.

## 9.4. Homografía
A parte de existir un parecido el cuanto a descriptores, los keypoints deberán estar situados geometricamente de forma parecida en ambas imagenes (ya que si en la imagen se repiten patrones en varios sitios, los descriptores pueden ser iguales). Estos keypoints deberán seguir una homografía.

RANSAC (Random Sample Consensus) hace lo siguiente:
1. Elige aleatoriamente 4 matches (mínimo necesario para homografía).
2. Calcula una homografía provisional.
3. Proyecta todos los puntos usando esa H.
4. Mide error de reproyección.
5. Cuenta cuántos puntos cumplen error < threshold.
6. Repite muchas veces.
7. Se queda con la H que tenga más inliers (matches que cumplen la homografía).


# 10. Estéreo
## 10.1. Geometría Epipolar
Cuando realizas 2 imagenes del mismo objeto trasladando la cámara (puede haber rotación pero tiene que haber obligatoriamente traslación).

Cuando tienes dos cámaras (o una cámara movida a otra posición), un punto 3D "X" proyecta a:
- "x" en la imagen izquierda.
- "x'" en la imagen derecha.

La relación geométrica entre "x" y "x'" viene dada por la matriz fundamental:

$$
x'^T * F * x = 0
$$

Esto se llama restricción epipolar.

Si eliges un punto "x" en la imagen izquierda, su correspondencia en la derecha no puede estar en cualquier sitio: debe estar sobre una línea llamada línea epipolar.

$$
l' = F*x
$$

$$
l = F^T*x'
$$

Esto reduce un problema 2D (buscar por toda la imagen) a 1D (buscar sobre una línea). En estéreo es clave para triangulación, disparidad, profundidad, etc.

<p align="center">
   <img height="300" alt="image" src="https://github.com/user-attachments/assets/1bd6b418-1221-464c-abde-a7293beef140" />
</p>

El plano dado por C1 (centro cámara 1), C2 (centro cámara 2) y M (punto tridimensional) es el plano epipolar que corta los planos de las cámaras dando las líneas epipolares.

Se cumple que todas las lineas epipolares pasan por $e_i$ por lo que $F*e_1 = 0$ o $F^T * e_2 = 0$

Obteniendo la matriz de parámetros intrínsecos de la cama (K) podemos obtener la matriz esencial:

$$
E = K^T * F * K
$$

Esta matriz representa la dirección de traslación (no la magnitud) y la rotación de las cámaras.

$$
E = {[t]}_X * R
$$

- ${[t]}_X$: matriz skew-summetric de t
- $R$: matriz de rotación

$$
{x'}^T * E * x = 0
$$

Sabiendo la matriz de rotación y la traslación (con su magnitud que deberás obtener midiendo en la vida real) y la matriz de parámetros intrínsecos podemos obtener estas 2 matrices (3 x 4).

$$
P1 = K * [I | 0]
$$

$$
P2 = K * [R | t]
$$

Con estas dos matrices pondermos crear estas 2 ecuaciones y obtener la distancia resolviendolas.

$$
x_1 = P1 * X
$$

$$
x_2 = P2 * X
$$

Donde:

$$
X =
\begin{bmatrix}
x \\
y \\
z \\
1
\end{bmatrix}
$$


## 10.2. Disparidad
Para obtener una disparidad buena sin mucho problema, las cámaras deben estar paralelas, es decir, las lineas epipolares deben ser horizontales.

Esto da una disparidad de la siguiente manera:

$$
d(x,y) = x_{left}(x,y) - x_{right}(x,y) 
$$

Teniendo la disparidad podemos calcular la distancia de la siguiente manera:

$$
Z(x,y) = \frac{f*B}{d(x,y)}
$$

- $B$: Baseline, es decir, distancia entre cámaras
- $f$: distancia focal

Las cámaras deberán estar calibradas y rectificadas para no complicar los cálculos.


### 10.2.1. Block Matching
En StereoBM para cada pixel "p(x,y)" se da una función de coste que depende de la disparidad (d). Esta función de coste compara las intensidades en un entorno del pixel en cada imagen. Se realizará esto para varios valores de "d" y el valor de "d" cuyo coste sea menor, esa será la disparidad de dicho píxel.

$$
C(d) = \sum_{i,j \in ventana} {|I_{left}(x+i,y+j) - I_{right}(x+i+d,y+j)|}
$$ 

En el código, el valor de ```numDisparities``` debe ser múltiplo de 16, e indica cuantos valores de "d" va a utilizar para la función de coste.

### 10.2.2. Semi Global Block Matching
En StereoSGBM, se intenta minimizar la energía en vez del coste. Esta energía depende del coste y depende de si hay mucha diferencia en la disparidad de dicho pixel (p) con la disparidad de sus vecinos (q). Si la disparidad es igual no habrá penalización, si la disparidad es parecidad habrá un poco de penalización (P1), y si la disparidad es totalmente diferente la penalización será muy alta (P2).

$$
E(D) = \sum {C(p,D_p)} + \sum {penalización(D_p,D_q)}
$$ 

Tiene como parámetros:
- minDisparity: disparidad mínima a considerar
- P1 y P2: Penalizaciones débil y fuerte
- disp12MaxDiff: chequea si la disparidad no es consistente entre ambas direcciones (entonces se marcaría como mala).
- uniquenessRatio: filtra matches ambiguos (obliga a que el mejor coste sea mucho mejor que el segundo)
- speckleWindowSize y speckleRange: elimina pequeñas regiones aisladas de disparidad errónea.
- preFilterCap: Recorte previo de intensidades para estabilizar
