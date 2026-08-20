# Índice

- [1. Segmentación](#1-Segmentación)
   - [1.1. Explicación](#11-Explicación)

- [2. Técnicas de Segmentación](#2-Técnicas-de-Segmentación)
   - [2.1. Basadas en Frontera](#21-Basadas-en-Frontera)
   - [2.2. Mediante Umbralización](#22-Mediante-Umbralización)
   - [2.3. Basadas en Regiones](#23-Basadas-en-Regiones)
   - [2.4. Regiones de Interés](#24-Regiones-de-Interés)


# 1. Segmentación
## 1.1. Explicación

Proceso el cual divide una imagen en regiones cuyos píxeles poseen atributos similares. Nos encontramos ya en el nivel medio del procesamiento de imágenes.

<p align="center">
   <img height="325" alt="image" src="https://github.com/user-attachments/assets/8d66eea6-d538-4b0a-8d90-a7250149156a" />
</p>

# 2. Técnicas de Segmentación
## 2.1. Basadas en Frontera
### 2.1.1. Seguimiento de Contornos
Seleccionamos un punto arbitrario de la frontera.

Incorporamos pixeles a los puntos anteriores: El siguiente píxel tiene que cumplir 3 condiciones de similitud con el píxel anterior.7

- Conectividad: nivel de gris similar (que la resta sea menor a un umbral).

- Vector gradiente: magnitud y dirección similar (que la resta sea menor a un umbral).

Veremos si a 45º, 90º y 135º respecto a la dirección del vector gradiente, el píxel cumple las condiciones de similitud.

<p align="center">
   <img height="250" alt="image" src="https://github.com/user-attachments/assets/761e3bb1-3834-4386-bf5d-3ddd1ace5167" />
</p>

Selección del siguiente punto: Entre los candidatos anteriores se selecciona aquél con el gradiente máximo. Si no hay candidatos, se salta a un píxel más alejado. Finalmente volveremos al paso anterior para obtener el
siguiente píxel.

Si se vuelve al punto inicial o si no se consiguen incorporar nuevos píxeles, se termina el proceso.

### 2.1.2. Transformada de Hough
Útil para obtener rectas y círculos de la imagen.

- Rectas: Sabemos que la ecuación de la recta es la siguiente:

$$
y = a * x + b
$$

Queremos saber cuales son los valores de "a" y "b" de nuestra recta teniendo varios píxeles. Para ello pasaremos cada píxel al espacio de Hough:

$$
b = -a *x + y
$$

Esto hace que cada píxel (x, y) sea una recta en el espacio de Hough. Si varios pixeles pertenecen a la misma recta, las rectas equivalentes en el espacio de Hough cortarán en un punto (a, b).

Lo único malo de esta técnica es que las rectas perpendiculares hacen que "a" tienda a infinito. Por eso se utilizan coordenadas polares.

$$
\rho = x * cos(\theta) + y * sin(\theta).
$$

Ahora, cada punto será representado por una sinusoide en el espacio de Hough. Si varias sinusoides cortan en un mismo punto pertenecen a la misma recta.

<p align="center">
   <img height="250" alt="image" src="https://github.com/user-attachments/assets/387af1b6-ed50-4aec-9e0d-cfcc5697db6b" />
</p>

- Círculos: Sabemos que la ecuación de un círculo es el siguiente:

$$
r^2 = (x-a)^2 + (y-b)^2
$$

Sabiendo el radio de nuestra circunferencia, cada píxel representa un círculo en el espacio de Hough. Todos los círculos que son representados por píxeles pertenecientes a un mismo círculo cortarán en el mismo punto en el espacio de Hough.

- Generalizada: Necesitaremos un prototipo el cual queremos encontrar dentro de una imagen. Crearemos una tabla de parámetros que nos ayude a buscar nuestro prototipo en la imagen. 

Esta tabla representa la dirección del contorno del prototipo con la distancia desde ese punto de contorno al centroide y el ángulo que hace la tangente del contorno con la recta del punto al centroide. 

<p align="center">
   <img height="275" alt="image" src="https://github.com/user-attachments/assets/86dd598d-2427-49a4-95a7-3d6e10f42846" />
</p>

Sabiendo las discontinuidades de nuestra imagen iremos aplicando la tabla a cada píxel y calculando donde estarían los centroides. Si todos los posibles centroides coinciden en el mismo punto, ese contorno es igual al prototipo.


## 2.2. Mediante Umbralización
Conseguir uno o varios umbrales (niveles de grises) que nos permitan clasificar los píxeles en regiones.

<p align="center">
   <img height="300" alt="image" src="https://github.com/user-attachments/assets/1d469086-e2a6-47a2-b7bc-cf78c11f8d95" />
</p>

### 2.2.1. Global Básica
Estimamos un umbral, aplicamos la LUT y calculamos la media de los niveles de grises. Esta será el nuevo umbral. Será un proceso iterativo.

### 2.2.2. Global Óptima (OTSU)
Utilizaremos el histograma como dos funciones de densidad de probabilidad y asumiremos que estas son gaussianas. Determino un umbral arbitrariamente y calculo la desviación típica y la media de ambas gaussianas Intento maximizar lo siguiente.

<p align="center">
   <img height="250" alt="image" src="https://github.com/user-attachments/assets/7820b8ae-b01b-4ebc-af7b-5ba2acfb4179" />
</p>

### 2.2.3. Adaptativa Básica
Divido la imagen en subimágenes y les aplico a cada una el método de umbralización global básico.

<p align="center">
   <img height="200" alt="image" src="https://github.com/user-attachments/assets/0b03465d-44e1-4061-a188-348defa34a99" />
</p>

### 2.2.4. Adaptativa Estadística
Calcula el umbral de un entorno de vecindad mediante la media, la mediana o la media gaussiana. El entorno de vecindad depende del tamaño de la imagen: $2*\frac{tamaño}{16} + 1$ . Se emplea un factor de sensibilidad entre “0” y “1” para determinar cuándo un píxel se debe asignar al fondo o al objeto.

### 2.2.5. Basada en Frontera
Se utilizará tanto el gradiente como la laplaciana. Delimitaremos cuando empieza y cuando acaba un objeto observando sus bordes. Desde que se encuentra el primer borde hasta que se encuentra el final, será el objeto.

Para que se considere primer borde, el valor absoluto del gradiente deberá ser mayor que un umbral y la laplaciana pasar de negativo a positivo o viceversa.

Para que se considere último borde, el valor absoluto del gradiente deberá ser mayor que un umbral y la laplaciana cambiará de signos de forma contraria a como lo hizo en el primer borde. 

<p align="center">
   <img height="325" alt="image" src="https://github.com/user-attachments/assets/f594a0d5-9fb8-4fde-b496-9413df1cd72c" />
</p>

### 2.2.6. Conexión de Regiones
En un principio tendremos una imagen binarizada (el fondo será "0" y los objetos serán "1"). Se irán mirando los píxeles de arriba debajo de izquierda a derecha. De cada píxel "p" se mirará su vecino superior "a" y el de la izquierda "z". 

<p align="center">
   <img height="75" alt="image" src="https://github.com/user-attachments/assets/6a9a5613-0f3a-40f5-9a48-5fea50967e32" />
</p>

- Si "a" y "z" son "0", entonces, se le asigna una etiqueta nueva a "p"

- Si "a" o "z" es "1", entonces, se le asigna su etiqueta a "p"

- Si "a" y "z" son "1" y ambos tienen la misma etiqueta, entonces, se le asigna su etiqueta a "p"

- Si "a" y "z" son "1", pero no tienen la misma etiqueta, entonces, se le asigna a "p" una de las etiquetas y se igualan las etiquetas de "z" y "a".

## 2.3. Basadas en Regiones
### 2.3.1. Crecimiento de Regiones
Se elige una semilla en la imagen y si sus vecinos cumplen unas propiedades de similitud (nivel de gris parecido), se agrupan.

### 2.3.2. División y Fusión de Regiones
Dividimos la imagen en cuatro cuadrantes si hay algún píxel de esa región que no sea muy parecido al resto (que no cumpla una inecuación estadística). Si uniendo dos regiones cercanas, estas cumplen la inecuación, se fusionarán.

Volveremos al primer paso hasta que no sea posible ni fusionar ni dividir. La inecuación estadística puede ser: $\abs{z_j - \mu_j} \le 2 * \sigma_i$ siendo " $z_j$ " el nivel de gris del píxel "j", " $\mu_i$ " la media de la región y " $\sigma_i$ " la desviación típica de la región.

### 2.3.3. Algoritmo de las K-Medias
- Se especifica el valor inicial del vector de medias "m", llamados semillas (por defecto al azar) (estas semillas son niveles de grises para imágenes sin color).

- Cada píxel se agrupa al conjunto con el valor más cercano.

- Se detiene si no se ha cambiado ninguna asignación con respecto a la iteración previa.

- Se actualizan las semillas a un nuevo nivel de gris.

### 2.3.4. Agrupación en SuperPíxeles

Los píxeles son tan pequeños que no tienen tanto significado a nivel de observación. Si los agrupamos en superpíxeles disminuiremos el coste computacional.

Se eligen "N" superpíxeles y se divide la imagen en "N" cuadrados de tamaños iguales $(S \times S)$ . Los centros de cada cuadrado serán los
centros de los superpíxeles. A cada píxel de la imagen se calculará su distancia (tanto de color como espacial) a cada uno de los centros de los superpíxeles).

<p align="center">
   <img height="75" alt="image" src="https://github.com/user-attachments/assets/930ef7e2-d4ed-49d6-8f72-d217e5c31605" />
</p>

"m" es un parámetro de compactación. Cada píxel se unirá con el superpixel cuya distancia al centro sea menor. Finalmente se recalculan los nuevos centros de los superpíxeles, se le da un color medio y se realiza un proceso iterativo con los nuevos centros. Cuando el color no varía mucho, se termina el proceso iterativo.

<p align="center">
   <img height="150" alt="image" src="https://github.com/user-attachments/assets/b7008599-70a0-4830-bfc3-55ee2b63def1" />
</p>

## 2.4. Regiones de Interés
En vez de procesar toda la imagen podremos procesar solo una región. Pueden tener cualquier forma (línea, círculo, rectángulo…)

- ROI absoluta: Misma posición y orientación dentro de la imagen. Es útil cuando los objetos a procesar no cambian su posición de forma significativa.

- ROI relativa: La posición se define respecto a un sistema de referencia variable (un píxel de la imagen).

# [Bibliografía](https://github.com/user-attachments/files/25095730/Tema.6.pdf)
