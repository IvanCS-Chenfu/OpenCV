# Índice

- [1. Descriptores](#1-Descriptores)
   - [1.1. Explicación](#11-Explicación)

- [2. Esquemas de Representación](#2-Esquemas-de-Representación)
   - [2.1. Código Cadena](#21-Código-Cadena)
   - [2.2. Aproximación Poligonal](#22-Aproximación-Poligonal)
   - [2.3. Signatura](#23-Signatura)
   - [2.4. Esqueleto de una Región](#24-Esqueleto-de-una-Región)

- [3. Descriptores de Frontera](#3-Descriptores-de-Frontera)
   - [3.1. Simples](#31-Simples)
   - [3.2. Número de Contorno](#32-Número-de-Contorno)
   - [3.3. Descriptores de Fourier](#33-Descriptores-de-Fourier)
   - [3.4. Momentos Estadísticos](#34-Momentos-Estadísticos)

- [4. Descriptores de Región](#4-Descriptores-de-Región)
   - [4.1. Simples](#41-Simples)
   - [4.2. Momentos Estadísticos](#42-Momentos-Estadísticos)
   - [4.3. Descriptores Topológicos](#43-Descriptores-Topológicos)
   - [4.4. Transformada de Hotelling](#44-Transformada-de-Hotelling)
   - [4.5. Textura](#45-Textura)

- [5. Opeadores Morfológicos](#5-Opeadores-Morfológicos)
   - [5.1. Explicación](#51-Explicación)
   - [5.2. Hit or Miss](#52-Hit-or-Miss)
   - [5.3. Erosión](#53-Erosión)
   - [5.4. Dilatación](#54-Dilatación)
   - [5.5. Apertura y Cierre](#55-Apertura-y-Cierre)

- [6. Algoritmos Morfológicos](#6-Algoritmos-Morfológicos)
   - [6.1. Esqueleto](#61-Esqueleto)
   - [6.2. Adelgazamiento](#62-Adelgazamiento)
   - [6.3. Puntos Finales](#63-Puntos-Finales)
   - [6.4. Poda](#64-Poda)
   - [6.5 Cerco Convexo](#65-Cerco-Convexo)

# 1. Descriptores
## 1.1. Explicación

Tras segmentar el objeto, queremos saber qué tipo de objeto es, (una “A”, una “B”, una cometa, un coche, el cielo…). Cada objeto tiene unas características propias llamadas descriptores, estos se guardarán en una tabla. Una vez segmentado el objeto deberemos calcular sus descriptores y compararlos con los de la tabla para saber qué tipo de objeto es.

<p align="center">
   <img height="325" alt="image" src="https://github.com/user-attachments/assets/db5306f0-a5ed-42f0-9620-809d3b5a8131" />
</p>

Estos descriptores deben ser invariantes al tamaño, orientación y posición.

# 2. Esquemas de Representación
## 2.1. Código Cadena
Empezando en un punto de la frontera del objeto, empezamos a escribir números dependiendo de donde esté el siguiente píxel de la frontera.

<p align="center">
   <img height="175" alt="image" src="https://github.com/user-attachments/assets/2b3fb718-de6a-4165-9426-843f8b4ce3fe" />
</p>

Como el contorno puede ser muy variable y muy grande, se realiza un muestreo del mismo.

<p align="center">
   <img height="250" alt="image" src="https://github.com/user-attachments/assets/bddada5a-030b-400a-a90c-98af2a74142d" />
</p>

Como el código depende de cuál es el primer punto elegido del contorno, este código irá girando hasta elegir el código de menor módulo

<p align="center">
   <img height="50" alt="image" src="https://github.com/user-attachments/assets/7d6dd805-b0b0-40a1-9813-121e1ec4983e" />
</p>

Como el código depende de la orientación del objeto, cada número del código serán el número de pasos en sentido antihorario de ese número al siguiente.

<p align="center">
   <img height="150" alt="image" src="https://github.com/user-attachments/assets/22b5f5ed-2d82-4c56-ac17-691e1239dd46" />
</p>

## 2.2. Aproximación Poligonal
### 2.2.1. Perímetro Mínimo
Los posibles descriptores pueden ser el número de segmentos, el cociente entre el segmento mayor y el menor...

Se obtienen todos los puntos equina del objeto. Los puntos dependerán del tamaño de la rejilla utilizada. Los convexos pertenecen a la frontera del objeto y los cóncavos están fuera. Se realizarán los siguientes pasos.

<p align="center">
   <img height="300" alt="image" src="https://github.com/user-attachments/assets/df5eb118-808e-4581-9a9a-5fc23d1d2634" />
</p>

### 2.2.2. Fusión de Puntos
Coges 3 puntos, creas una recta aproximada por mínimos cuadrados. Si el error desde cada punto a la recta es menor a un umbral, se añade otro punto y se realiza lo mismo. En el momento en el que el error de algún punto supere el umbral, se coge ese punto y se empieza otra vez a realizar otra línea recta con los 2 puntos siguientes. 

<p align="center">
   <img height="175" alt="image" src="https://github.com/user-attachments/assets/8f4c729a-ab41-4a94-af18-3710daf0aaef" />
</p>

### 2.2.3. División de Segmentos

De una frontera se obtienen 2 puntos, el más alejado del centroide y el más alejado de ese primer punto. Tanto por arriba como por abajo se mide la distancia de los píxeles de la frontera a la recta. Si el máximo de esas distancias supera un umbral, se considerará un punto del polígono. Así se hará hasta que ninguna de las distancias medidas respecto a las rectas del polígono supere el umbral.

<p align="center">
   <img height="175" alt="image" src="https://github.com/user-attachments/assets/c4bd1342-f8f7-4063-be3f-848137d7ad3c" />
</p>

### 2.2.4. División y Fusión
Se aproxima el contorno mediante el método de división de segmentos y reajusta esos segmentos mediante la fusión de los puntos que dieron origen en el proceso de división.

## 2.3. Signatura
Desde el centroide de la figura calculamos la distancia al punto más alejado. Iremos avanzando punto a punto e iremos calculando las distancias al centroide dependiendo del ángulo que formen desde la distancia inicial. La función se dividirá entre el valor máximo (con el fin de que sea independiente del tamaño).

<p align="center">
   <img height="275" alt="image" src="https://github.com/user-attachments/assets/19567464-1c70-440d-b3cc-33a879466906" />
</p>

Problema: Si la figura tiene muchas concavidades la función puede estar multivaluada. Por ello utilizaremos el cerco convexo.

<p align="center">
   <img height="200" alt="image" src="https://github.com/user-attachments/assets/c6ef9681-2fd3-45a8-97ce-569a18a75dfa" />
</p>

## 2.4. Esqueleto de una Región
### 2.4.1. MAT (Medial Axis Transformation)
A todos los pixeles que forman la figura se le calcula la distancia mínima a cada píxel de la frontera. Si un píxel tiene la misma distancia a 2 píxeles diferentes de la frontera y esta es la distancia mínima, el píxel pertenece al esqueleto de la región.

<p align="center">
   <img height="225" alt="image" src="https://github.com/user-attachments/assets/769ba80d-2d18-45b7-b5fc-d7947116f419" />
</p>

### 2.4.2. Algoritmo de Zhan y Suen
Utilizando una imagen binarizada, a cada píxel de la región se realizan 2 test sobre cada píxel que se encuentre a "1".

<p align="center">
   <img height="200" alt="image" src="https://github.com/user-attachments/assets/0de1d335-7ed3-44f3-8777-4d9914f408f7" />
</p>

Los tests son los siguientes:
- N(pi): Numero de pixeles con valor "1" en los 8 vecinos
- S(pi): Yendo en orden, numero de transiciones 0, entonces, 1.

<p align="center">
   <img height="100" alt="image" src="https://github.com/user-attachments/assets/12423bdf-793f-414b-98b0-93d0a9cce812" />
</p>

# 3. Descriptores de Frontera
## 3.1. Simples
- Perímetro: utilizando el código cadena, se puede aproximar el perímetro. Si utilizamos 8 vecinos en el código cadena, los diagonales cuentan $\sqrt{2}$ .

- Diámetro: La distancia máxima de entre dos puntos del contorno. Para ello hay que calcular la distancia de cada pixel con todos los demás.

- Excentricidad: El eje menor es aquel perpendicular al mayor. El cociente entre el menor y el mayor es la excentricidad.

## 3.2. Número de Contorno
Es exactamente igual que el código cadena explicado anteriormente. Para saber como de grande será la rejilla a utilizar (para utilizar más o menos dígitos en el código cadena) se utilizará aquella rejilla que haga que la excentricidad de la nueva figura sea aproximada a la de la figura original. El orden de la rejilla se calcula multiplicando por dos la suma de filas y columnas de la rejilla

<p align="center">
   <img height="425" alt="image" src="https://github.com/user-attachments/assets/7a792f0d-9076-43d8-bafd-b3b1f1c60331" />
</p>

## 3.3. Descriptores de Fourier
Cada punto del contorno se puede considerar como un numero imaginario.

<p align="center">
   <img height="425" alt="image" src="https://github.com/user-attachments/assets/9262b23a-5b80-46cc-b1fb-93bad4725f75" />
</p>

El valor de "N/P" que haga que la figura se asemeje bastante a la original será el descriptor.

Teniendo la distancia de todos los puntos respecto al centroide del objeto, calculamos la media y hacemos un círculo cuyo radio sea esa distancia. Todo lo que salga de ese círculo y entre es debido a las altas frecuencias. Viendo la transformada de Fourier se pueden ver. Un descriptor pueden ser los módulos de los "n" primeros armónicos de la señal.

## 3.4. Momentos Estadísticos
Utilizando la signatura, dividimos cada distancia entre la suma de todas las distancias para hacer una función de densidad de probabilidad. Hacemos que la signatura, en vez de depender del ángulo, dependa del número de píxel (i = 0, 1, 2, … , k). Si " $v_i$ " es la distancia del
píxel "i" del contorno, los descriptores que se pueden obtener son los momentos " $\mu_n$ "

<p align="center">
   <img height="75" alt="image" src="https://github.com/user-attachments/assets/df7484f0-e92e-40ad-896c-54cf6253702c" />
</p>

# 4. Descriptores de Región
## 4.1. Simples

- Área: Número de píxeles de la región.

- Compactación: $\frac{perímetro^2}{Área}$

- Estadísticos Básicos: Nivel de gris medio, mediana, máximo y mínimo, número de píxeles por encima y por debajo de la media...

## 4.2. Momentos Estadísticos
Seguir los siguientes pasos:

<p align="center">
   <img height="450" alt="image" src="https://github.com/user-attachments/assets/a4146339-0987-4dce-acff-bbe7fbc086e8" />
</p>

## 4.3. Descriptores Topológicos
Son todas las propiedades que no se ven afectadas por deformaciones de la región. Por ejemplo, el número de Euler, siendo este la resta entre el número de regiones conectadas menos el número de huecos.

<p align="center">
   <img height="300" alt="image" src="https://github.com/user-attachments/assets/2b7b5d3d-bc5f-451d-9ac7-df671c3fb481" />
</p>

## 4.4. Transformada de Hotelling

- Tenemos todos los puntos de la región.

<p align="center">
   <img height="30" alt="image" src="https://github.com/user-attachments/assets/6a9cfb83-de74-4f6e-b4d3-c26074e2540b" />
</p>

- Calculamos la media y se la restamos a cada punto.

<p align="center">
   <img height="100" alt="image" src="https://github.com/user-attachments/assets/bb4c2cc4-2d45-4f9a-a695-70b29d769b73" />
</p>

- Creamos la matriz de covarianza.

<p align="center">
   <img height="225" alt="image" src="https://github.com/user-attachments/assets/dd5dadd1-b2e8-4303-a5e1-1cf9561158e0" />
</p>

- Calculamos los autovalores y autovectores de dicha matriz de covarianza.

<p align="center">
   <img height="30" alt="image" src="https://github.com/user-attachments/assets/efa4735f-b785-477c-b24a-f14a852b6894" />
</p>

- La excentricidad del objeto (cociente entre autovalores) puede ser un descriptor.

<p align="center">
   <img height="50" alt="image" src="https://github.com/user-attachments/assets/581f8398-2ee4-4408-a0ee-a4f40ab0ea61" />
</p>

- Podremos girar el objeto para ponerlo paralelo a los ejes.

<p align="center">
   <img height="130" alt="image" src="https://github.com/user-attachments/assets/97854694-8087-40be-8f27-5c7a015cec19" />
</p>

## 4.5. Textura
### 4.5.1. Histograma
Siendo " $z_i$ " el valor de gris del punto $(x_i, y_i)$ , "m" la media de gris de la región y " $p(z_i)$ " el valor de la función de densidad de probabilidad hecha con el histograma:

<p align="center">
   <img height="200" alt="image" src="https://github.com/user-attachments/assets/cc6a6cdf-32d6-42c1-96d1-2756ab220446" />
</p>

### 4.5.2. Posición
Se crea una matriz en la cual cada elemento " $a_{ij}$ " indica cuantos pixeles con valor de gris "i" tienen en su posición abajoderecha un píxel con valor de gris "j".

<p align="center">
   <img height="175" alt="image" src="https://github.com/user-attachments/assets/755aa527-a5c9-4ccb-9ad5-ca63ae5eec43" />
</p>

Con los elementos de esta matriz calcularemos la probabilidad de que un píxel de nivel de gris "i" tenga abajo-derecha un píxel de valor de gris "j".

<p align="center">
   <img height="85" alt="image" src="https://github.com/user-attachments/assets/5d7e2d04-6be8-460c-ad5f-59d465f26497" />
</p>

Con esto se pueden calcular todos los descriptores siguientes:

<p align="center">
   <img height="350" alt="image" src="https://github.com/user-attachments/assets/b8d727de-a61a-478b-98d6-4710c8c033f1" />
</p>

### 4.5.3. Espectral
El espectro se puede expresar en polares por lo que:

<p align="center">
   <img height="150" alt="image" src="https://github.com/user-attachments/assets/4ba530e9-aa0a-4282-b4a5-164ee6032460" />
</p>

Esta función bidimensional se divide entre 2 funciones unidimensionales.

Estas funciones son módulo → ángulo y módulo → radio.

<p align="center">
   <img height="450" alt="image" src="https://github.com/user-attachments/assets/03d58df8-0ef5-465c-aaa4-480065f43dcb" />
</p>

# 5. Opeadores Morfológicos
## 5.1. Explicación
Teniendo una imagen binarizada (en los ejemplos se verá en negro la figura) le aplicaremos una “máscara” la cual hará cosas diferentes dependiendo del método. La máscara tendrá la forma que quiera y estará compuesta por unos (negro en los ejemplos) y ceros (blancos en los
ejemplos). En los recuadros azules:

- $B_x^1 \in X$ : Si los pixeles a "1" en la máscara coinciden con los pixeles a "1" en la imagen. En erosión y en dilatación debería poner esto en vez de " $B_x$ ".

- $B_x^2 \in X^C$ : Si los pixeles a "0" en la máscara coinciden con los pixeles a "0" en la imagen.

## 5.2. Hit or Miss
Una de las celdas de la máscara será la principal. Esta celda se pondrá sobre cada píxel de la imagen. Si todos los bits de la máscara coinciden con todos los bits de la imagen sobre los que están colocados, la celda donde se encuentra la celda principal de la máscara se marcará.

<p align="center">
   <img height="400" alt="image" src="https://github.com/user-attachments/assets/2bdbaceb-f4a0-4ec0-bd77-2912bcdeb3e3" />
</p>

## 5.3. Erosión
Si en la máscara hay un bloque blanco, da igual que bloque haya en la imagen, pero si hay un bloque negro, tiene que haber un bloque negro
(tienen que coincidir todas las celdas a "1" de la máscara y de la imagen). Si cumple eso, se marcará esa celda en la nueva imagen. En la imagen derecha, han hecho algo raro con los colores (el objeto inicial y la máscara tiene en blanco los bits a 1, pero la solución tiene en negro los bits a 1).

<p align="center">
   <img height="225" alt="image" src="https://github.com/user-attachments/assets/bfa3ce80-4b73-4f1d-bb6d-00466a8f0a53" />
</p>

## 5.4. Dilatación
Si al menos una celda a “1” de la máscara coincide con una celda a "1" de la imagen, se pone ese bit a "1".

<p align="center">
   <img height="225" alt="image" src="https://github.com/user-attachments/assets/c0be7004-d2bf-4435-949f-d3450b84b7b1" />
</p>

## 5.5. Apertura y Cierre
La apertura es una dilatación después de una erosión y el cierre lo contrario.

<p align="center">
   <img height="475" alt="image" src="https://github.com/user-attachments/assets/a7310fa9-405d-430f-846b-d3bd7563a78f" />
</p>

# 6. Algoritmos Morfológicos
## 6.1. Esqueleto
Se le harán "n" erosiones a la figura inicial. " $n_{máx}$ " es aquella la cual hace desaparecer la figura. A la erosión se le hace una apertura. Se resta la erosión sin apertura y la erosión con apertura. Finalmente se suma todo lo que ha quedado desde el primer "n" hasta " $n_{máx}$ ". 

Siempre se utilizará la misma máscara. 

<p align="center">
   <img height="60" alt="image" src="https://github.com/user-attachments/assets/485c2bb3-3f7c-4f6a-b30c-3b6415332b4d" />
</p>

<p align="center">
   <img height="85" alt="image" src="https://github.com/user-attachments/assets/fc1a0942-afe0-4c56-bdce-751e6e7d8185" />
</p>

Utilizando el esqueleto se pueden hacer " $n_{máx}$ " dilataciones para obtener la figura inicial.

<p align="center">
   <img height="400" alt="image" src="https://github.com/user-attachments/assets/1d67d462-a45f-4897-a268-fdf41626187a" />
</p>

## 6.2. Adelgazamiento
Se utilizarán 8 máscaras y utilizando el operador "Hit or Miss", cuando alguna de las máscaras coincida completamente con la imagen, esa celda se convertirá en "0".

<p align="center">
   <img height="400" alt="image" src="https://github.com/user-attachments/assets/065d97b4-2f61-4cf4-b166-c59bc4566876" />
</p>

## 6.3. Puntos Finales

A cada celda a "1" de la figura se le hace un "hit or miss" con 8 máscaras. Con que solo una de ellas acierte (solo será en caso de que sea un extremo), se mantendrá.

<p align="center">
   <img height="225" alt="image" src="https://github.com/user-attachments/assets/206f160e-0619-4c8e-964a-166b50ed188f" />
</p>

## 6.4. Poda
- Creamos " $X_1$ " haciendo 3 adelgazamientos de "X" pero con las máscaras " $E^n$ ".

<p align="center">
   <img height="50" alt="image" src="https://github.com/user-attachments/assets/f0056bd4-1b99-4332-95c8-08bfb7baf4fe" />
</p>

- Obtenemos los puntos finales:

<p align="center">
   <img height="60" alt="image" src="https://github.com/user-attachments/assets/4ccb16af-6df7-45c2-b99c-9fd9229f7339" />
</p>

- Creamos " $X_3$ " haciendo tres dilataciones de los puntos finales con una matriz 3x3 de unos y haciendo la intersección de lo que nos ha dado con la figura inicial.

<p align="center">
   <img height="40" alt="image" src="https://github.com/user-attachments/assets/05b06155-f1b7-4ec7-8f45-2a15a0be4789" />
</p>

- Finalmente unimos " $X_3$ " y " $X_1$ "

<p align="center">
   <img height="300" alt="image" src="https://github.com/user-attachments/assets/9015c413-8d16-48fa-b6bd-48c24c6a1d8d" />
</p>

## 6.5. Cerco Convexo

Haciendo operaciones “hit or miss” con las máscaras siguientes y añadiendo lo obtenido a la figura inicial. Esta operación se repetirá con una máscara hasta que la figura no varíe más. En ese momento se pasará a la siguiente máscara.

<p align="center">
   <img height="500" alt="image" src="https://github.com/user-attachments/assets/1ddc1baa-f7fc-4236-ba9f-ae9fc7702b80" />
</p>

Para mejorar el resultado se limita el crecimiento a las coordenadas máximas y mínimas de la figura inicial.

# [Bibliografía](https://github.com/user-attachments/files/25096269/Tema.7.pdf)
