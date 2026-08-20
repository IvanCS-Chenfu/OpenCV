# Índice

- [0. Introducción](#0-introducción)

- [1. Qué significa formar una imagen](#1-qué-significa-formar-una-imagen)

- [2. El proceso geométrico completo](#2-el-proceso-geométrico-completo)
  - [2.1 Transformación 3D → 3D](#21-transformación-3d--3d)
  - [2.2 Transformación 3D → 2D](#22-transformación-3d--2d)
  - [2.3 Transformación 2D → 2D](#23-transformación-2d--2d)

- [3. Sistemas de referencia en la formación de imágenes](#3-sistemas-de-referencia-en-la-formación-de-imágenes)

  - [3.1 Sistema del mundo](#31-sistema-del-mundo)
  - [3.2 Sistema de la cámara](#32-sistema-de-la-cámara)
  - [3.3 Plano sensor](#33-plano-sensor)
  - [3.4 Matriz imagen](#34-matriz-imagen)

- [4. Transformación del mundo a la cámara](#4-transformación-del-mundo-a-la-cámara)
  - [4.1 Parámetros extrínsecos](#41-parámetros-extrínsecos)
  - [4.2 Interpretación de R y t](#42-interpretación-de-r-y-t)
  - [4.3 Forma homogénea](#43-forma-homogénea)

- [5. Modelo pinhole](#5-modelo-pinhole)
  - [5.1 Idea física del modelo pinhole](#51-idea-física-del-modelo-pinhole)
  - [5.2 Plano imagen real y plano imagen virtual](#52-plano-imagen-real-y-plano-imagen-virtual)
  - [5.3 Proyección 3D → 2D](#53-proyección-3d--2d)
  - [5.4 Interpretación geométrica de la profundidad](#54-interpretación-geométrica-de-la-profundidad)
  - [5.5 Proyección 2D → 3D: el rayo de proyección](#55-proyección-2d--3d-el-rayo-de-proyección)
  - [5.6 Plano normalizado](#56-plano-normalizado)
  - [5.7 Forma matricial homogénea del modelo pinhole](#57-forma-matricial-homogénea-del-modelo-pinhole)

- [6. Homografía 2D en visión por computador](#6-homografía-2d-en-visión-por-computador)
  - [6.1 Homografía como transformación entre planos](#61-homografía-como-transformación-entre-planos)
  - [6.2 Cuándo aparece una homografía entre imágenes](#62-cuándo-aparece-una-homografía-entre-imágenes)
  - [6.3 Cámara fija y cambio de plano imagen](#63-cámara-fija-y-cambio-de-plano-imagen)
  - [6.4 Cámara rotando sobre su centro óptico](#64-cámara-rotando-sobre-su-centro-óptico)
  - [6.5 Cámara moviéndose observando un plano](#65-cámara-moviéndose-observando-un-plano)
  - [6.6 Escenas no planas](#66-escenas-no-planas)
  - [6.7 Estimación de una homografía: DLT](#67-estimación-de-una-homografía-dlt)
  - [6.8 Homografía de rectas](#68-homografía-de-rectas)
  - [6.9 Puntos en el infinito en homografías](#69-puntos-en-el-infinito-en-homografías)

- [7. Del plano sensor a la matriz imagen](#7-del-plano-sensor-a-la-matriz-imagen)
  - [7.1 Por qué hace falta esta transformación](#71-por-qué-hace-falta-esta-transformación)
  - [7.2 Coordenadas métricas y coordenadas en píxeles](#72-coordenadas-métricas-y-coordenadas-en-píxeles)
  - [7.3 Matriz de conversión sensor-imagen](#73-matriz-de-conversión-sensor-imagen)
  - [7.4 Centro principal](#74-centro-principal)
  - [7.5 Skew](#75-skew)
  - [7.6 Distancia focal en píxeles](#76-distancia-focal-en-píxeles)

- [8. Modelo completo de cámara](#8-modelo-completo-de-cámara)
  - [8.1 Por qué el modelo pinhole aislado no basta](#81-por-qué-el-modelo-pinhole-aislado-no-basta)
  - [8.2 Parámetros extrínsecos](#82-parámetros-extrínsecos)
  - [8.3 Parámetros intrínsecos](#83-parámetros-intrínsecos)
  - [8.4 Matriz de proyección de la cámara](#84-matriz-de-proyección-de-la-cámara)
  - [8.5 Ecuaciones no lineales resultantes](#85-ecuaciones-no-lineales-resultantes)
  - [8.6 Grados de libertad](#86-grados-de-libertad)

- [9. Distorsión radial](#9-distorsión-radial)

- [10. Resumen final](#10-resumen-final)

---

# 0. Introducción

En esta página se estudia la **formación de imágenes** desde el punto de vista geométrico.

La pregunta principal es:

> Dado un punto 3D de una escena, ¿en qué posición de la imagen aparece?

Este problema es fundamental en visión por computador, porque permite relacionar el mundo tridimensional con la imagen bidimensional capturada por una cámara.

En esta página se utilizarán conceptos matemáticos ya explicados en [Métodos Matemáticos](https://github.com/IvanCS-Chenfu/M-todos-Matem-ticos/wiki/Matrices-de-Transformaci%C3%B3n):

- [Coordenadas homogéneas y matrices homogéneas](https://github.com/IvanCS-Chenfu/M-todos-Matem-ticos/wiki/Matrices-de-Transformaci%C3%B3n#5-coordenadas-homog%C3%A9neas-y-matrices-homog%C3%A9neas)
- [Transformación euclídea o rígida](https://github.com/IvanCS-Chenfu/M-todos-Matem-ticos/wiki/Matrices-de-Transformaci%C3%B3n#61-transformaci%C3%B3n-eucl%C3%ADdea-o-r%C3%ADgida)
- [Transformación afín](https://github.com/IvanCS-Chenfu/M-todos-Matem-ticos/wiki/Matrices-de-Transformaci%C3%B3n#63-transformaci%C3%B3n-af%C3%ADn)
- [Homografía](https://github.com/IvanCS-Chenfu/M-todos-Matem-ticos/wiki/Matrices-de-Transformaci%C3%B3n#64-homograf%C3%ADa)

---

# 1. Qué significa formar una imagen

La **formación de imágenes** es el proceso mediante el cual los objetos de una escena 3D se proyectan sobre un plano 2D.

Es decir:

$$
\text{escena 3D} \longrightarrow \text{imagen 2D}
$$

Un punto de la escena se puede representar como:

$$
M =
\begin{bmatrix}
X \\
Y \\
Z
\end{bmatrix}
$$

y su imagen como:

$$
m =
\begin{bmatrix}
x \\
y
\end{bmatrix}
$$

o, si hablamos de píxeles de la imagen digital:

$$
m' =
\begin{bmatrix}
u \\
v
\end{bmatrix}
$$

El proceso de formación de imágenes tiene dos grandes partes:

1. **Problema geométrico**: determinar dónde se proyecta cada punto 3D en la imagen.
2. **Problema radiométrico**: determinar qué color o intensidad tiene cada punto proyectado.

En esta página nos centramos en el **problema geométrico**.

Es decir, estudiaremos cómo se obtiene la posición de la imagen:

$$
(X,Y,Z) \longrightarrow (u,v)
$$

pero no estudiaremos cómo se calcula el color del píxel.

---

<img width="563" height="331" alt="image" src="https://github.com/user-attachments/assets/069b1d1b-8ceb-44b5-abee-4d7634dada47" />

---

# 2. El proceso geométrico completo

El proceso geométrico completo que se quiere modelar puede dividirse en tres transformaciones principales:

$$
\text{mundo 3D}
\longrightarrow
\text{cámara 3D}
\longrightarrow
\text{plano sensor 2D}
\longrightarrow
\text{imagen digital 2D}
$$

Es decir:

$$
M_W
\longrightarrow
M_C
\longrightarrow
m
\longrightarrow
m'
$$

donde:

- $M_W$ es el punto expresado en el sistema de coordenadas del mundo.
- $M_C$ es el mismo punto expresado en el sistema de coordenadas de la cámara.
- $m$ es el punto proyectado en el plano sensor.
- $m'$ es el punto expresado en coordenadas de imagen, normalmente en píxeles.

El proceso completo se puede dividir en tres transformaciones geométricas:

1. **3D → 3D**: paso del sistema del mundo al sistema de la cámara.
2. **3D → 2D**: proyección perspectiva del punto 3D sobre el plano sensor.
3. **2D → 2D**: conversión desde coordenadas del sensor a coordenadas de la matriz imagen.

---

<img width="1235" height="419" alt="image" src="https://github.com/user-attachments/assets/205f767d-af5d-4930-856b-94f3ff71efa1" />

---

# 2.1 Transformación 3D → 3D

La primera transformación consiste en expresar un punto 3D del mundo en el sistema de coordenadas de la cámara.

Si el punto está expresado en el sistema del mundo:

$$
M_W =
\begin{bmatrix}
X_W \\
Y_W \\
Z_W
\end{bmatrix}
$$

queremos obtener sus coordenadas en el sistema de la cámara:

$$
M_C =
\begin{bmatrix}
X_C \\
Y_C \\
Z_C
\end{bmatrix}
$$

Esta transformación se realiza mediante una rotación y una traslación:

$$
M_C = R M_W + t
$$

donde:

- $R$ es la matriz de rotación.
- $t$ es el vector de traslación.
- $M_W$ es el punto en el sistema mundo.
- $M_C$ es el punto en el sistema cámara.

Esta transformación es una [transformación euclídea o rígida](https://github.com/IvanCS-Chenfu/M-todos-Matem-ticos/wiki/Matrices-de-Transformaci%C3%B3n#61-transformaci%C3%B3n-eucl%C3%ADdea-o-r%C3%ADgida), porque conserva distancias y ángulos. Solo cambia el sistema de referencia desde el que se expresa el punto.

En visión por computador, esta transformación representa la **pose de la cámara** respecto al mundo.

---

# 2.2 Transformación 3D → 2D

Una vez que el punto está expresado en el sistema de la cámara, se proyecta sobre el plano imagen.

Esta es la parte central del **modelo pinhole**.

Si:

$$
M_C =
\begin{bmatrix}
X_C \\
Y_C \\
Z_C
\end{bmatrix}
$$

entonces su proyección ideal en el plano sensor es:

$$
m =
\begin{bmatrix}
x \\
y
\end{bmatrix} =
\begin{bmatrix}
f\dfrac{X_C}{Z_C} \\
f\dfrac{Y_C}{Z_C}
\end{bmatrix}
$$

donde $f$ es la distancia focal.

Esta transformación es la que introduce la perspectiva.

La división por $Z_C$ hace que los objetos más lejanos aparezcan más pequeños en la imagen.

---

<p align="center">
   <img height="175" alt="image" src="https://github.com/user-attachments/assets/ce0ace38-1e29-41e6-bbd0-5f60c7a23796" />
</p>

---

# 2.3 Transformación 2D → 2D

El punto $m=(x,y)$ está en el plano sensor, normalmente en unidades métricas, por ejemplo metros o milímetros.

Pero en un ordenador la imagen no se representa en metros, sino como una matriz de píxeles.

Por tanto, hay que convertir:

$$
m =
\begin{bmatrix}
x \\
y
\end{bmatrix}
$$

en:

$$
m' =
\begin{bmatrix}
u \\
v
\end{bmatrix}
$$

donde:

- $u$ suele representar la coordenada horizontal, es decir, la columna.
- $v$ suele representar la coordenada vertical, es decir, la fila.

Esta transformación se modela mediante una transformación 2D, normalmente afín, que incorpora:

- cambio de escala de metros a píxeles,
- desplazamiento del origen,
- posible falta de perpendicularidad exacta entre ejes,
- posición del centro principal.

---

# 3. Sistemas de referencia en la formación de imágenes

Para entender el modelo de cámara es fundamental distinguir claramente los sistemas de coordenadas.

En el proceso de formación de imagen aparecen cuatro sistemas importantes:

1. Sistema del mundo.
2. Sistema de la cámara.
3. Plano sensor.
4. Sistema imagen o matriz imagen.

---

# 3.1 Sistema del mundo

El **sistema del mundo** es un sistema de referencia externo a la cámara.

Se utiliza para describir la posición real de los objetos de la escena.

Un punto en el sistema del mundo se escribe como:

$$
M_W =
\begin{bmatrix}
X_W \\
Y_W \\
Z_W
\end{bmatrix}
$$

Este sistema puede definirse de muchas maneras.

Por ejemplo:

- el origen puede estar en una esquina de una habitación,
- en el centro de un robot,
- en una marca de calibración,
- en una esquina de un patrón de ajedrez,
- en cualquier punto elegido como referencia.

El sistema del mundo no depende de la cámara. La cámara puede moverse respecto a él.

---

# 3.2 Sistema de la cámara

El **sistema de la cámara** tiene su origen en el centro óptico de la cámara, normalmente denotado como $C$.

En el modelo pinhole, $C$ es el punto por el que pasan todos los rayos de proyección.

Un punto expresado en el sistema de la cámara se escribe como:

$$
M_C =
\begin{bmatrix}
X_C \\
Y_C \\
Z_C
\end{bmatrix}
$$

El eje $Z_C$ suele coincidir con el eje óptico o eje principal de la cámara.

La profundidad del punto respecto a la cámara viene dada por:

$$
Z_C
$$

Esta coordenada será clave, porque en la proyección perspectiva se divide entre $Z_C$.

---

# 3.3 Plano sensor

El **plano sensor** es el plano donde se forma la imagen geométrica ideal.

En una cámara física, la luz pasa por la lente y llega al sensor.

En el modelo pinhole ideal, todos los rayos pasan por un único punto, el centro óptico $C$, y cortan el plano imagen.

Un punto del plano sensor se expresa como:

$$
m =
\begin{bmatrix}
x \\
y
\end{bmatrix}
$$

Estas coordenadas suelen interpretarse en unidades físicas, por ejemplo metros.

---

# 3.4 Matriz imagen

La **matriz imagen** es la representación digital de la imagen en el ordenador.

En vez de coordenadas métricas $(x,y)$, usamos coordenadas de píxel:

$$
m' =
\begin{bmatrix}
u \\
v
\end{bmatrix}
$$

donde normalmente:

- $u$ indica la columna.
- $v$ indica la fila.

Esta diferencia es importante porque en matemáticas solemos representar los ejes como $x$ horizontal e $y$ vertical hacia arriba, mientras que en imágenes digitales el eje vertical suele crecer hacia abajo.

Por eso es necesario un último paso de conversión entre el plano sensor y la matriz imagen.

---

# 4. Transformación del mundo a la cámara

# 4.1 Parámetros extrínsecos

La cámara no siempre está situada en el origen del mundo ni orientada igual que el sistema del mundo.

Por eso, antes de proyectar un punto, hay que expresarlo en coordenadas de cámara.

La transformación es:

$$
M_C = R_W^C M_W + t_W^C
$$

donde:

- $M_W$ es el punto en coordenadas del mundo.
- $M_C$ es el mismo punto en coordenadas de cámara.
- $R_W^C$ es la rotación que expresa los ejes del mundo en el sistema de cámara.
- $t_W^C$ es la posición del origen del mundo expresada en el sistema de cámara.

Estos parámetros se llaman **parámetros extrínsecos**.

Se llaman así porque describen la posición y orientación de la cámara respecto al mundo, no propiedades internas de la cámara.

---

# 4.2 Interpretación de R y t

La matriz $R_W^C$ es una matriz de rotación.

Una matriz de rotación 3D tiene la forma:

$$
R =
\begin{bmatrix}
r_{11} & r_{12} & r_{13} \\
r_{21} & r_{22} & r_{23} \\
r_{31} & r_{32} & r_{33}
\end{bmatrix}
$$

En el contexto de cámara, esta matriz puede interpretarse como el cambio de orientación entre el sistema mundo y el sistema cámara.

El vector de traslación:

$$
t =
\begin{bmatrix}
t_x \\
t_y \\
t_z
\end{bmatrix}
$$

representa el desplazamiento entre los orígenes de ambos sistemas.

La expresión:

$$
M_C = R M_W + t
$$

significa que primero se reorienta el punto mediante $R$ y después se traslada mediante $t$.

Desde el punto de vista de visión por computador, esta operación es una transformación de coordenadas: no se está moviendo físicamente el punto de la escena, sino cambiando el sistema desde el que se expresan sus coordenadas.


---

<img width="759" height="453" alt="image" src="https://github.com/user-attachments/assets/1f7420df-f3ee-4fd0-a6d8-6bb3f6bf03d4" />

---

# 4.3 Forma homogénea

Para que el sistema sea lineal, se utilizan [transformaciones homogéneas 3D](https://github.com/IvanCS-Chenfu/M-todos-Matem-ticos/wiki/Matrices-de-Transformaci%C3%B3n#56-matrices-homog%C3%A9neas-en-3d).


En coordenadas homogéneas, la transformación:

$$
M_C = R M_W + t
$$

se escribe como una única multiplicación matricial:

$$
\tilde{M}_C =
D
\tilde{M}_W
$$

donde:

$$
\tilde{M}_W =
\begin{bmatrix}
X_W \\
Y_W \\
Z_W \\
1
\end{bmatrix}
$$

$$
\tilde{M}_C =
\begin{bmatrix}
X_C \\
Y_C \\
Z_C \\
1
\end{bmatrix}
$$

y:

$$
D =
\begin{bmatrix}
R & t \\
0_3^T & 1
\end{bmatrix}
$$

Escrita completa:

$$
D =
\begin{bmatrix}
r_{11} & r_{12} & r_{13} & t_x \\
r_{21} & r_{22} & r_{23} & t_y \\
r_{31} & r_{32} & r_{33} & t_z \\
0 & 0 & 0 & 1
\end{bmatrix}
$$

Esta matriz $D$ será uno de los bloques principales del modelo completo de cámara. Se usa para pasar de mundo a cámara antes de aplicar el modelo pinhole.

---

# 5. Modelo pinhole

# 5.1 Idea física del modelo pinhole

El modelo **pinhole** representa una cámara ideal con una abertura infinitamente pequeña.

La idea es:

> De todos los rayos de luz que salen de un punto 3D de la escena, solo uno pasa por el centro óptico y llega al plano imagen.

El punto por el que pasa ese rayo se llama:

$$
C
$$

y se interpreta como el centro óptico de la cámara.

Si un punto 3D de la escena es:

$$
M =
\begin{bmatrix}
X \\
Y \\
Z
\end{bmatrix}
$$

entonces el rayo que va desde $M$ hasta el centro óptico $C$ corta al plano imagen en un punto:

$$
m =
\begin{bmatrix}
x \\
y
\end{bmatrix}
$$

Ese punto $m$ es la proyección de $M$.

---

<img width="775" height="520" alt="image" src="https://github.com/user-attachments/assets/23a08aaf-d2bd-4923-93a0-3004f014b2ef" />

---

# 5.2 Plano imagen real y plano imagen virtual

En una cámara pinhole física, el plano sensor se encuentra detrás del centro óptico.

Esto provoca que la imagen aparezca invertida horizontal y verticalmente.

Si el punto 3D es:

$$
M =
\begin{bmatrix}
X \\
Y \\
Z
\end{bmatrix}
$$

su proyección en el plano físico detrás del centro óptico tendría coordenadas proporcionales a:

$$
-x
$$

y:

$$
-y
$$

Para simplificar el modelo matemático se suele introducir un **plano imagen virtual** delante del centro óptico.

Este plano virtual se coloca a distancia $f$ del centro óptico, en la dirección positiva del eje óptico.

La ventaja es que las coordenadas proyectadas tienen el mismo signo que las coordenadas $X$ e $Y$ del punto 3D.

Por eso se trabaja con:

$$
x = f \frac{X}{Z}
$$

$$
y = f \frac{Y}{Z}
$$

sin arrastrar signos negativos.

---

<img width="952" height="483" alt="image" src="https://github.com/user-attachments/assets/773873e7-49fa-4a38-a3eb-c519aa341405" />

---

# 5.3 Proyección 3D → 2D

Supongamos que el punto 3D ya está expresado en el sistema de la cámara:

$$
M_C =
\begin{bmatrix}
X_C \\
Y_C \\
Z_C
\end{bmatrix}
$$

Para simplificar la notación, en esta sección escribiremos:

$$
M =
\begin{bmatrix}
X \\
Y \\
Z
\end{bmatrix}
$$

La cámara proyecta este punto sobre el plano imagen situado a distancia $f$.

Por semejanza de triángulos:

$$
\frac{x}{f} = \frac{X}{Z}
$$

por tanto:

$$
x = f\frac{X}{Z}
$$

De forma análoga:

$$
\frac{y}{f} = \frac{Y}{Z}
$$

por tanto:

$$
y = f\frac{Y}{Z}
$$

Así, la proyección pinhole es:

$$
m =
\begin{bmatrix}
x \\
y
\end{bmatrix} =
\begin{bmatrix}
f\dfrac{X}{Z} \\
f\dfrac{Y}{Z}
\end{bmatrix}
$$

Esta es una transformación:

$$
\mathbb{R}^3 \longrightarrow \mathbb{R}^2
$$

---

<p align="center">
   <img height="175" alt="image" src="https://github.com/user-attachments/assets/ce0ace38-1e29-41e6-bbd0-5f60c7a23796" />
</p>

---

## Ejemplo numérico

Supongamos:

$$
f = 0.003 \text{ m}
$$

y:

$$
M =
\begin{bmatrix}
0.12 \\
0.24 \\
3
\end{bmatrix}
\text{ m}
$$

Entonces:

$$
x = 0.003 \cdot \frac{0.12}{3}
$$

$$
x = 0.003 \cdot 0.04
$$

$$
x = 0.00012 \text{ m}
$$

y:

$$
y = 0.003 \cdot \frac{0.24}{3}
$$

$$
y = 0.003 \cdot 0.08
$$

$$
y = 0.00024 \text{ m}
$$

Por tanto:

$$
m =
\begin{bmatrix}
0.00012 \\
0.00024
\end{bmatrix}
\text{ m}
$$

El punto aparece en el plano sensor a $0.12$ mm y $0.24$ mm del centro.

---

# 5.4 Interpretación geométrica de la profundidad

La profundidad $Z$ aparece en el denominador:

$$
x = f\frac{X}{Z}
$$

$$
y = f\frac{Y}{Z}
$$

Esto tiene una interpretación muy importante:

- Si $Z$ aumenta, el punto está más lejos.
- Si $Z$ aumenta, las coordenadas proyectadas $x$ e $y$ disminuyen.
- Por tanto, el objeto aparece más pequeño.

Por ejemplo, si mantenemos $X$ e $Y$ constantes pero duplicamos $Z$:

$$
Z \rightarrow 2Z
$$

entonces:

$$
x' = f\frac{X}{2Z} = \frac{1}{2}x
$$

$$
y' = f\frac{Y}{2Z} = \frac{1}{2}y
$$

El punto proyectado se acerca al centro de la imagen.

Este efecto es la base de la perspectiva.

---

# 5.5 Proyección 2D → 3D: el rayo de proyección

El modelo pinhole también puede verse al revés.

Dado un punto de la imagen:

$$
m =
\begin{bmatrix}
x \\
y
\end{bmatrix}
$$

no podemos recuperar un único punto 3D, porque se ha perdido la profundidad.

Lo que sí podemos recuperar es un **rayo 3D**.

El punto del plano imagen correspondiente a $m$ se puede escribir como:

$$
P =
\begin{bmatrix}
x \\
y \\
f
\end{bmatrix}
$$

El rayo que pasa por el centro óptico y por ese punto es:

$$
M(k) =
k
\begin{bmatrix}
x \\
y \\
f
\end{bmatrix}
$$

donde $k$ es un escalar.

Como el centro óptico está en:

$$
C =
\begin{bmatrix}
0 \\
0 \\
0
\end{bmatrix}
$$

el rayo es simplemente:

$$
M(k) =
\begin{bmatrix}
k x \\
k y \\
k f
\end{bmatrix}
$$

Si queremos parametrizar el rayo usando la profundidad $Z$, observamos que:

$$
Z = kf
$$

por tanto:

$$
k = \frac{Z}{f}
$$

Sustituyendo:

$$
M(Z) =
\begin{bmatrix}
Z\dfrac{x}{f} \\
Z\dfrac{y}{f} \\
Z
\end{bmatrix}
$$

o:

$$
M(Z) =
Z
\begin{bmatrix}
x/f \\
y/f \\
1
\end{bmatrix}
$$

Esto significa que todos los puntos 3D que están sobre ese rayo proyectan en el mismo punto de imagen $m$.

---

## Ejemplo numérico

Sea:

$$
f = 3 \times 10^{-3} \text{ m}
$$

y un punto del plano imagen:

$$
m =
\begin{bmatrix}
-4 \times 10^{-4} \\
-8 \times 10^{-4}
\end{bmatrix}
\text{ m}
$$

El punto del plano imagen en 3D es:

$$
P =
\begin{bmatrix}
-4 \times 10^{-4} \\
-8 \times 10^{-4} \\
3 \times 10^{-3}
\end{bmatrix}
$$

El rayo asociado es:

$$
M(k) =
k
\begin{bmatrix}
-4 \times 10^{-4} \\
-8 \times 10^{-4} \\
3 \times 10^{-3}
\end{bmatrix}
$$

Usando $Z$ como parámetro:

$$
M(Z) =
Z
\begin{bmatrix}
\dfrac{-4 \times 10^{-4}}{3 \times 10^{-3}} \\
\dfrac{-8 \times 10^{-4}}{3 \times 10^{-3}} \\
1
\end{bmatrix}
$$

Esto representa todos los puntos 3D posibles que se proyectan en ese punto de imagen.

---

<img width="1155" height="306" alt="image" src="https://github.com/user-attachments/assets/49bd0512-648a-480d-8e5d-1f2ca4d4af8b" />

<img width="694" height="361" alt="image" src="https://github.com/user-attachments/assets/d51c1652-090b-4926-b9b1-046d205b9053" />

---

# 5.6 Plano normalizado

El plano imagen normalizado es el plano que se obtiene al tomar:

$$
f = 1
$$

En ese caso, la proyección se simplifica a:

$$
x_n = \frac{X}{Z}
$$

$$
y_n = \frac{Y}{Z}
$$

El punto normalizado es:

$$
m_1 =
\begin{bmatrix}
X/Z \\
Y/Z
\end{bmatrix}
$$

Después, la distancia focal escala ese punto:

$$
m =
\begin{bmatrix}
fX/Z \\
fY/Z
\end{bmatrix} =
f
\begin{bmatrix}
X/Z \\
Y/Z
\end{bmatrix}
$$

Por eso el modelo pinhole se puede descomponer en dos pasos:

1. Proyección perspectiva normalizada:

$$
\begin{bmatrix}
X \\
Y \\
Z
\end{bmatrix}
\longrightarrow
\begin{bmatrix}
X/Z \\
Y/Z
\end{bmatrix}
$$

2. Escalado por la distancia focal:

$$
\begin{bmatrix}
X/Z \\
Y/Z
\end{bmatrix}
\longrightarrow
\begin{bmatrix}
fX/Z \\
fY/Z
\end{bmatrix}
$$

Esta descomposición será útil cuando se introduzca la matriz intrínseca de la cámara.

---

# 5.7 Forma matricial homogénea del modelo pinhole

La proyección pinhole:

$$
x = f\frac{X}{Z}
$$

$$
y = f\frac{Y}{Z}
$$

no es lineal en coordenadas cartesianas, porque aparece una división entre $Z$.

Sin embargo, usando [coordenadas homogéneas](https://github.com/IvanCS-Chenfu/M-todos-Matem-ticos/wiki/Matrices-de-Transformaci%C3%B3n#5-coordenadas-homog%C3%A9neas-y-matrices-homog%C3%A9neas), se puede escribir mediante una matriz.

Partimos del punto 3D homogéneo:

$$
\tilde{M} =
\begin{bmatrix}
X \\
Y \\
Z \\
1
\end{bmatrix}
$$

y queremos obtener el punto imagen homogéneo:

$$
\tilde{m} =
\begin{bmatrix}
x \\
y \\
1
\end{bmatrix}
$$

El modelo pinhole se puede escribir como:

$$
Z
\begin{bmatrix}
x \\
y \\
1
\end{bmatrix} =
\begin{bmatrix}
f & 0 & 0 & 0 \\
0 & f & 0 & 0 \\
0 & 0 & 1 & 0
\end{bmatrix}
\begin{bmatrix}
X \\
Y \\
Z \\
1
\end{bmatrix}
$$

La matriz:

$$
\begin{bmatrix}
f & 0 & 0 & 0 \\
0 & f & 0 & 0 \\
0 & 0 & 1 & 0
\end{bmatrix}
$$

es una matriz de proyección $3 \times 4$.

Si multiplicamos:

$$
\begin{bmatrix}
fX \\
fY \\
Z
\end{bmatrix}
$$

y recordamos que en homogéneas hay que dividir entre la última coordenada, obtenemos:

$$
x = \frac{fX}{Z}
$$

$$
y = \frac{fY}{Z}
$$

Por tanto:

$$
\tilde{m}
\sim
\begin{bmatrix}
f & 0 & 0 & 0 \\
0 & f & 0 & 0 \\
0 & 0 & 1 & 0
\end{bmatrix}
\tilde{M}
$$

---

<img width="1090" height="657" alt="image" src="https://github.com/user-attachments/assets/715f5828-d50d-4ae5-961d-8eda6459fd37" />

---

# 6. Homografía 2D en visión por computador

Aquí se estudia la [homografía](https://github.com/IvanCS-Chenfu/M-todos-Matem-ticos/wiki/Matrices-de-Transformaci%C3%B3n#64-homograf%C3%ADa) en visión por computador.

Una homografía 2D es una transformación proyectiva entre planos:

$$
\tilde{x}' \sim H \tilde{x}
$$

donde:

$$
H \in \mathbb{R}^{3 \times 3}
$$

En visión por computador, una homografía aparece cuando existe una relación proyectiva entre dos imágenes, o entre un plano del mundo y una imagen.

---

# 6.1 Homografía como transformación entre planos

Una homografía transforma puntos de un plano en puntos de otro plano.

En coordenadas homogéneas:

$$
\lambda
\begin{bmatrix}
x' \\
y' \\
1
\end{bmatrix} =
H
\begin{bmatrix}
x \\
y \\
1
\end{bmatrix}
$$

La matriz $H$ está definida salvo escala.

Es decir:

$$
H
$$

y:

$$
\alpha H
$$

representan la misma transformación proyectiva si:

$$
\alpha \neq 0
$$

En visión por computador, esto es útil porque una imagen es un plano, y muchas superficies del mundo también pueden aproximarse como planos.

Por ejemplo:

- una pared,
- una hoja de papel,
- una pizarra,
- una carretera plana,
- el suelo,
- una pista deportiva,
- un tablero de calibración.

Si todos los puntos observados pertenecen a un mismo plano, la relación entre ese plano y su imagen se puede describir mediante una homografía.

---

<img width="692" height="585" alt="image" src="https://github.com/user-attachments/assets/b24bead3-5875-404f-ba32-db967fe45290" />

---

# 6.2 Cuándo aparece una homografía entre imágenes

Aparece una homografía entre imágenes en varios casos importantes:

1. Cámara fija con diferentes planos imagen.
2. Cámara rotando observando una escena no plana.
3. Cámara moviéndose observando un plano.
4. Cámara moviéndose observando una escena no plana, donde no existe una única homografía global, pero sí pueden existir homografías locales por cada plano de la escena.

---

<img width="1153" height="532" alt="image" src="https://github.com/user-attachments/assets/a0ffe260-94ab-4fe2-97f9-b377a66aa3ce" />

---

# 6.3 Cámara fija y cambio de plano imagen

Si la cámara no cambia su centro óptico, pero cambia el plano imagen, la relación entre las imágenes puede modelarse como una homografía.

Un ejemplo sencillo es el **zoom**.

Si una imagen se escala uniformemente, se puede escribir:

$$
H =
\begin{bmatrix}
s & 0 & 0 \\
0 & s & 0 \\
0 & 0 & 1
\end{bmatrix}
$$

donde $s$ es el factor de zoom.

Aplicando:

$$
\tilde{x}' = H\tilde{x}
$$

obtenemos:

$$
x' = sx
$$

$$
y' = sy
$$

Esto es una homografía muy simple.

Aunque aquí no hay una deformación proyectiva compleja, sigue siendo un caso particular de homografía.

---

# 6.4 Cámara rotando sobre su centro óptico

Otro caso importante ocurre cuando la cámara rota, pero su centro óptico permanece fijo.

Esto sucede, por ejemplo, al hacer una panorámica girando la cámara desde un mismo punto.

En este caso, aunque la escena no sea plana, los rayos de proyección siguen pasando por el mismo centro óptico.

La cámara cambia su orientación, por lo que los rayos cortan el nuevo plano imagen en posiciones distintas, pero la relación entre las dos imágenes puede describirse mediante una homografía.

Este es el principio usado en muchas aplicaciones de **image stitching** o creación de panoramas.

La condición importante es:

> La cámara puede rotar, pero el centro óptico no debe trasladarse de forma significativa.

Si la cámara se traslada mucho y la escena no es plana, una única homografía ya no describe correctamente la relación entre las imágenes.

---

<img width="1202" height="425" alt="image" src="https://github.com/user-attachments/assets/68418677-213f-439c-9071-2deb0aab9dc1" />

---

# 6.5 Cámara moviéndose observando un plano

Si la cámara se mueve, pero todos los puntos observados pertenecen a un mismo plano de la escena, entonces también existe una homografía entre las imágenes.

Supongamos un plano 3D de la escena.

La primera cámara observa el plano y define una homografía:

$$
x_1 = H_1 x
$$

La segunda cámara observa el mismo plano y define:

$$
x_2 = H_2 x
$$

donde:

- $x$ es un punto del plano de la escena.
- $x_1$ es su imagen en la primera cámara.
- $x_2$ es su imagen en la segunda cámara.

Si queremos relacionar directamente $x_1$ con $x_2$, despejamos:

$$
x = H_1^{-1}x_1
$$

y sustituimos:

$$
x_2 = H_2 H_1^{-1} x_1
$$

Por tanto, la homografía entre la imagen 1 y la imagen 2 es:

$$
H_{12} = H_2 H_1^{-1}
$$

y:

$$
x_2 = H_{12}x_1
$$

Este resultado es muy importante en visión por computador.

Permite relacionar dos imágenes distintas de un mismo plano aunque la cámara se haya movido.

---

<img width="822" height="575" alt="image" src="https://github.com/user-attachments/assets/d597a0c7-b321-4045-81a5-da14f170069a" />

---

# 6.6 Escenas no planas

Si la cámara se mueve y la escena no es plana, en general no existe una única homografía que relacione todos los puntos de una imagen con todos los puntos de la otra.

Esto se debe a que los puntos tienen diferentes profundidades.

Una homografía puede explicar correctamente la transformación de puntos que pertenecen a un mismo plano, pero no de toda una escena 3D arbitraria.

En una escena no plana puede haber varias homografías, una por cada plano dominante.

Por ejemplo:

- una pared puede tener una homografía,
- el suelo otra,
- una mesa otra,
- una pizarra otra.

Por tanto, para escenas no planas con cámara en movimiento:

$$
\text{una única homografía global no suele ser suficiente}
$$

pero:

$$
\text{pueden existir homografías locales por planos}
$$

---

<img width="430" height="461" alt="image" src="https://github.com/user-attachments/assets/0d779b32-a6e5-4a8a-ac06-90ed58629932" />

---

# 6.7 Estimación de una homografía: DLT

En la práctica, muchas veces no conocemos la matriz $H$ y queremos estimarla a partir de correspondencias entre puntos.

Supongamos que tenemos pares de puntos correspondientes:

$$
x_i \leftrightarrow x'_i
$$

donde:

$$
x_i =
\begin{bmatrix}
x_i \\
y_i \\
1
\end{bmatrix}
$$

y:

$$
x'_i =
\begin{bmatrix}
x'_i \\
y'_i \\
1
\end{bmatrix}
$$

La homografía cumple:

$$
\lambda_i x'_i = Hx_i
$$

Como $H$ tiene 8 grados de libertad, hacen falta al menos 4 correspondencias de puntos.

Cada correspondencia aporta dos ecuaciones independientes.

Por tanto:

$$
4 \text{ puntos} \times 2 \text{ ecuaciones por punto} = 8 \text{ ecuaciones}
$$

Esto permite resolver los 8 grados de libertad de la homografía.

---

## Sistema homogéneo

El método DLT, **Direct Linear Transformation**, plantea un sistema de la forma:

$$
Ah = 0
$$

donde:

- $A$ es una matriz construida a partir de las correspondencias.
- $h$ es un vector que contiene los 9 elementos de $H$ apilados.
- La solución se busca salvo escala.

El vector:

$$
h =
\begin{bmatrix}
h_{00} \\
h_{01} \\
h_{02} \\
h_{10} \\
h_{11} \\
h_{12} \\
h_{20} \\
h_{21} \\
h_{22}
\end{bmatrix}
$$

representa la matriz:

$$
H =
\begin{bmatrix}
h_{00} & h_{01} & h_{02} \\
h_{10} & h_{11} & h_{12} \\
h_{20} & h_{21} & h_{22}
\end{bmatrix}
$$

Como $H$ está definida salvo escala, no interesa la solución trivial:

$$
h = 0
$$

Por eso se impone una restricción, por ejemplo:

$$
\|h\| = 1
$$

Entonces se resuelve:

$$
\arg\min_h \|Ah\|^2
$$

sujeto a:

$$
\|h\| = 1
$$

La solución se obtiene como el vector singular asociado al menor valor singular de $A$.

En la práctica, se usa SVD:

$$
A = U\Sigma V^T
$$

y la solución $h$ es la última columna de $V$.

---

## Casos según el número de puntos

Si hay menos de 4 correspondencias independientes:

$$
n < 4
$$

el sistema no está suficientemente restringido y existen infinitas soluciones.

Si hay exactamente 4 correspondencias independientes:

$$
n = 4
$$

se puede obtener una solución exacta en ausencia de ruido.

Si hay más de 4 correspondencias:

$$
n > 4
$$

normalmente no existe una solución exacta debido al ruido de las medidas, y se busca la solución de mínimos cuadrados.

Usar más puntos suele mejorar la robustez.

---

# 6.8 Homografía de rectas

Una homografía no solo transforma puntos.

También transforma rectas.

Si los puntos se transforman como:

$$
x' = Hx
$$

entonces las rectas se transforman como:

$$
l' = H^{-T}l
$$

Esta expresión aparece porque una recta se define por la condición:

$$
l^T x = 0
$$

Si:

$$
x' = Hx
$$

entonces:

$$
x = H^{-1}x'
$$

Sustituyendo en la ecuación de la recta:

$$
l^T H^{-1}x' = 0
$$

Esto puede escribirse como:

$$
(H^{-T}l)^T x' = 0
$$

Por tanto:

$$
l' = H^{-T}l
$$

Esta propiedad es útil en rectificación de imágenes y análisis geométrico.

---

## Ejemplo conceptual

Supongamos que rectificamos una imagen de una superficie plana, como una pista, una pizarra o una carretera.

En la imagen rectificada definimos una recta vertical sencilla:

$$
l' =
\begin{bmatrix}
1 \\
0 \\
-136
\end{bmatrix}
$$

Eso representa una recta del tipo:

$$
x' - 136 = 0
$$

Si queremos saber qué recta corresponde en la imagen original, usamos:

$$
l = H^T l'
$$

o, según la dirección concreta de transformación usada, la relación inversa correspondiente.

La idea importante es que las rectas también se transforman mediante matrices relacionadas con $H$.

---

<img width="1043" height="617" alt="image" src="https://github.com/user-attachments/assets/9c27b13e-8b34-4ce3-bd78-6677a596de35" />

<img width="1261" height="705" alt="image" src="https://github.com/user-attachments/assets/f055754a-3882-41fe-b244-9e2ce2ab9de8" />

---

# 6.9 Puntos en el infinito en homografías

En coordenadas homogéneas, un punto con última coordenada cero representa un [punto en el infinito](https://github.com/IvanCS-Chenfu/M-todos-Matem-ticos/wiki/Matrices-de-Transformaci%C3%B3n#54-qu%C3%A9-significa-que-la-%C3%BAltima-coordenada-sea-0).

Por ejemplo:

$$
\begin{bmatrix}
a \\
b \\
0
\end{bmatrix}
$$

no representa un punto finito del plano, sino una dirección.

En visión por computador, los puntos en el infinito están relacionados con los puntos de fuga.

Por ejemplo, las vías de un tren son paralelas en el mundo real, pero en la imagen parecen converger en un punto.

Ese punto de convergencia es la imagen de una dirección en el infinito.

---

## Interpretación con una homografía

Una homografía puede transformar puntos finitos en puntos en el infinito, o puntos en el infinito en puntos finitos.

Esto explica muchos efectos de perspectiva.

Por ejemplo, en una imagen de unas vías de tren:

- las rectas paralelas del mundo real se cortan visualmente en un punto de fuga,
- ese punto de fuga representa una dirección,
- en coordenadas homogéneas puede interpretarse como la imagen de un punto en el infinito.

En una transformación proyectiva, el paralelismo no se conserva necesariamente.

Por eso una homografía puede convertir un rectángulo en un trapecio, o un trapecio en un rectángulo.

---

<img width="331" height="257" alt="image" src="https://github.com/user-attachments/assets/9f289931-f3cf-4649-8cee-ca9123138fb3" />

<img width="470" height="268" alt="image" src="https://github.com/user-attachments/assets/9fa87686-7d3b-47aa-badb-db4d3f41189d" />

<img width="638" height="97" alt="image" src="https://github.com/user-attachments/assets/2af02bfb-336b-470d-9a79-1b952376dedd" />

<img width="331" height="92" alt="image" src="https://github.com/user-attachments/assets/dae38096-684a-4001-bbab-7634ec391094" />


---

# 7. Del plano sensor a la matriz imagen

# 7.1 Por qué hace falta esta transformación

El modelo pinhole proyecta un punto 3D sobre el plano sensor:

$$
M_C
\longrightarrow
m =
\begin{bmatrix}
x \\
y
\end{bmatrix}
$$

Pero estas coordenadas $(x,y)$ están en el plano sensor y se interpretan en unidades métricas.

Por ejemplo:

$$
x = 0.00012 \text{ m}
$$

$$
y = 0.00024 \text{ m}
$$

Sin embargo, una imagen digital no se almacena en metros.

Se almacena como una matriz de píxeles.

Por tanto necesitamos transformar:

$$
\begin{bmatrix}
x \\
y
\end{bmatrix}
\longrightarrow
\begin{bmatrix}
u \\
v
\end{bmatrix}
$$

donde $(u,v)$ son coordenadas en píxeles.

---

# 7.2 Coordenadas métricas y coordenadas en píxeles

El punto en el sensor:

$$
m =
\begin{bmatrix}
x \\
y
\end{bmatrix}
$$

se mide en metros.

El punto en la imagen digital:

$$
m' =
\begin{bmatrix}
u \\
v
\end{bmatrix}
$$

se mide en píxeles.

La conversión entre ambos sistemas depende de:

- el tamaño físico de los píxeles,
- la posición del centro principal,
- la orientación de los ejes de la imagen,
- la posible falta de perpendicularidad entre los ejes.

En el caso más habitual, se considera que los ejes de la matriz imagen son casi perpendiculares.

Entonces el modelo se simplifica bastante.

---

# 7.3 Matriz de conversión sensor-imagen

La transformación del plano sensor a la matriz imagen puede escribirse en homogéneas como:

$$
\tilde{m}' = K_s \tilde{m}
$$

donde:

$$
\tilde{m} =
\begin{bmatrix}
x \\
y \\
1
\end{bmatrix}
$$

y:

$$
\tilde{m}' =
\begin{bmatrix}
u \\
v \\
1
\end{bmatrix}
$$

La matriz general es:

$$
K_s =
\begin{bmatrix}
k_x & s & u_0 \\
0 & k_y & v_0 \\
0 & 0 & 1
\end{bmatrix}
$$

Entonces:

$$
\begin{bmatrix}
u \\
v \\
1
\end{bmatrix} =
\begin{bmatrix}
k_x & s & u_0 \\
0 & k_y & v_0 \\
0 & 0 & 1
\end{bmatrix}
\begin{bmatrix}
x \\
y \\
1
\end{bmatrix}
$$

Al multiplicar:

$$
u = k_x x + s y + u_0
$$

$$
v = k_y y + v_0
$$

Si el skew se considera despreciable:

$$
s \approx 0
$$

entonces:

$$
K_s \approx
\begin{bmatrix}
k_x & 0 & u_0 \\
0 & k_y & v_0 \\
0 & 0 & 1
\end{bmatrix}
$$

y:

$$
u = k_x x + u_0
$$

$$
v = k_y y + v_0
$$

---

# 7.4 Centro principal

El punto:

$$
(u_0,v_0)
$$

es el **centro principal** de la imagen.

Representa la posición en píxeles donde el eje óptico corta el plano imagen.

Idealmente, podría coincidir con el centro de la imagen.

Pero en cámaras reales no siempre coincide exactamente.

Por eso se incluye como parámetro de la cámara.

La conversión:

$$
u = k_x x + u_0
$$

$$
v = k_y y + v_0
$$

muestra que aunque el punto proyectado tenga coordenadas sensor:

$$
x=0,\quad y=0
$$

su coordenada de píxel será:

$$
u = u_0
$$

$$
v = v_0
$$

Es decir, el origen del plano sensor no tiene por qué coincidir con la esquina superior izquierda de la imagen.

---

# 7.5 Skew

El parámetro $s$ representa la posible falta de perpendicularidad entre los ejes del sensor.

La forma general es:

$$
K_s =
\begin{bmatrix}
k_x & s & u_0 \\
0 & k_y & v_0 \\
0 & 0 & 1
\end{bmatrix}
$$

Si los ejes son perfectamente perpendiculares:

$$
s = 0
$$

En cámaras modernas, normalmente:

$$
s \approx 0
$$

Por eso muchas veces se utiliza:

$$
K_s =
\begin{bmatrix}
k_x & 0 & u_0 \\
0 & k_y & v_0 \\
0 & 0 & 1
\end{bmatrix}
$$

---

# 7.6 Distancia focal en píxeles

En el modelo pinhole, la distancia focal $f$ aparece en unidades métricas.

Por ejemplo:

$$
f = 0.003 \text{ m}
$$

Pero al pasar a píxeles aparece combinada con los factores de conversión $k_x$ y $k_y$.

Definimos:

$$
s_x = f k_x
$$

$$
s_y = f k_y
$$

Estos valores representan la distancia focal medida en píxeles.

Por eso, en visión por computador, la matriz intrínseca suele escribirse como:

$$
K =
\begin{bmatrix}
s_x & s & u_0 \\
0 & s_y & v_0 \\
0 & 0 & 1
\end{bmatrix}
$$

o, si $s=0$:

$$
K =
\begin{bmatrix}
s_x & 0 & u_0 \\
0 & s_y & v_0 \\
0 & 0 & 1
\end{bmatrix}
$$

donde:

- $s_x$ es la distancia focal en píxeles en el eje horizontal.
- $s_y$ es la distancia focal en píxeles en el eje vertical.
- $(u_0,v_0)$ es el centro principal.
- $s$ es el skew.

---

<img width="1234" height="292" alt="image" src="https://github.com/user-attachments/assets/6fc2dc9b-379b-4212-8de5-664588ba6a54" />

<img width="1184" height="602" alt="image" src="https://github.com/user-attachments/assets/aa8fc334-4c5a-4be4-9766-e2aeb15b3bb0" />

---

# 8. Modelo completo de cámara

# 8.1 Por qué el modelo pinhole aislado no basta

El modelo pinhole básico describe la proyección:

$$
M_C
\longrightarrow
m
$$

es decir, desde coordenadas de cámara al plano sensor.

Pero en la práctica tenemos dos problemas:

1. El punto 3D suele estar expresado en el sistema del mundo, no en el sistema de la cámara.
2. El punto observado en la imagen está en píxeles, no en coordenadas métricas del sensor.

Por tanto, el modelo pinhole aislado no basta.

Necesitamos añadir:

1. Una transformación 3D → 3D del mundo a la cámara.
2. Una transformación 2D → 2D del plano sensor a la matriz imagen.

El modelo completo queda:

$$
M_W
\longrightarrow
M_C
\longrightarrow
m
\longrightarrow
m'
$$

---

<img width="1058" height="458" alt="image" src="https://github.com/user-attachments/assets/ba8eaf53-5223-43fd-b661-eed814921b8c" />

---

# 8.2 Parámetros extrínsecos

Los parámetros extrínsecos son:

$$
R
$$

y:

$$
t
$$

Describen cómo pasar del sistema mundo al sistema cámara:

$$
M_C = R M_W + t
$$

En homogéneas:

$$
\tilde{M}_C =
\begin{bmatrix}
R & t \\
0_3^T & 1
\end{bmatrix}
\tilde{M}_W
$$

La matriz:

$$
D =
\begin{bmatrix}
R & t \\
0_3^T & 1
\end{bmatrix}
$$

representa la pose de la cámara respecto al mundo.

---

# 8.3 Parámetros intrínsecos

Los parámetros intrínsecos describen cómo la cámara transforma puntos del plano sensor en coordenadas de imagen.

La matriz intrínseca es:

$$
K =
\begin{bmatrix}
s_x & s & u_0 \\
0 & s_y & v_0 \\
0 & 0 & 1
\end{bmatrix}
$$

En el caso más habitual:

$$
s = 0
$$

y queda:

$$
K =
\begin{bmatrix}
s_x & 0 & u_0 \\
0 & s_y & v_0 \\
0 & 0 & 1
\end{bmatrix}
$$

Los parámetros intrínsecos son:

- $s_x$: distancia focal en píxeles en dirección horizontal.
- $s_y$: distancia focal en píxeles en dirección vertical.
- $u_0$: coordenada horizontal del centro principal.
- $v_0$: coordenada vertical del centro principal.
- $s$: skew entre ejes.

---

# 8.4 Matriz de proyección de la cámara

El modelo completo combina:

1. Transformación mundo-cámara.
2. Proyección pinhole.
3. Conversión a píxeles.

En forma compacta:

$$
\lambda \tilde{m}' = K [R|t] \tilde{M}_W
$$

donde:

$$
\tilde{m}' =
\begin{bmatrix}
u \\
v \\
1
\end{bmatrix}
$$

y:

$$
\tilde{M}_W =
\begin{bmatrix}
X_W \\
Y_W \\
Z_W \\
1
\end{bmatrix}
$$

La matriz:

$$
P = K[R|t]
$$

se llama matriz de proyección de la cámara.

Tiene tamaño:

$$
3 \times 4
$$

Por tanto:

$$
\lambda
\begin{bmatrix}
u \\
v \\
1
\end{bmatrix} =
P
\begin{bmatrix}
X_W \\
Y_W \\
Z_W \\
1
\end{bmatrix}
$$

Escrita completa:

$$
\lambda
\begin{bmatrix}
u \\
v \\
1
\end{bmatrix} =
\begin{bmatrix}
p_{11} & p_{12} & p_{13} & p_{14} \\
p_{21} & p_{22} & p_{23} & p_{24} \\
p_{31} & p_{32} & p_{33} & p_{34}
\end{bmatrix}
\begin{bmatrix}
X_W \\
Y_W \\
Z_W \\
1
\end{bmatrix}
$$

Esta es una de las ecuaciones más importantes de la geometría de cámaras.

---

<img width="1111" height="552" alt="image" src="https://github.com/user-attachments/assets/73b35a24-f4c5-4e07-a53f-e7be8eff6088" />

<img width="1210" height="424" alt="image" src="https://github.com/user-attachments/assets/87d67a32-c6c7-4d22-b18f-2db019f2ec69" />

---

# 8.5 Ecuaciones no lineales resultantes

Aunque el modelo se escriba de forma matricial homogénea, al volver a coordenadas cartesianas aparecen divisiones.

De la ecuación:

$$
\lambda
\begin{bmatrix}
u \\
v \\
1
\end{bmatrix} =
P
\begin{bmatrix}
X_W \\
Y_W \\
Z_W \\
1
\end{bmatrix}
$$

obtenemos:

$$
\lambda u =
p_{11}X_W + p_{12}Y_W + p_{13}Z_W + p_{14}
$$

$$
\lambda v =
p_{21}X_W + p_{22}Y_W + p_{23}Z_W + p_{24}
$$

$$
\lambda =
p_{31}X_W + p_{32}Y_W + p_{33}Z_W + p_{34}
$$

Dividiendo:

$$
u =
\frac{
p_{11}X_W + p_{12}Y_W + p_{13}Z_W + p_{14}
}{
p_{31}X_W + p_{32}Y_W + p_{33}Z_W + p_{34}
}
$$

$$
v =
\frac{
p_{21}X_W + p_{22}Y_W + p_{23}Z_W + p_{24}
}{
p_{31}X_W + p_{32}Y_W + p_{33}Z_W + p_{34}
}
$$

Estas ecuaciones son no lineales en coordenadas cartesianas debido a la división por la tercera coordenada homogénea.

Este es exactamente el comportamiento proyectivo de una cámara.

---

# 8.6 Grados de libertad

La matriz de proyección:

$$
P \in \mathbb{R}^{3 \times 4}
$$

tiene 12 elementos.

Pero como trabaja en coordenadas homogéneas, está definida salvo escala.

Por tanto, tiene:

$$
12 - 1 = 11
$$

grados de libertad.

Esto significa que:

$$
P
$$

y:

$$
\alpha P
$$

representan la misma cámara proyectiva si:

$$
\alpha \neq 0
$$

La matriz $P$ puede entenderse como el modelo proyectivo completo de una cámara ideal sin distorsión.

---

# 9. Distorsión radial

El modelo pinhole ideal supone que los rayos se proyectan perfectamente según el modelo perspectiva.

Pero las cámaras reales tienen lentes, y las lentes introducen distorsión.

Una de las distorsiones más importantes es la **distorsión radial**.

La distorsión radial desplaza los puntos de la imagen según su distancia al centro.

Si:

$$
r^2 = x^2 + y^2
$$

un modelo sencillo de distorsión radial es:

$$
x_d =
(1 + k_1r^2 + k_2r^4)x
$$

$$
y_d =
(1 + k_1r^2 + k_2r^4)y
$$

donde:

- $(x,y)$ son las coordenadas sin distorsión.
- $(x_d,y_d)$ son las coordenadas distorsionadas.
- $k_1$ y $k_2$ son coeficientes de distorsión radial.
- $r$ es la distancia al centro de la imagen.

Esta transformación no es una homografía.

En el esquema final del temario se remarca que la distorsión de lente es la única transformación del modelo completo que no se representa como una homografía o matriz proyectiva simple.

---

<img width="1249" height="564" alt="image" src="https://github.com/user-attachments/assets/d59e9407-6dd2-43b7-b2b8-eb7c05eb6b67" />

---

# 10. Resumen final

La formación geométrica de imágenes describe cómo un punto 3D acaba convirtiéndose en un píxel de una imagen.

El proceso completo es:

$$
M_W
\longrightarrow
M_C
\longrightarrow
m
\longrightarrow
m'
$$

donde:

1. $M_W$ es el punto en coordenadas del mundo.
2. $M_C$ es el punto en coordenadas de cámara.
3. $m$ es la proyección en el plano sensor.
4. $m'$ es la coordenada final en píxeles.

Las tres transformaciones principales son:

| Transformación | Descripción | Modelo |
|---|---|---|
| 3D → 3D | Mundo a cámara | $M_C = RM_W + t$ |
| 3D → 2D | Proyección pinhole | $x=fX_C/Z_C$, $y=fY_C/Z_C$ |
| 2D → 2D | Sensor a píxeles | $\tilde{m}' = K_s\tilde{m}$ |

El modelo completo de cámara se escribe como:

$$
\lambda \tilde{m}' = K[R|t]\tilde{M}_W
$$

donde:

$$
P = K[R|t]
$$

es la matriz de proyección de la cámara.

Los parámetros se dividen en:

| Tipo | Parámetros | Significado |
|---|---|---|
| Extrínsecos | $R,t$ | Posición y orientación de la cámara respecto al mundo |
| Intrínsecos | $K$ | Propiedades internas de la cámara y conversión a píxeles |

La matriz intrínseca suele tener la forma:

$$
K =
\begin{bmatrix}
s_x & s & u_0 \\
0 & s_y & v_0 \\
0 & 0 & 1
\end{bmatrix}
$$

y, si el skew se desprecia:

$$
K =
\begin{bmatrix}
s_x & 0 & u_0 \\
0 & s_y & v_0 \\
0 & 0 & 1
\end{bmatrix}
$$

La proyección perspectiva es no lineal en coordenadas cartesianas porque implica divisiones por profundidad, pero puede escribirse de forma compacta usando coordenadas homogéneas.

Las homografías aparecen en visión por computador cuando existe una relación proyectiva entre planos, especialmente en:

- imágenes de planos,
- panoramas,
- rotaciones puras de cámara,
- rectificación de imágenes,
- stitching,
- estimación de transformaciones entre vistas.

Por último, las cámaras reales pueden incluir distorsión radial:

$$
x_d =
(1 + k_1r^2 + k_2r^4)x
$$

$$
y_d =
(1 + k_1r^2 + k_2r^4)y
$$

que debe modelarse aparte porque no es una transformación proyectiva lineal homogénea.

La ecuación central de todo el tema es:

$$
\boxed{
\lambda \tilde{m}' = K[R|t]\tilde{M}_W
}
$$

Esta ecuación resume el paso desde un punto 3D del mundo hasta su posición 2D en la imagen.