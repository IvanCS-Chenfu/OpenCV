# Índice

- [1. Elementos que Intervienen en la Formación de Imágenes](#1-Elementos-que-Intervienen-en-la-Formación-de-Imágenes)
   - [1.1. Componentes](#11-Componentes)
   - [1.2. Funcionamiento Global](#12-Funcionamiento-Global)

- [2. Modelo de Lentes](#2-Modelo-de-Lentes)
   - [2.1. Tipos](#21-Tipos)
   - [2.2. Características de la Lente Delgada](#22-Características-de-la-Lente-Delgada)

- [3. Distorsiones](#3-Distorsiones)
   - [3.1. Explicación](#31-Explicación)
   - [3.2. Tipos](#32-Tipos)

- [4. Transformaciones](#4-Transformaciones)
   - [4.1. Básicas](#41-Básicas)
   - [4.2. Perspectiva](#42-Perspectiva)

- [5. Modelo de Cámara](#5-Modelo-de-Cámara)
   - [5.1. Parámetros a Utilizar](#51-Parámetros-a-Utilizar)
   - [5.2. Procedimiento](#52-Procedimiento)

- [6. Calibración de Cámaras](#6-Calibración-de-Cámaras)
   - [6.1. Explicación](#61-Explicación)
   - [6.2. Proceso](#62-Proceso)
   - [6.3. Depende de](#63-Depende-de)
   - [6.4. Características del Calibrado](#64-Características-del-Calibrado)
   - [6.5. Metodo Transformación Lineal Directa](#65-Metodo-Transformación-Lineal-Directa)


# 1. Elementos que Intervienen en la Formación de Imágenes
## 1.1. Componentes
- Lente: Se encarga de concentrar todos los haces de luz que proceden del mismo punto.

- Plano Sensor: Plano en el cual se proyecta la imagen para su obtención analógica o digital (CMOS o CDD).

<p align="center">
   <img height="200" alt="image" src="https://github.com/user-attachments/assets/57dfb80e-a95e-4e0c-9fd9-8ab2b4251232" />
</p>

## 1.2. Funcionamiento Global
- Queremos obtener un punto del espacio para que sea procesado.

- Ese punto está iluminado con una fuente de luz.

- Todos los haces de luz de la fuente chocan con dicho punto y rebotan en todas direcciones.

- La lente intenta obtener la mayoría de esos haces (que están dispersos) y enfocarlos todos en el mismo punto del plano sensor (plano imagen). Si no estuviese la lente, llegarían a distintas partes del sensor haces pertenecientes al mismo punto. También llegarían haces de
distintos puntos (objetos) al mismo punto del sensor produciendo un desenfoque.

- Al sensor le llegan dichos haces de luz, todos con la misma información (características visuales del punto).

# 2. Modelo de Lentes
## 2.1. Tipos
- Pinhole (Agujero de Alfiler): Entre el sensor y el objeto pones otro plano completamente opaco por el cual solo puedan entrar haces de luz por su punto central. Esto hará que al sensor solo le llegue un haz de luz por cada punto del objeto (evitando desenfoques). La distancia focal determina el tamaño de la imagen proyectada.

<p align="center">
   <img height="250" alt="image" src="https://github.com/user-attachments/assets/e7a1cfb1-32eb-4a07-8ecc-f63c9de2ced5" />
   <img height="250" alt="image" src="https://github.com/user-attachments/assets/5e6cfce6-df8f-419f-9b3b-7182ea047a94" />
</p>

   - Ventajas: Modelo simple que enfoca toda la escena.
   - Desventajas: Incide poca luz en el sensor y el diámetro depende de la longitud de onda de la señal.

$$
D_{min} = 2 * \sqrt{f * \lambda}
$$

- Lente Delgada: El grosor de la lente es despreciable respecto a su diámetro. Todos los haces se desvían sobre el plano focal. 

<p align="center">
   <img height="250" alt="image" src="https://github.com/user-attachments/assets/6edb4d08-5ace-42b0-b579-30539c6fc7a7" />
</p>

## 2.2. Características de la Lente Delgada
- Comportamiento de los Haces: Los haces que vienen de un punto e inciden perpendicularmente a la lente, pasan por el foco de la lente. Los haces que atraviesan el centro de la lente siguen su trayectoria.

- Distancia de Enfoque: Para que un objeto se encuentre enfocado, todos los haces que vengan de un mismo punto deben coincidir en el mismo punto del plano imagen. La distancia de enfoque es aquella " $S'$ " en la que todos los haces de un punto coinciden en el plano imagen. Esta distancia depende de la distancia real de la lente al objeto. En el ejemplo siguiente, " $S'$ " es la distancia de enfoque de " $d_1$ ".

<p align="center">
   <img height="300" alt="image" src="https://github.com/user-attachments/assets/8e9dbb34-a307-4509-8456-a533f9c514ae" />
</p>

Es muy complicado que todos los haces incidan en el mismo punto. Sin embargo, no es necesario, ya que al tener un sensor discreto (píxeles), mientras el círculo de confusión esté dentro del mismo píxel, no existirá desenfoque. Debido a esto existe la profundidad de campo.

<p align="center">
   <img height="250" alt="image" src="https://github.com/user-attachments/assets/d8764b2f-d588-41b7-b8cf-b86bfd77361a" />
</p>

- Distancia Focal (zoom): Distancia del punto central de la lente al punto focal. Cuanto más grande sea la distancia focal, más grande se verá el objeto.

<p align="center">
  <img height="200" alt="image" src="https://github.com/user-attachments/assets/f89fa8d0-dbcf-4dc8-b867-d15e8dd736cb" />
  <img height="200" alt="image" src="https://github.com/user-attachments/assets/370a6b54-6c57-43a2-9262-fd96f4954fab" />
</p>

- Profundidad de Campo: una cámara no solo enfoca bien un plano del espacio, también suele enfocar bien cierto espacio anterior y posterior al objeto. La profundidad de campo es el área de delante y de detrás del objeto en el cual se observan las cosas enfocadas. Depende de la distancia de enfoque, la apertura de la lente y del sensor de la cámara.

- Apertura: Determina la cantidad de luz que entra en la cámara (iris). 

<p align="center">
   <img height="175" alt="image" src="https://github.com/user-attachments/assets/370e9d98-086c-4c53-a2f6-7939f2095758" />
</p>

Cuanto mayor sea la apertura, más luz entra (mejora la imagen), pero el círculo de confusión aumenta, purdendo producir desenfoque.

<p align="center"> 
   <img height="315" alt="image" src="https://github.com/user-attachments/assets/dd6cf915-3aa7-45e1-a603-9525f27aad3b" />
</p>


# 3. Distorsiones
## 3.1. Explicación
Variación o alteración que sufre un objeto en el plano imagen cuando sus haces pasan por la lente (un punto de la imagen no se proyecta donde debería).

## 3.2. Tipos
- Desplazamiento del Punto Central:

<p align="center">
   <img height="100" alt="image" src="https://github.com/user-attachments/assets/4f701c71-136e-4516-b4ff-7c87c869e184" />
</p>

- Distorsión Tangencial (parámetros " $q_i$ "):

<p align="center">
   <img height="100" alt="image" src="https://github.com/user-attachments/assets/d8f7f2d6-9e94-46d0-8aa8-1a00824e4a84" />
</p>

- Distorsión Radial (parámetros " $k_i$ "):

<p align="center">
   <img height="100" alt="image" src="https://github.com/user-attachments/assets/66f4f594-26d1-4a4f-b1f6-294639634dde" />
</p>

# 4. Transformaciones
## 4.1. Básicas
Todas ellas se pueden utilizar conjuntas realizando una "transformación compuesta".

- Translación:

<p align="center">
   <img height="200" alt="image" src="https://github.com/user-attachments/assets/11be4746-45f8-4290-bd9d-74a289f86652" />
</p>

- Escalado:

<p align="center">
   <img height="200" alt="image" src="https://github.com/user-attachments/assets/bffe089a-62a6-45fa-9f43-c1a88bc70097" />
</p>

- Rotación:

<p align="center">
   <img height="200" alt="image" src="https://github.com/user-attachments/assets/8b44237e-4883-4227-bc4b-3bb60c96d57e" />
</p>

## 4.2. Perspectiva
### 4.2.1. Normal
Obtener la posición en el plano imagen ( $x'$ , $y'$ ) de un objeto, sabiendo la posición real ( $𝑋$ , $𝑌$ , $𝑍$ ) de dicho objeto. Todos los puntos se toman desde el centro del plano imagen ( $X_c$ , $Y_c$ ). Las ecuaciones se obtienen mediante triángulos semejantes. Las fórmulas se obtienen por triángulos semejantes.

<p align="center">
   <img height="175" alt="image" src="https://github.com/user-attachments/assets/ee9bf63c-b925-4022-ad51-7b33c887f028" />
</p>

Normalmente trabajaremos con matrices para el cálculo de ( $x'$ , $y'$ ). El cálculo matricial se realiza con matrices homogéneas. "k" es una
constante arbitraria (para pasar de distancia a pixeles). 

<p align="center">
   <img height="175" alt="image" src="https://github.com/user-attachments/assets/58e3277b-598c-4553-9c5e-c774788674ed" />
</p>

Finalmente obtendremos las coordenadas cartesianas. " $C(3)$ " no tiene sentido físico (no existe " $z'$ ").

<p align="center">
   <img height="175" alt="image" src="https://github.com/user-attachments/assets/17a3fa46-25fc-4d3a-9109-1c37ce7c99f2" />
</p>


### 4.2.2. Modificada

Como las ecuaciones anteriores no son lineales, cambiaremos el origen de " $Z$ " del centro del plano imagen hasta el centro de la lente.

<p align="center">
   <img height="175" alt="image" src="https://github.com/user-attachments/assets/ce0ace38-1e29-41e6-bbd0-5f60c7a23796" />
</p>

### 4.2.3. Inversa
Utilizaremos las matrices de la transformada perspectiva normal. 

<p align="center">
   <img height="200" alt="image" src="https://github.com/user-attachments/assets/59353636-a4d6-4d8f-b31f-afb93345a759" />
</p>

Despejaríamos " $z$ " en " $W(3)$ " y utilizaríamos dicha " $z$ " en las otras dos ecuaciones.

<p align="center">
   <img height="125" alt="image" src="https://github.com/user-attachments/assets/11ae2443-efbd-465f-a326-f1036ef89517" />
</p>

# 5. Modelo de Cámara
## 5.1. Parámetros a Utilizar
- Número de pixeles del plano imagen en el eje " $x$ " e " $y$ " (número de filas y columnas).

$$
Nc_x
$$

$$
Nc_y
$$

- Número de píxeles muestreados en el eje " $x$ " (de todos los pixeles hay algunos muestreados y otros que no).

$$
Nf_x
$$

- Tamaño desde el centro de cada píxel a uno de sus lados.

$$
d_x
$$

$$
d_y
$$

- Tamaño efectivo (píxeles muestreados) de cada píxel.

$$
dp_x = \frac{Nc_x}{Nf_x}*d_x 
$$

$$
dp_y = d_y
$$

- Tamaño del plano imagen.

$$
Tm_x = Nc_x * d_x
$$

$$
Tm_y = Nc_y * d_y
$$

## 5.2. Procedimiento
- La distancia se mide desde el centro del plano imagen y los píxeles se empiezan a contar desde una de las esquinas.

$$
x'' = -x' + \frac{Tm_x}{2}
$$

$$
y'' = -y' + \frac{Tm_y}{2}
$$

<p align="center">
   <img height="175" alt="image" src="https://github.com/user-attachments/assets/6ef79796-bd08-44e6-96c6-95ab46b5bc58" />
</p>

- Hacemos un escalado pasando de centímetros a píxeles (pero puede haber pixeles decimales).

$$
x''' = \frac{x''}{dp_x}
$$

$$
y''' = \frac{y''}{dp_y}
$$

<p align="center">
   <img height="175" alt="image" src="https://github.com/user-attachments/assets/d8c56abb-2cda-4917-946a-1cc64c03af46" />
</p>

- Los píxeles se cuentan desde arriba hasta abajo. Los píxeles son números enteros.

$$
columna = round(x''')
$$

$$
fila = Nc_y - round(y''')
$$

<p align="center">
   <img height="175" alt="image" src="https://github.com/user-attachments/assets/953b6adf-887b-4875-935f-4870797c8abb" />
</p>

# 6. Calibración de Cámaras
## 6.1. Explicación
Obtener automáticamente los parámetros geométricos (intrínsecos y extrínsecos) que intervienen en el proceso de formación de imágenes.

- Parámetros intrínsecos: Geometría y óptica del conjunto de la cámara y la tarjeta de adquisición (distancia focal, coeficientes de distorsión...)

- Parámetros extrínsecos: Definen la orientación y posición de la cámara respecto a un sistema de referencia conocido.

## 6.2. Proceso
- Tenemos una rejilla en el espacio la cual forma puntos.

- Se toman varias fotos de la rejilla desde distintas posiciones y ángulos.

- Estos puntos son leídos por la cámara

- Se establece una correspondencia (por métodos numéricos minimizando el error) entre puntos tridimensionales y sus proyecciones

## 6.3. Depende de

- El modelo de la cámara.

- Número y distribución de los puntos.

- Método numérico empleado.

## 6.4. Características del Calibrado

- El operador debe intervenir mínimamente.

- Debe ser muy precisa.

- Debe ser eficiente, una rejilla grande hace que la resolución sea costosa en el tiempo.

- Debe ser aplicable no solo a un tipo de cámara u óptica.

## 6.5. Metodo Transformación Lineal Directa
### 6.5.1. Declaración de las Matrices

<p align="center">
   <img height="200" alt="image" src="https://github.com/user-attachments/assets/f0b479a2-5c77-4f87-897b-9c6197023dca" />
</p>

M es el producto entre la matriz de transformación (la cámara se sitúa a una distancia y con una orientación distinta del sistema) y una matriz de cambio de escala y referencia (debido al tamaño de los píxeles y a centrar el plano imagen).

<p align="center">
   <img height="100" alt="image" src="https://github.com/user-attachments/assets/8ad912b8-1a16-44e5-b2ee-1053c16abbbf" />

</p>

Escribimos " $x'$ " e " $y'$ " con los parámetros de " $M$ ".

<p align="center">
   <img height="350" alt="image" src="https://github.com/user-attachments/assets/361c7b76-2bf6-40aa-b4aa-c4cdc4689dfb" />
</p>

Un posible problema de lo anterior es que " $M = 0$ ", impidiendo solucionar la ecuación. Para evitarlo, dividimos todo entre " $m_{34}$ ".

<p align="center">
   <img height="300" alt="image" src="https://github.com/user-attachments/assets/2ed38435-1e3d-4938-b7f8-ec6a4b5c15ea" />
</p>

Tenemos 11 incógnitas por lo que mínimo necesitaremos 6 puntos en la rejilla para poder calibrarlo. De cada punto deberemos saber tanto su posición tridimensional ( $X$ , $Y$ , $Z$ ) como su posición en el plano imagen (" $x'$ ", " $y'$ " ). Con esto obtendremos las 11 incógnitas. 

<p align="center">
   <img height="250" alt="image" src="https://github.com/user-attachments/assets/4dfe01b1-b381-422c-9df3-e7d669228c1f" />
</p>

La matriz " $𝑊$ " tiene una longitud de " $2 ∗ n$ " siendo " $𝑛$ " el número de puntos, por lo que, si tenemos más de 6 puntos, necesitaremos ayuda de la pseudoinversa.

$$
X = (W^T * W)^{-1} * W^T * C
$$

Una vez obtenidos todos los " $L_i$ ", nuestra matriz " $M$ " (la cual queremos ortonormal) será:

<p align="center">
   <img height="200" alt="image" src="https://github.com/user-attachments/assets/0342cf73-d466-4850-a1c1-d0fdcf91757a" />
</p>

### 6.5.2. Obtención de los Parámetros Intrínsecos
Obtenida " $M$ ", finalmente calcularemos los parámetros intrínsecos y extrínsecos. 

<p align="center">
   <img height="225" alt="image" src="https://github.com/user-attachments/assets/2ce4f8e5-d998-4adc-9445-d43ea7d338d4" />
</p>

Sabiendo que:

<p align="center">
   <img height="150" alt="image" src="https://github.com/user-attachments/assets/64ae8520-0e3c-4e97-b833-1766091e5edd" />
</p>

El cálculo de la distancia focal está explicado en el campus:

<p align="center">
   <img height="60" alt="image" src="https://github.com/user-attachments/assets/3b836282-7a57-4d9b-8397-e42c0a4a905b" />
</p>

# [Bibliografía](https://github.com/user-attachments/files/25093930/Tema.3.pdf)

