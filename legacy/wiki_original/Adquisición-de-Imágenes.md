# Índice

- [1. Adquisición de la Imágen](#1-Adquisición-de-la-Imágen)

- [2. Técnicas de Iluminación](#2-Técnicas-de-Iluminación)
   - [2.1. Explicación](#21-Explicación)
   - [2.2. Apertura y Velocidad de Obturación](#22-Apertura-y-Velocidad-de-Obturación)
   - [2.3. Tipos de Iluminación](#23-Tipos-de-Iluminación)
   - [2.4. Tipos de Fuentes](#24-Tipos-de-Fuentes)

- [3. Representación del Color](#3-Representación-del-Color)
   - [3.1. RGB](#31-RGB)
   - [3.2. CMY](#32-CMY)
   - [3.3. HSV](#33-HSV)
   - [3.4. LAB](#34-LAB)

- [4. Tipos de Cámaras](#4-Tipos-de-Cámaras)
   - [4.1. Explicación](#41-Explicación)
   - [4.2. De Tubo de Vacío](#42-De-Tubo-de-Vacío)
   - [4.3. De Estado Sólido](#43-De-Estado-Sólido)

- [5. Proceso de Digitalización](#5-Proceso-de-Digitalización)
   - [5.1. Muestreo](#51-Muestreo)
   - [5.2. Cuantificación](#52-Cuantificación)

- [6. Sistemas](#6-Sistemas)
   - [6.1. Transporte](#61-Transporte)
   - [6.2. Sistemas de Visión](#62-Sistemas-de-Visión)

- [7. Código](#7-Código)
   - [7.1. Detección de Colores](#71-Detección de Colores)


# 1. Adquisición de la Imágen
<p align="center">
   <img height="300" alt="image" src="https://github.com/user-attachments/assets/b82c756c-cbde-4495-9e77-d48ae07cacfa" />
   <img height="250" alt="image" src="https://github.com/user-attachments/assets/83821f3d-f736-4497-85ee-5aea5464061b" />
</p>

# 2. Técnicas de Iluminación
## 2.1. Explicación
Las cámaras captan la luz reflejada de los objetos. Si controlamos la luz, controlamos la forma en la que la cámara va a ver ese objeto. Al ojo humano le es fácil ver un objeto de la misma forma teniendo distintas fuentes de luz, sin embargo, a una cámara le es mucho más difícil y costoso (muchos filtros de software).

## 2.2. Apertura y Velocidad de Obturación
Dependiendo de la cantidad de luz que entre en la cámara y de las fotos que pueda hacer por segundo, se verá mejor o peor la imagen.

<p align="center">
   <img height="300" alt="image" src="https://github.com/user-attachments/assets/a3f4d282-a113-447e-b26e-0c35f5b51dcb" />
</p>

## 2.3. Tipos de Iluminación
- Iluminación Frontal: Es útil en superficies con pocos reflejos (papel, tela…)

<p align="center">
   <img height="300" alt="image" src="https://github.com/user-attachments/assets/4c6fe7a4-de85-4cd5-91ce-e413f0b667ed" />
</p>

- Iluminación Lateral: Útil para ciertos detalles de piezas que solo se ven orientando la luz de dicha forma (los pequeños objetos y las hendiduras aparecen en negro).

<p align="center">
   <img height="300" alt="image" src="https://github.com/user-attachments/assets/dc203630-de37-4f03-820b-aa60348afcdc" />
</p>

- Iluminación por Campo Oscuro: Útil para resaltar los defectos superficiales (grietas, surcos.)

<p align="center">
   <img height="400" alt="image" src="https://github.com/user-attachments/assets/aebdb879-96af-4027-8372-0c15bf6ed23b" />
</p>

- Iluminación por Contraste: Útil para reconocer la silueta del objeto y realizar mediciones muy precisas. Si el material es transparente o translucido, se pueden ver manchas, rayas y grietas.

<p align="center">
   <img height="400" alt="image" src="https://github.com/user-attachments/assets/f8f54e78-0a9b-4e70-9e9e-743855c0f9bd" />
</p>

- Iluminación Difusa sobre el Mismo eje (Iluminación Coaxial): Utilizada para iluminar objetos reflectantes. 

<p align="center">
   <img  height="350" alt="image" src="https://github.com/user-attachments/assets/d79935d4-468f-4bf5-87b9-7c8a5404971b" />
</p>

- Iluminación Difusa tipo Domo: Ofrece el máximo nivel de rendimiento en cuanto a iluminación difusa. Útil para objetos reflectantes complejos.

<p align="center">
   <img height="250" alt="image" src="https://github.com/user-attachments/assets/47b8413b-a5c9-4333-af72-e76e1dd48ec5" />
</p>

- Iluminación Difusa tipo Domo Plano: Es igual que el anterior, pero ocupa menos espacio. Tiene una lámina de material que difracta la luz perpendicularmente.

<p align="center">
   <img  height="300" alt="image" src="https://github.com/user-attachments/assets/fda48f69-1116-4c10-a715-788f25436994" />
</p>

- Iluminación Estructurada: Es utilizado para determinar la tercera dimensión de un objeto. Se utiliza una fuente de luz (generalmente un láser) en un ángulo conocido de forma que, viendo la distorsión con la luz, se puede medir la profundidad. 

<p align="center">
   <img height="250" alt="image" src="https://github.com/user-attachments/assets/4cff8513-e7e3-465e-88bb-d892fb59f8d3" />
</p>

## 2.4. Tipos de Fuentes
- LED: Debido a la polarización directa de un diodo, circula por él una corriente eléctrica que emite luz. La longitud de onda de esta luz depende del material semiconductor del diodo. Es eficiente energéticamente, barato y con larga vida, sin embargo, no tienen gran intensidad comparado con otros. El espectro es desde el ultravioleta hasta el infrarrojo.

<p align="center">
   <img height="350" alt="image" src="https://github.com/user-attachments/assets/b8c1a227-6415-4c3b-88d7-57ef7b099c2f" />
</p>

- Fibra Óptica: Por ahora proporciona la luz más intensa. Más que una fuente es una forma de enfocar y conducir una luz creada por otra fuente. Proporciona luz fría, así que es ideal para sistemas en los que el calor sea un inconveniente. 

<p align="center">
   <img height="175" alt="image" src="https://github.com/user-attachments/assets/a738d7b1-c9b5-4f22-b36f-0b897051c928" />
</p>

- Fluorescentes: Utilizan vapor de mercurio a baja presión para iluminar, produciendo que sean eficientes energéticamente. Es muy frágil y las lámparas creadas no pueden ser de todas las formas que queramos. Estas lámparas funcionan a una frecuencia determinada y, si esta es baja, este parpadeo se puede apreciar en las cámaras (en industria se necesita que funcionen a mínimo 25kHz).

<p align="center">
   <img height="200" alt="image" src="https://github.com/user-attachments/assets/61c437b5-6aad-41e3-b9bf-0fbfc549ec31" />
</p>

- Láser: Utilizadas para la iluminación estructurada.

<p align="center">
   <img  height="250" alt="image" src="https://github.com/user-attachments/assets/fa19edbf-a4a8-43ab-b76b-1483c3cef320" />
</p>

# 3. Representación del Color
## 3.1. RGB
Está basado en cómo nuestro ojo interpreta el color. Se pinta sobre un fondo negro (todo a 0).
- R: Nivel de Rojo del pixel.
- G: Nivel de Verde del pixel.
- B: Nivel de Azul del pixel.

<p align="center">
   <img height="300" alt="RGB" src="https://github.com/user-attachments/assets/cc9eed6d-d4cd-4b24-bb9d-a13aa89b59cf" />
</p>

- Intensidad: $0.3 ∗ R + 0.59 ∗ G + 0.11 ∗ B$

<p align="center">
   <img height="300" alt="image" src="https://github.com/user-attachments/assets/5fba20e2-4cff-45b3-9689-abb0d6effdba" />
</p>


## 3.2. CMY
Es útil para impresoras ya que se pinta sobre un fondo blanco (todo a 0).
- C: Nivel de Cian del pixel.
- M: Nivel de Magenta del pixel.
- Y: Nivel de Amarillo del pixel. 

<p align="center">
   <img height="250" alt="image" src="https://github.com/user-attachments/assets/c03cc582-dabd-4344-9cee-e32fda22b8e0" />
</p>

$$
\begin{bmatrix}
C \\
Y \\
M
\end{bmatrix}
= 1-
\begin{bmatrix}
R \\
G \\
B
\end{bmatrix}
$$

## 3.3. HSV
Es lo más útil para procesar la imagen a color en un computador.
- H (Matiz): Clasifica los colores, es decir, la variación de esta característica hace que el pixel pase de un color a otro (pasa por todos los colores).
- S (Saturación): Cuanto menor sea el valor, más se acercará al gris (escala del negro al blanco) dicho pixel y menos se acercará al color dado por el parámetro "H".
- V (Valor): Cuanto mayor sea más claro será y menos oscuro, es decir, determina qué escala de gris es dicho color. 

<p align="center">
   <img height="350" alt="image" src="https://github.com/user-attachments/assets/7d13c554-f6a6-4540-a735-e46415752052" />
</p>

## 3.4. LAB
- L: Nivel de Gris del pixel.
- A: Moverse por el eje verde-rojo.
- B: Moverse por el eje amarillo-azul. 

<p align="center">
   <img height="250" alt="image" src="https://github.com/user-attachments/assets/88e61bc6-82a3-4cdb-903c-9cc86246b516" />
</p>


# 4. Tipos de Cámaras
## 4.1. Explicación
Captura una imagen que se proyecta en el sensor (elemento fotosensible). Mediante una electrónica de lectura, un acondicionamiento de la señal y un conversor analógico digital, obtenemos la imagen digital.

## 4.2. De Tubo de Vacío
## 4.3. De Estado Sólido
Características a Tener en Cuenta: Control de disparo, Velocidad de Obturación, Sensibilidad espectral (rango de frecuencias), Factor de relleno (porcentaje de elementos que se utilizan tanto como sensor como registro), linealidad (entre la luz recibida y la señal dada), Blooming (cuando un registro de un elemento se llena pasa su valor de la señal a los elementos vecinos, cosa que no queremos), color o blanco y negro, lineal o espacial, salida digital o analógica, resolución...

<p align="center">
  <img height="300" alt="image" src="https://github.com/user-attachments/assets/07d862e6-3ed1-4e41-a2c1-36be734030dc" />
</p>

- Obturador (Shutter): Muchas veces, cuando se toma una foto, la cámara no emplea todo el tiempo para tomar una foto, si no un pequeño instante. Eso es debido a que si hay un objeto en movimiento y la cámara emplea mucho tiempo en obtener la información del entorno, el objeto en movimiento saldrá movido.

<p align="center">
   <img height="150" alt="image" src="https://github.com/user-attachments/assets/77c4e82a-1321-4620-af24-78a76c0796de" />
</p>

Esta es la gráfica de tiempo de un video a 25 fps.

<p align="center">
   <img height="150" alt="image" src="https://github.com/user-attachments/assets/e005e08c-363c-477b-b644-325271389881" />
</p>

- Apertura (número F): cuanto menor sea el número (denominador mayor), menor será la apertura.

<p align="center">
   <img width="829" height="100" alt="image" src="https://github.com/user-attachments/assets/24da82ed-9de1-440f-a985-fc34d9ffeb1a" />
</p>

- ISO (ganancia de los sensores): Subir el ISO aumenta la ganancia del sensor haciendo que se vea más los puntos de más luz. También amplifica imperfecciones.

<p align="center">
   <img height="275" alt="image" src="https://github.com/user-attachments/assets/b9463d7e-77d7-41f8-a965-1f672c814fb7" />
</p>

### 4.3.1. CCD (Charge Coupled Device)
- Funcionamiento: Tiene elementos fotosensibles capaces de acumular carga eléctrica en función de la cantidad de luz que reciben. Estos elementos también actúan como registros, es decir, a parte de actuar como sensor, guardan la información. Las cámaras matriciales tienen una relación o 4:3 o 16:9 (normalmente 16:9).

<p align="center">
   <img height="125" alt="image" src="https://github.com/user-attachments/assets/e7b7e246-87ec-433a-bb59-cd2488b1b7f3" />
   <img height="125" alt="image" src="https://github.com/user-attachments/assets/30fec3c9-3187-4d23-8ba3-60d9b58257d2" />
</p>

- Procesos de lectura:
   - Full Frame: Hacen una foto y empiezan a leer pixel tras pixel de la siguiente forma. Debido al paso de la información de los pixeles de arriba hacia los de abajo, se puede producir un proceso de “smearing” en con los objetos brillantes (con un obturador se puede evitar).

<p align="center">
   <img height="150" alt="image" src="https://github.com/user-attachments/assets/74725b36-df91-4980-9015-395b76c01231" />
   <img height="150" alt="image" src="https://github.com/user-attachments/assets/12910d52-12a0-410b-af8f-d498d4c78be5" />
</p>

   - Frame Transfert: Utiliza la mitad de los elementos como registros en vez de como registros y sensores. Con los sensores obtiene la información. Esta información se copia en los elementos que solo actúan como registros y se liberan los que actúan como sensores para poder hacer fotos con mayor velocidad. Mientras los elementos de registro procesan la imagen.

<p align="center">
   <img height="350" alt="image" src="https://github.com/user-attachments/assets/5117f504-24c0-4341-bacb-acf2e8bdb769" />
</p>

   - Interligne Transfert: Parecido al anterior, pero en vez de utilizar la mitad de abajo se intercalan columnas de elementos completos y elementos de registros. El sensor obtiene la información y se lo pasa al registro de su derecha. 

<p align="center">
   <img height="250" alt="image" src="https://github.com/user-attachments/assets/0821e98d-63ce-4600-abba-7d380f07ae2d" />
</p>

### 4.3.2. CMOS (Complementary Metal Oxide Semiconductor)
- Funcionamiento: Utilizando la tecnología CMOS (fotodiodos), detecta la luz. Se pueden integrar ciertas funciones en el propio chip del
sensor (control de luminosidad, contraste, conversor analógico digital).

<p align="center">
  <img height="250" alt="image" src="https://github.com/user-attachments/assets/8110a0cc-2cac-4f42-ae22-1f1f96a7be88" />
</p>

- Errores (Rolling Shutter): Muchos sensores utilizan el Global Shutter, es decir, todos los pixeles del sensor actúan a la vez. Sin embargo, las cámaras baratas hacen un barrido. 

<p align="center">
  <img height="250" alt="image" src="https://github.com/user-attachments/assets/1de1d4f5-1371-4fcb-9dcf-b70895fb3f2a" />
</p>



### 4.3.3. Obtención del Color
- Triple Sensor: Utilizando un prisma, descomponemos la luz en los colores rojo, azul y verde y obtener la información con 3 sensores. Tienen una gran resolución y calidad cromática. Son caras.

<p align="center">
  <img height="175" alt="image" src="https://github.com/user-attachments/assets/dafc9fde-1472-41f8-a308-801426f27749" />
</p>

- Sensor con Exposición Triple: Cada sensor tiene 3 filtros que se van intercambiado secuencialmente obteniendo la intensidad lumínica del rojo, azul y el verde. El cuarzo líquido puede actuar como filtro de un color dependiendo del voltaje que se le aplique.

<p align="center">
  <img height="200" alt="image" src="https://github.com/user-attachments/assets/248b7e2c-22c7-422d-b78f-397af952af86" />
</p>

- Mosaico: Cada pixel tiene un filtro por lo que solo es sensible a un color. Los pixeles de alrededor de otro pixel tienen filtros diferentes. Para que cada pixel tenga la información del color exacto, cada pixel obtiene información tanto suya como de los de al lado.

<p align="center">
  <img height="175" alt="image" src="https://github.com/user-attachments/assets/ec52e1a7-fc3e-4f3f-8ee6-815481326c38" />
</p>

Finalmente se interpolan los píxeles no obtenidos

<p align="center">
  <img height="80" alt="image" src="https://github.com/user-attachments/assets/d810a24f-545f-487b-b393-ff34e49914d1" />
</p>
- Foveon x3: Como dependiendo de la longitud de onda cada color tiene distinta profundidad en el silicio, se pueden poner los 3 sensores en columna en un mismo píxel.

<p align="center">
  <img height="200" alt="image" src="https://github.com/user-attachments/assets/781b77a8-c026-4de8-8622-7940f26a6624" />
</p>

- Mosaico super CDD: Es igual que el método mosaico, pero en vez de utilizar sensores rectangulares se utilizan octogonales.

<p align="center">
  <img height="200" alt="image" src="https://github.com/user-attachments/assets/9324cefe-ef36-47fb-8ad2-81f9c97794a6" />
</p>

# 5. Proceso de Digitalización
## 5.1. Muestreo
El sensor da un valor analógico dependiendo de la intensidad de luz recibida en cada momento. Se debe muestrear este valor y formar una curva de puntos en el tiempo a cada valor.

<p align="center">
   <img height="200" alt="image" src="https://github.com/user-attachments/assets/90288804-42fd-42ae-b2c6-9441f9177811" />
</p>

## 5.2. Cuantificación
Establece un valor discreto (entre el 0 y el 1 o entre el 0 y el 255) a cada valor muestreado (a cada punto) y crea la matriz que representa la imagen.

<p align="center">
   <img height="200" alt="image" src="https://github.com/user-attachments/assets/7a3fcee8-0a18-4458-87ef-31c6518ac9b0" />
</p>

# 6. Sistemas
## 6.1. Transporte
- Fire Wire – IEEE 1394: es un bus digital que puede alcanzar 800 Mbits/seg que proporciona una interface cámara ordenador flexible y de coste razonable. Puede conectar varias cámaras a una sóla placa. Varios ordenadores pueden capturar imágenes desde la misma cámara. El control de la cámara, la alimentación y las señales se transmiten a través de un mismo cable.

- GIGABIT – ETHERNET: la velocidad de transferencia de Gigabit Ethernet es de 1000 Mbits/seg. Conexión punto a punto. Permite largas longitudes de cables. Múltiple distribución de imagen. Número de dispositivos ilimitado.

- Camera Link: es un estándar de conexión entre las tarjetas de adquisición de imágenes y cámaras digitales, que permite la transferencia de datos a alta velocidad.

- USB2 – USB3 – USBC: múltiples entradas disponibles en el mismo ordenador. Velocidad de transferencia de hasta 480 Mbits/seg en USB2 (x3 en USB3).

## 6.2. Sistemas de Visión
- Tarjetas de Adquisición de Imágenes: Conectan diversos tipos de cámaras a un ordenador.

- Sensores de Visión: Cámaras las cuales tienen un programa simple asignado el cual realiza una actividad requerida de procesamiento de imagen. Su salida, por ejemplo, puede ser la lectura de un código de barras.

- Cámaras Inteligentes: Igual que el anterior pero más potentes (memoria, procesador, mecanismos de entrada y salida…).

- Sistemas de Visión Integrados: A un controlador se le conectan varias cámaras para procesar lo elegido.

<p align="center">
   <img height="175" alt="image" src="https://github.com/user-attachments/assets/d2433199-8bb2-47b3-b242-60fabab5f5ec" />
</p>

# [Bibliografía](https://github.com/user-attachments/files/25093907/Tema.2.pdf)




# 7. Código
## 7.1. Detección de Colores


<p align="center">
   <img width="571" height="324" alt="image" src="https://github.com/user-attachments/assets/ac43023c-0841-4f93-b14a-92610d19da26" />
</p>

