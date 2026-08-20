# Índice

- [0. Introducción](#0-introducción)

- [1. Qué significa calibrar una cámara](#1-qué-significa-calibrar-una-cámara)
  - [1.1 Parámetros extrínsecos](#11-parámetros-extrínsecos)
  - [1.2 Parámetros intrínsecos](#12-parámetros-intrínsecos)
  - [1.3 Matriz de proyección](#13-matriz-de-proyección)

- [2. Distorsión de lente](#2-distorsión-de-lente)
  - [2.1 Por qué aparece la distorsión](#21-por-qué-aparece-la-distorsión)
  - [2.2 Distorsión radial](#22-distorsión-radial)
  - [2.3 Distorsión en coordenadas de píxel](#23-distorsión-en-coordenadas-de-píxel)
  - [2.4 Distorsión de barril y de cojín](#24-distorsión-de-barril-y-de-cojín)
  - [2.5 La distorsión no es una homografía](#25-la-distorsión-no-es-una-homografía)

- [3. Cámara calibrada y cámara no calibrada](#3-cámara-calibrada-y-cámara-no-calibrada)
  - [3.1 Cámara calibrada](#31-cámara-calibrada)
  - [3.2 Cámara no calibrada](#32-cámara-no-calibrada)

- [4. Procedimiento general de calibración](#4-procedimiento-general-de-calibración)
  - [4.1 Paso 1: proporcionar puntos 3D conocidos](#41-paso-1-proporcionar-puntos-3d-conocidos)
  - [4.2 Paso 2: detectar las proyecciones en la imagen](#42-paso-2-detectar-las-proyecciones-en-la-imagen)
  - [4.3 Paso 3: aplicar el modelo de cámara](#43-paso-3-aplicar-el-modelo-de-cámara)
  - [4.4 Paso 4: aplicar el modelo de distorsión](#44-paso-4-aplicar-el-modelo-de-distorsión)

- [5. Error de reproyección](#5-error-de-reproyección)

- [6. Método DLT para calibración](#6-método-dlt-para-calibración)
  - [6.1 Modelo usado por DLT](#61-modelo-usado-por-dlt)
  - [6.2 Ecuaciones lineales del DLT](#62-ecuaciones-lineales-del-dlt)
  - [6.3 Sistema homogéneo](#63-sistema-homogéneo)
  - [6.4 Descomposición de P en K, R y t](#64-descomposición-de-p-en-k-r-y-t)
  - [6.5 Factorización de B](#65-factorización-de-b)
  - [6.6 Ambigüedad de signo](#66-ambigüedad-de-signo)
  - [6.7 Limitaciones del método DLT](#67-limitaciones-del-método-dlt)

- [7. Método de Zhang](#7-método-de-zhang)
  - [7.1 Idea principal del método](#71-idea-principal-del-método)
  - [7.2 Por qué se necesitan varias imágenes](#72-por-qué-se-necesitan-varias-imágenes)

- [8. Procedimiento del método de Zhang](#8-procedimiento-del-método-de-zhang)
  - [8.1 Adquisición de datos](#81-adquisición-de-datos)
  - [8.2 Paso 1: solución cerrada para K, R y t](#82-paso-1-solución-cerrada-para-k-r-y-t)
  - [8.3 Restricciones geométricas usadas por Zhang](#83-restricciones-geométricas-usadas-por-zhang)
  - [8.4 Cálculo de R y t a partir de H](#84-cálculo-de-r-y-t-a-partir-de-h)
  - [8.5 Por qué la solución cerrada no es exacta](#85-por-qué-la-solución-cerrada-no-es-exacta)

- [9. Estimación de la distorsión en Zhang](#9-estimación-de-la-distorsión-en-zhang)
- [10. Refinamiento no lineal](#10-refinamiento-no-lineal)

- [11. Número mínimo de imágenes en Zhang](#11-número-mínimo-de-imágenes-en-zhang)

- [12. Comparación entre DLT y Zhang](#12-comparación-entre-dlt-y-zhang)

- [13. Interpretación conceptual](#13-interpretación-conceptual)
  - [13.1 Cómo es la cámara por dentro](#131-cómo-es-la-cámara-por-dentro)
  - [13.2 Dónde estaba la cámara en cada imagen](#132-dónde-estaba-la-cámara-en-cada-imagen)
  - [13.3 Cómo de deformada está la imagen](#133-cómo-de-deformada-está-la-imagen)
  - [13.4 Qué tan buena es la calibración](#134-qué-tan-buena-es-la-calibración)

- [14. Relación con la formación de imágenes](#14-relación-con-la-formación-de-imágenes)

- [15. Resumen final](#15-resumen-final)

---

# 0. Introducción

En la página de [Formación de Imágenes](https://github.com/IvanCS-Chenfu/OpenCV/wiki/Formaci%C3%B3n-de-Im%C3%A1genes) se estudia cómo una cámara transforma un punto tridimensional del mundo en una posición bidimensional de la imagen.

De forma resumida, el modelo geométrico completo puede escribirse como:

$$
\lambda \tilde{m}' = K [R|t] \tilde{M}_W
$$

donde:

- $\tilde{M}_W$ es un punto 3D del mundo en coordenadas homogéneas.
- $\tilde{m}'$ es el punto proyectado en la imagen, expresado en píxeles y coordenadas homogéneas.
- $R$ y $t$ son los **parámetros extrínsecos**.
- $K$ es la **matriz de parámetros intrínsecos**.
- $\lambda$ es un factor de escala homogéneo.

Esta ecuación ya se explica en la sección [8.4 Matriz de proyección de la cámara](https://github.com/IvanCS-Chenfu/OpenCV/wiki/Formaci%C3%B3n-de-Im%C3%A1genes#84-matriz-de-proyección-de-la-cámara).

La **calibración de la cámara** aparece como el problema inverso: si conocemos puntos 3D del mundo y somos capaces de detectar sus proyecciones en la imagen, queremos estimar los parámetros de la cámara que explican esa proyección.

Es decir, en formación de imágenes se parte de:

$$
K, R, t, M_W
\quad \longrightarrow \quad
m'
$$

mientras que en calibración se plantea el problema:

$$
M_W, m'
\quad \longrightarrow \quad
K, R, t
$$

y, además, en cámaras reales también se estiman los parámetros de distorsión de la lente:

$$
k_1, k_2
$$

Por tanto, la calibración de cámara es el proceso mediante el cual se calculan los parámetros que intervienen en el modelo de cámara:

$$
K, R, t, k_1, k_2
$$

En muchos textos este proceso también se conoce como **camera resectioning**, porque consiste en recuperar la cámara a partir de correspondencias entre puntos 3D y sus proyecciones 2D.

---

# 1. Qué significa calibrar una cámara

Calibrar una cámara significa encontrar los parámetros que permiten relacionar correctamente el mundo 3D con la imagen 2D capturada por la cámara.

En el modelo ideal sin distorsión, el proceso completo es:

$$
M_W \longrightarrow M_C \longrightarrow m \longrightarrow m'
$$

donde:

- $M_W$ es el punto expresado en el sistema del mundo.
- $M_C$ es el mismo punto expresado en el sistema de la cámara.
- $m$ es el punto proyectado sobre el plano sensor.
- $m'$ es el punto final en coordenadas de imagen, normalmente píxeles.

Este proceso coincide con el descrito en [2. El proceso geométrico completo](https://github.com/IvanCS-Chenfu/OpenCV/wiki/Formaci%C3%B3n-de-Im%C3%A1genes#2-el-proceso-geométrico-completo).

La calibración intenta estimar los parámetros de cada una de esas transformaciones.

---

## 1.1 Parámetros extrínsecos

Los parámetros extrínsecos describen la posición y orientación de la cámara respecto al sistema de coordenadas del mundo.

Están formados por:

$$
R
$$

y:

$$
t
$$

donde:

- $R$ es una matriz de rotación $3 \times 3$.
- $t$ es un vector de traslación $3 \times 1$.

Permiten transformar un punto desde coordenadas del mundo a coordenadas de cámara:

$$
M_C = R M_W + t
$$

En coordenadas homogéneas:

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

representa la transformación rígida entre el sistema del mundo y el sistema de la cámara.

Estos parámetros dependen de la posición de la cámara. Si la cámara se mueve, cambian $R$ y $t$.

Por eso, cuando se habla de calibrar una cámara de forma práctica, normalmente se está más interesado en encontrar los parámetros que son propios de la cámara, es decir, los intrínsecos y la distorsión. Sin embargo, durante el proceso de calibración también se calculan los extrínsecos de cada imagen usada.

---

## 1.2 Parámetros intrínsecos

Los parámetros intrínsecos describen las propiedades internas de la cámara y la conversión entre coordenadas del plano sensor y coordenadas de imagen.

La matriz intrínseca suele escribirse como:

$$
K =
\begin{bmatrix}
s_x & 0 & u_0 \\
0 & s_y & v_0 \\
0 & 0 & 1
\end{bmatrix}
$$

donde:

- $s_x$ es la distancia focal expresada en píxeles en el eje horizontal.
- $s_y$ es la distancia focal expresada en píxeles en el eje vertical.
- $(u_0, v_0)$ son las coordenadas del punto principal en la imagen.
- El término de skew se suele considerar cero en el modelo simplificado.

En otros textos se puede ver una notación similar:

$$
K =
\begin{bmatrix}
f_x & \gamma & c_x \\
0 & f_y & c_y \\
0 & 0 & 1
\end{bmatrix}
$$

donde:

- $f_x$ y $f_y$ equivalen a las focales en píxeles.
- $(c_x,c_y)$ equivalen al punto principal.
- $\gamma$ representa el skew o falta de perpendicularidad entre los ejes de la imagen.

Nosotros utilizaremos la notación:

$$
K =
\begin{bmatrix}
s_x & 0 & u_0 \\
0 & s_y & v_0 \\
0 & 0 & 1
\end{bmatrix}
$$

asumiendo skew nulo.

---

## 1.3 Matriz de proyección

El modelo completo sin distorsión se puede escribir como:

$$
\lambda \tilde{m}' = K [R|t] \tilde{M}_W
$$

Si definimos:

$$
P = K [R|t]
$$

entonces:

$$
\lambda \tilde{m}' = P \tilde{M}_W
$$

La matriz $P$ se llama **matriz de proyección de la cámara**.

Tiene tamaño:

$$
3 \times 4
$$

y transforma puntos 3D homogéneos del mundo en puntos 2D homogéneos de la imagen.

Este modelo coincide con el que ya se explica en la sección [8. Modelo completo de cámara](https://github.com/IvanCS-Chenfu/OpenCV/wiki/Formaci%C3%B3n-de-Im%C3%A1genes#8-modelo-completo-de-cámara).

---

<img width="1248" height="567" alt="image" src="https://github.com/user-attachments/assets/54ab5116-1c12-4796-9d1f-f41b64731d0f" />

---

# 2. Distorsión de lente

El modelo pinhole ideal supone que los rayos se proyectan perfectamente según la geometría perspectiva. Sin embargo, una cámara real tiene lentes, y las lentes deforman la imagen.

Por eso, además de estimar $K$, $R$ y $t$, en calibración real también se estiman parámetros de distorsión.

Nos centraremos especialmente en la **distorsión radial**, que es una de las más importantes en visión por computador.

---

## 2.1 Por qué aparece la distorsión

Toda óptica introduce cierto grado de distorsión. La distorsión suele ser más visible cuando:

- la distancia focal es pequeña,
- el campo de visión es grande,
- se usan lentes gran angular,
- los puntos están lejos del centro de la imagen.

Cuanto más abierto es el campo de visión, más se separa el comportamiento real de la lente del modelo pinhole ideal.

---

## 2.2 Distorsión radial

La distorsión radial desplaza los puntos de la imagen según su distancia al centro.

Si un punto ideal del plano sensor es:

$$
(x,y)
$$

y su distancia radial al centro es:

$$
r = \sqrt{x^2 + y^2}
$$

entonces el modelo de distorsión radial utilizado es:

$$
x_d = (1 + k_1 r^2 + k_2 r^4)x
$$

$$
y_d = (1 + k_1 r^2 + k_2 r^4)y
$$

donde:

- $(x,y)$ son las coordenadas ideales sin distorsión.
- $(x_d,y_d)$ son las coordenadas distorsionadas.
- $k_1$ y $k_2$ son los coeficientes de distorsión radial.
- $r$ mide la distancia del punto al centro de la imagen.

Esta misma idea se introduce en la sección [9. Distorsión radial](https://github.com/IvanCS-Chenfu/OpenCV/wiki/Formaci%C3%B3n-de-Im%C3%A1genes#9-distorsión-radial).

La distorsión radial se puede interpretar como un desplazamiento en la dirección radial:

$$
\delta_r = k_1r^2 + k_2r^4
$$

de forma que:

$$
x_d = x + x\delta_r
$$

$$
y_d = y + y\delta_r
$$

Es decir, el punto se desplaza en la dirección del vector $(x,y)$.

---

## 2.3 Distorsión en coordenadas de píxel

En la imagen digital no observamos directamente $(x,y)$, sino coordenadas de píxel.

Si el punto ideal en píxeles es:

$$
(u,v)
$$

y el punto distorsionado observado es:

$$
(u_d,v_d)
$$

entonces se expresa la distorsión radial en píxeles como:

$$
u_d = u + (u-u_0)\delta_r
$$

$$
v_d = v + (v-v_0)\delta_r
$$

con:

$$
\delta_r = k_1r^2 + k_2r^4
$$

Aquí:

- $(u_0,v_0)$ es el punto principal.
- $(u,v)$ es el píxel ideal sin distorsión.
- $(u_d,v_d)$ es el píxel realmente observado.
- $\delta_r$ controla cuánto se desplaza el punto.

Esta formulación es importante porque, en la práctica, lo único que observamos en una imagen real son los píxeles distorsionados $(u_d,v_d)$.

---

<img width="360" height="623" alt="image" src="https://github.com/user-attachments/assets/f7d789bc-af33-4a74-9703-7e6b69b48ad9" />

---

## 2.4 Distorsión de barril y de cojín

El signo de $k_1$ determina el tipo principal de distorsión.

### Distorsión de barril

Si:

$$
k_1 < 0
$$

aparece distorsión de barril.

En este caso, las líneas que no pasan por el centro tienden a curvarse hacia fuera.

Visualmente parece que la imagen se hincha desde el centro, como un barril.

### Distorsión de cojín

Si:

$$
k_1 > 0
$$

aparece distorsión de cojín.

En este caso, las líneas se curvan hacia dentro.

Visualmente parece que la imagen se comprime hacia el centro.

---

<img width="469" height="223" alt="image" src="https://github.com/user-attachments/assets/e5346803-11e9-4447-b238-0b3e8161926b" />

---

## 2.5 La distorsión no es una homografía

Una idea clave es que casi todas las transformaciones del modelo de cámara pueden expresarse mediante matrices homogéneas o transformaciones proyectivas, excepto la distorsión de lente.

La cadena ideal:

$$
M_W \longrightarrow M_C \longrightarrow m \longrightarrow m'
$$

puede describirse mediante transformaciones lineales en coordenadas homogéneas más una proyección perspectiva.

Sin embargo, la distorsión radial introduce términos como:

$$
r^2 = x^2 + y^2
$$

y:

$$
r^4 = (x^2+y^2)^2
$$

Por tanto, la transformación:

$$
(x,y) \longrightarrow (x_d,y_d)
$$

no es lineal ni proyectiva.

Por eso se dice que la distorsión radial **no es una homografía**.

Esta idea conecta directamente con la explicación de homografías en [6. Homografía 2D en visión por computador](https://github.com/IvanCS-Chenfu/OpenCV/wiki/Formaci%C3%B3n-de-Im%C3%A1genes#6-homografía-2d-en-visión-por-computador).

---

# 3. Cámara calibrada y cámara no calibrada

Hay que distinguir entre cámara calibrada y cámara no calibrada.

---

## 3.1 Cámara calibrada

Una cámara está calibrada si se conoce su matriz intrínseca $K$.

Si conocemos $K$, podemos pasar de píxeles a coordenadas normalizadas del sensor:

$$
\tilde{m} = K^{-1}\tilde{m}'
$$

Esto es muy importante porque permite trabajar con puntos expresados en el sistema geométrico de la cámara, eliminando el efecto de la conversión a píxeles.

En una cámara calibrada, un punto de imagen define un rayo 3D que sale del centro óptico de la cámara.

Si el punto normalizado es:

$$
m =
\begin{bmatrix}
x \\
y
\end{bmatrix}
$$

entonces el punto 3D correspondiente está sobre la recta:

$$
M =
Z
\begin{bmatrix}
x \\
y \\
1
\end{bmatrix}
$$

donde $Z$ es la profundidad desconocida.

Es decir, un píxel no determina un punto 3D único, sino un rayo de posibles puntos 3D.

Esto conecta con la sección [5.5 Proyección 2D → 3D: el rayo de proyección](https://github.com/IvanCS-Chenfu/OpenCV/wiki/Formaci%C3%B3n-de-Im%C3%A1genes#55-proyección-2d--3d-el-rayo-de-proyección).

---

## 3.2 Cámara no calibrada

Si $K$ no se conoce, entonces no podemos convertir directamente píxeles en coordenadas normalizadas del sensor.

En ese caso, todavía podemos relacionar puntos 3D y puntos 2D mediante la matriz de proyección completa:

$$
\lambda \tilde{m}' = P \tilde{M}
$$

pero no podemos separar fácilmente qué parte de esa transformación se debe a la geometría externa de la cámara y qué parte se debe a sus propiedades internas.

Por eso la calibración es tan importante: permite separar el modelo en componentes interpretables:

$$
P = K[R|t]
$$

---

# 4. Procedimiento general de calibración

El procedimiento general de calibración se basa en obtener correspondencias entre puntos 3D conocidos y sus proyecciones 2D en la imagen.

Es decir, se necesitan pares:

$$
(M_i, m_i')
$$

donde:

- $M_i$ es un punto 3D conocido.
- $m_i'$ es su proyección observada en la imagen.

El objetivo es encontrar los parámetros del modelo de cámara que mejor explican esas correspondencias.

---

<img width="1268" height="367" alt="image" src="https://github.com/user-attachments/assets/b31e297e-43db-4e31-8168-7f991c19f155" />

---

## 4.1 Paso 1: proporcionar puntos 3D conocidos

Primero se necesita un conjunto de puntos 3D conocidos:

$$
\{M_i\}
$$

En la práctica se suele usar un patrón de calibración, por ejemplo:

- un tablero de ajedrez,
- un patrón de círculos,
- una plantilla plana,
- un patrón 3D rígido.

El caso más habitual es un tablero de ajedrez porque sus esquinas son fáciles de detectar y sus coordenadas son conocidas si sabemos el tamaño real de cada cuadrado.

Por ejemplo, si el tablero es plano y cada cuadrado tiene lado $s$, podemos definir sus puntos como:

$$
M_{ij} =
\begin{bmatrix}
is \\
js \\
0
\end{bmatrix}
$$

Es decir, todos los puntos están sobre el plano:

$$
Z = 0
$$

En métodos generales como DLT 3D, los puntos no deben estar todos en un único plano. Sin embargo, el método de Zhang está diseñado precisamente para trabajar con patrones planos observados desde varias posiciones.

---

<img width="422" height="339" alt="image" src="https://github.com/user-attachments/assets/603e633d-b949-40a3-a1ad-8595c5404a6f" />

<img width="636" height="240" alt="image" src="https://github.com/user-attachments/assets/130f7a09-5270-4d1e-a165-e6c5b1a293b3" />

---

## 4.2 Paso 2: detectar las proyecciones en la imagen

Después se capturan imágenes del patrón y se detectan sus puntos característicos.

En el caso de un tablero de ajedrez, se detectan las esquinas internas de los cuadrados.

Para cada punto 3D conocido:

$$
M_i
$$

se obtiene su proyección en la imagen:

$$
m_i' =
\begin{bmatrix}
u_i \\
v_i
\end{bmatrix}
$$

Así se construye una lista de correspondencias:

$$
(M_i, m_i')
$$

En calibración es importante que los puntos detectados:

- sean precisos,
- cubran toda la imagen,
- aparezcan cerca del centro y también cerca de los bordes,
- se observen con distintas orientaciones del patrón.

La distribución uniforme de los puntos sobre la imagen es especialmente importante para estimar bien la distorsión de lente.

Si todos los puntos aparecen cerca del centro, la calibración no observará suficientemente el efecto de la distorsión radial, que suele ser más visible en los bordes.

---

<img width="362" height="384" alt="image" src="https://github.com/user-attachments/assets/0befb038-2df5-4d3c-b25b-38690bdd97c3" />

---

## 4.3 Paso 3: aplicar el modelo de cámara

Una vez obtenidas las correspondencias, se aplica el modelo de cámara:

$$
\lambda \tilde{m}_i' = P \tilde{M}_i
$$

con:

$$
P = KP_0D
$$

donde:

$$
P_0 =
\begin{bmatrix}
1 & 0 & 0 & 0 \\
0 & 1 & 0 & 0 \\
0 & 0 & 1 & 0
\end{bmatrix} =
[I|0]
$$

y:

$$
D =
\begin{bmatrix}
R & t \\
0_3^T & 1
\end{bmatrix}
$$

Como:

$$
P_0D = [R|t]
$$

entonces:

$$
P = K[R|t]
$$

Por tanto, la notación:

$$
P = KP_0D
$$

es equivalente a la notación usada en la página de formación de imágenes:

$$
P = K[R|t]
$$

---

## 4.4 Paso 4: aplicar el modelo de distorsión

El modelo anterior supone una cámara ideal sin distorsión.

En una cámara real, el punto proyectado ideal $(u,v)$ no coincide exactamente con el punto observado $(u_d,v_d)$.

Por eso se añade el modelo de distorsión radial:

$$
u_d = u + (u-u_0)\delta_r
$$

$$
v_d = v + (v-v_0)\delta_r
$$

con:

$$
\delta_r = k_1r^2 + k_2r^4
$$

El proceso de calibración debe encontrar los parámetros:

$$
K, R, t, k_1, k_2
$$

que mejor expliquen la diferencia entre las proyecciones esperadas y las observadas.

---

# 5. Error de reproyección

El criterio fundamental para evaluar una calibración es el **error de reproyección**.

Supongamos que tenemos un punto 3D real:

$$
M_i
$$

y que en la imagen hemos detectado su píxel real:

$$
m_i'
$$

Si usamos los parámetros estimados de la cámara, podemos proyectar $M_i$ y obtener una predicción:

$$
\hat{m}_i'
$$

El error de reproyección mide la distancia entre el punto observado y el punto predicho:

$$
e_i = \|m_i' - \hat{m}_i'\|
$$

El error cuadrático total para una imagen es:

$$
E = \sum_i \|m_i' - \hat{m}_i'\|^2
$$

Si hay varias imágenes del patrón, se suma sobre todas las imágenes y todos los puntos:

$$
E =
\sum_j
\sum_i
\|m_{ij}' - \hat{m}_{ij}'\|^2
$$

donde:

- $i$ recorre los puntos del patrón.
- $j$ recorre las imágenes.
- $m_{ij}'$ es el punto observado.
- $\hat{m}_{ij}'$ es el punto proyectado por el modelo estimado.

La calibración busca minimizar este error:

$$
\arg \min_{K,R_j,t_j,k_1,k_2}
\sum_j
\sum_i
\|m_{ij}' - \hat{m}_{ij}'\|^2
$$

Este ajuste final suele ser no lineal, porque la proyección perspectiva incluye divisiones por profundidad y la distorsión radial incluye términos cuadráticos y cuárticos.

La relación con las ecuaciones no lineales de la formación de imágenes se puede ver en [8.5 Ecuaciones no lineales resultantes](https://github.com/IvanCS-Chenfu/OpenCV/wiki/Formaci%C3%B3n-de-Im%C3%A1genes#85-ecuaciones-no-lineales-resultantes).

---

# 6. Método DLT para calibración

DLT significa **Direct Linear Transformation**.

Es un método lineal que permite estimar directamente la matriz de proyección:

$$
P
$$

a partir de correspondencias entre puntos 3D y puntos 2D.

El método DLT se usa para calcular:

$$
P
$$

asumiendo que la distorsión de lente es despreciable.

Después, a partir de $P$, se recuperan:

$$
K, R, t
$$

---

## 6.1 Modelo usado por DLT

DLT parte de la ecuación:

$$
\lambda \tilde{m}' = P\tilde{M}_W
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

La matriz $P$ es:

$$
P =
\begin{bmatrix}
p_{11} & p_{12} & p_{13} & p_{14} \\
p_{21} & p_{22} & p_{23} & p_{24} \\
p_{31} & p_{32} & p_{33} & p_{34}
\end{bmatrix}
$$

Entonces:

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

Equivale a:

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

Al dividir por la tercera ecuación aparecen las ecuaciones cartesianas:

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

Aunque estas ecuaciones son no lineales en coordenadas cartesianas, DLT evita trabajar directamente con las divisiones usando coordenadas homogéneas y reordenando los términos.

---

## 6.2 Ecuaciones lineales del DLT

Para cada correspondencia:

$$
M_i \leftrightarrow m_i'
$$

tenemos:

$$
u_i =
\frac{p_1^T \tilde{M}_i}{p_3^T \tilde{M}_i}
$$

$$
v_i =
\frac{p_2^T \tilde{M}_i}{p_3^T \tilde{M}_i}
$$

donde:

$$
p_1^T
$$

es la primera fila de $P$,

$$
p_2^T
$$

es la segunda fila de $P$,

y:

$$
p_3^T
$$

es la tercera fila de $P$.

Reordenando:

$$
p_1^T\tilde{M}_i - u_i p_3^T\tilde{M}_i = 0
$$

$$
p_2^T\tilde{M}_i - v_i p_3^T\tilde{M}_i = 0
$$

Cada punto genera dos ecuaciones lineales sobre los elementos de $P$.

Como $P$ tiene 12 elementos pero está definida salvo escala, tiene 11 grados de libertad.

Por tanto, se necesitan al menos 6 puntos 3D-2D para estimar $P$:

$$
6 \text{ puntos} \times 2 \text{ ecuaciones por punto} = 12 \text{ ecuaciones}
$$

En la práctica se usan más de 6 puntos y se resuelve un sistema sobredeterminado.

---

## 6.3 Sistema homogéneo

El DLT construye un sistema lineal de la forma:

$$
Ap = 0
$$

donde:

- $A$ contiene las ecuaciones generadas por las correspondencias.
- $p$ es el vector con los 12 elementos de $P$.

Como la solución trivial $p=0$ no sirve, se impone una restricción de escala, normalmente resolviendo mediante SVD.

La solución se toma como el vector singular asociado al menor valor singular de $A$.

---

## 6.4 Descomposición de P en K, R y t

Una vez estimada la matriz $P$, el siguiente paso es descomponerla en los parámetros de cámara.

Sabemos que:

$$
P = K[R|t]
$$

Se escribe esta descomposición como:

$$
P = [KR \quad Kt]
$$

Si definimos:

$$
B = KR
$$

y:

$$
b = Kt
$$

entonces:

$$
P = [B \quad b]
$$

La parte izquierda de $P$ es una matriz $3 \times 3$:

$$
B = KR
$$

y la cuarta columna es:

$$
b = Kt
$$

El objetivo es recuperar $K$, $R$ y $t$ a partir de $B$ y $b$.

---

## 6.5 Factorización de B

A partir de:

$$
B = KR
$$

se tiene:

$$
B^{-1} = (KR)^{-1}
$$

Por propiedades de la inversa:

$$
B^{-1} = R^{-1}K^{-1}
$$

Como $R$ es una matriz de rotación:

$$
R^{-1} = R^T
$$

Dependiendo de la convención usada, se puede realizar una factorización tipo RQ, QR o QU para separar una matriz triangular superior y una matriz ortogonal.

Se propone hacer una factorización QU de:

$$
B^{-1}
$$

de manera que:

$$
B^{-1} = QU
$$

donde:

- $Q$ es una matriz ortogonal, asociada a la rotación.
- $U$ es triangular superior, asociada a $K^{-1}$.

Como la inversa de una matriz triangular superior también es triangular superior, a partir de $U$ se puede recuperar $K$.

Una vez obtenido $K^{-1}$, la traslación se obtiene de:

$$
b = Kt
$$

multiplicando por $K^{-1}$:

$$
t = K^{-1}b
$$

---

## 6.6 Ambigüedad de signo

La factorización no es completamente única.

Pueden aparecer distintas combinaciones de signos que producen la misma matriz $P$.

Para resolver esta ambigüedad, se fuerza a que los elementos diagonales de la matriz triangular asociada a $K^{-1}$ sean positivos.

Esto tiene sentido porque los parámetros focales de la cámara deben ser positivos:

$$
s_x > 0
$$

$$
s_y > 0
$$

---

## 6.7 Limitaciones del método DLT

El método DLT es útil porque:

- es lineal,
- es sencillo,
- estima directamente la matriz $P$,
- puede servir como inicialización para métodos más complejos.

Sin embargo, tiene limitaciones importantes.

### No modela distorsión de lente

DLT asume que la distorsión es despreciable.

Por tanto, si la cámara tiene una distorsión radial significativa, la matriz $P$ estimada no explicará bien las observaciones.

### Requiere puntos 3D no degenerados

Para la calibración 3D general, los puntos usados no deben estar todos en un único plano.

Si todos los puntos son coplanares, la estimación de una matriz de cámara 3D general se vuelve degenerada.

### Sensibilidad al ruido

Como método lineal, DLT puede ser sensible al ruido en las correspondencias.

Por eso es habitual normalizar los puntos antes de resolver el sistema y después refinar la solución minimizando el error de reproyección.

### No impone perfectamente las restricciones de cámara

Una matriz $P$ estimada linealmente puede no descomponerse en una rotación perfectamente ortogonal y una matriz intrínseca físicamente válida.

Por eso, después de una solución lineal, suele hacerse una optimización no lineal.

---

# 7. Método de Zhang

El método de Zhang es uno de los métodos más usados en calibración práctica de cámaras.

Su principal ventaja es que no necesita un objeto 3D complejo. Basta con usar un patrón plano, normalmente un tablero de ajedrez, observado desde varias orientaciones.

Esto lo hace muy práctico:

- se puede imprimir un patrón,
- se fija sobre una superficie rígida plana,
- se toman varias imágenes desde distintas poses,
- se detectan las esquinas del patrón,
- se estima la cámara.

---

## 7.1 Idea principal del método

El método de Zhang se basa en que, si todos los puntos del patrón están sobre un plano, existe una homografía entre el plano del patrón y su imagen.

Si el patrón está en el plano:

$$
Z = 0
$$

entonces un punto del patrón puede escribirse como:

$$
\tilde{M} =
\begin{bmatrix}
X \\
Y \\
1
\end{bmatrix}
$$

La proyección de ese punto en la imagen se puede escribir como:

$$
\lambda \tilde{m}' =
K
\begin{bmatrix}
r_1 & r_2 & t
\end{bmatrix}
\begin{bmatrix}
X \\
Y \\
1
\end{bmatrix}
$$

donde:

- $r_1$ es la primera columna de $R$.
- $r_2$ es la segunda columna de $R$.
- $t$ es la traslación.

La matriz:

$$
H = K
\begin{bmatrix}
r_1 & r_2 & t
\end{bmatrix}
$$

es una homografía entre el plano del patrón y la imagen.

Por tanto:

$$
\lambda \tilde{m}' = H \tilde{M}
$$

Esta es la conexión fundamental entre calibración y homografías.

La idea se relaciona con la sección [6.1 Homografía como transformación entre planos](https://github.com/IvanCS-Chenfu/OpenCV/wiki/Formaci%C3%B3n-de-Im%C3%A1genes#61-homografía-como-transformación-entre-planos).

---

## 7.2 Por qué se necesitan varias imágenes

Una única imagen de un patrón plano proporciona una homografía.

Pero una sola homografía no contiene suficiente información para estimar de forma robusta todos los parámetros intrínsecos.

Por eso el método de Zhang utiliza varias imágenes del mismo patrón plano, cada una tomada desde una orientación distinta.

Cada imagen genera una homografía diferente:

$$
H_1, H_2, \dots, H_N
$$

Todas esas homografías comparten la misma matriz intrínseca $K$, porque la cámara es la misma.

Lo que cambia de una imagen a otra son los parámetros extrínsecos:

$$
R_j, t_j
$$

Por tanto, el método usa varias homografías para recuperar una única matriz $K$ común y una pose distinta para cada imagen.

---

# 8. Procedimiento del método de Zhang

Se divide el método de Zhang en tres grandes pasos.

---

## 8.1 Adquisición de datos

Primero se prepara el patrón de calibración.

El procedimiento típico es:

1. Imprimir una plantilla de calibración, normalmente un tablero de ajedrez.
2. Fijarla sobre una superficie plana y rígida.
3. Tomar varias imágenes del patrón desde distintas posiciones y orientaciones.
4. Detectar automáticamente las esquinas del tablero en cada imagen.
5. Asociar cada esquina detectada con su coordenada conocida en el patrón.

Es importante que las imágenes tengan variedad de poses.

No basta con mover el tablero paralelamente al plano de la imagen. Conviene inclinarlo, rotarlo y colocarlo en distintas zonas de la imagen para capturar mejor la geometría y la distorsión.

---

## 8.2 Paso 1: solución cerrada para K, R y t

El primer paso del método de Zhang es obtener una solución inicial en forma cerrada.

Este paso ignora inicialmente la distorsión radial.

Para cada imagen del patrón:

1. Se estima la homografía $H_i$ entre el plano del patrón y la imagen.
2. Se usan todas las homografías para estimar la matriz intrínseca $K$.
3. Se calcula $R_i$ y $t_i$ para cada imagen.

Es una solución cerrada para los parámetros lineales:

$$
K, [R,t]
$$

Si hay $N$ imágenes, el número de incógnitas de este paso es:

$$
4 + 6N
$$

donde:

- 4 corresponden a los parámetros intrínsecos del modelo simplificado:

$$
s_x, s_y, u_0, v_0
$$

- $6N$ corresponden a los parámetros extrínsecos de cada imagen:

$$
R_j, t_j
$$

Cada pose tiene 6 grados de libertad: 3 de rotación y 3 de traslación.

---

## 8.3 Restricciones geométricas usadas por Zhang

La homografía de cada vista puede escribirse como:

$$
H =
\begin{bmatrix}
h_1 & h_2 & h_3
\end{bmatrix} =
K
\begin{bmatrix}
r_1 & r_2 & t
\end{bmatrix}
$$

Por tanto:

$$
h_1 = \lambda K r_1
$$

$$
h_2 = \lambda K r_2
$$

$$
h_3 = \lambda K t
$$

De aquí:

$$
r_1 = \lambda K^{-1}h_1
$$

$$
r_2 = \lambda K^{-1}h_2
$$

$$
t = \lambda K^{-1}h_3
$$

La clave es que $r_1$ y $r_2$ son columnas de una matriz de rotación.

Por tanto, deben cumplir:

$$
r_1^T r_2 = 0
$$

y:

$$
r_1^T r_1 = r_2^T r_2
$$

Es decir:

- $r_1$ y $r_2$ son ortogonales.
- $r_1$ y $r_2$ tienen la misma norma.

Estas restricciones permiten construir ecuaciones sobre $K$ a partir de cada homografía.

En la formulación clásica se define:

$$
B = K^{-T}K^{-1}
$$

y se resuelve un sistema lineal para obtener los elementos de $B$.

Después, a partir de $B$, se recupera $K$.

---

## 8.4 Cálculo de R y t a partir de H

Una vez estimada $K$, se pueden recuperar los parámetros extrínsecos de cada imagen.

Dada una homografía:

$$
H =
\begin{bmatrix}
h_1 & h_2 & h_3
\end{bmatrix}
$$

se calcula un factor de escala:

$$
\lambda = \frac{1}{\|K^{-1}h_1\|}
$$

Entonces:

$$
r_1 = \lambda K^{-1}h_1
$$

$$
r_2 = \lambda K^{-1}h_2
$$

$$
r_3 = r_1 \times r_2
$$

$$
t = \lambda K^{-1}h_3
$$

Con esto se obtiene una estimación inicial de la pose del patrón respecto a la cámara para esa imagen.

Sin embargo, esta estimación no es perfecta.

---

## 8.5 Por qué la solución cerrada no es exacta

Hay dos razones por las que la solución inicial de Zhang no es precisa.

### La matriz R puede no ser perfectamente ortogonal

Aunque teóricamente $R$ debe ser una matriz de rotación, los datos reales tienen ruido.

Por tanto, la matriz calculada puede no cumplir exactamente:

$$
R^TR = I
$$

ni:

$$
\det(R)=1
$$

### Los puntos observados están distorsionados

El método inicial usa homografías, pero una homografía solo modela transformaciones proyectivas entre planos.

Si los puntos de imagen están afectados por distorsión radial, entonces no existe una homografía exacta entre el patrón plano ideal y los puntos observados.

Por eso la solución cerrada solo se usa como inicialización.

Después se estima la distorsión y se refinan todos los parámetros.

---

# 9. Estimación de la distorsión en Zhang

El segundo paso del método de Zhang consiste en estimar los coeficientes de distorsión radial:

$$
k_1, k_2
$$

A partir de la solución inicial de $K$, $R$ y $t$, podemos proyectar los puntos del patrón sin distorsión y obtener sus posiciones ideales:

$$
(u,v)
$$

También conocemos los puntos realmente observados en la imagen:

$$
(u_d,v_d)
$$

La diferencia entre ambos se explica mediante el modelo radial:

$$
u_d = u + (u-u_0)(k_1r^2 + k_2r^4)
$$

$$
v_d = v + (v-v_0)(k_1r^2 + k_2r^4)
$$

Restando:

$$
u_d - u = (u-u_0)(k_1r^2 + k_2r^4)
$$

$$
v_d - v = (v-v_0)(k_1r^2 + k_2r^4)
$$

Esto se puede escribir en forma matricial:

$$
\begin{bmatrix}
u_d-u \\
v_d-v
\end{bmatrix} =
\begin{bmatrix}
(u-u_0)r^2 & (u-u_0)r^4 \\
(v-v_0)r^2 & (v-v_0)r^4
\end{bmatrix}
\begin{bmatrix}
k_1 \\
k_2
\end{bmatrix}
$$

Para todos los puntos y todas las imágenes se construye un sistema lineal:

$$
d = Dk
$$

donde:

$$
k =
\begin{bmatrix}
k_1 \\
k_2
\end{bmatrix}
$$

La solución de mínimos cuadrados es:

$$
k = (D^TD)^{-1}D^Td
$$

Esta estimación proporciona una primera aproximación a la distorsión radial.

---

# 10. Refinamiento no lineal

El tercer paso del método de Zhang consiste en refinar todos los parámetros resolviendo un problema de optimización no lineal.

La solución inicial viene de:

1. La estimación cerrada de $K$, $R$ y $t$.
2. La estimación lineal de $k_1$ y $k_2$.

A partir de esa inicialización se minimiza el error de reproyección:

$$
\arg \min_{K,R_j,t_j,k_1,k_2}
\sum_j
\sum_i
\|m_{ij}' - \hat{m}_{ij}'(M_{ij},K,R_j,t_j,k_1,k_2)\|^2
$$

donde:

- $m_{ij}'$ es el punto observado en la imagen.
- $\hat{m}_{ij}'$ es el punto proyectado por el modelo estimado.
- $j$ recorre las imágenes.
- $i$ recorre los puntos del patrón.

Este refinamiento ajusta simultáneamente:

- la matriz intrínseca $K$,
- los extrínsecos de cada imagen $R_j,t_j$,
- los coeficientes de distorsión $k_1,k_2$.

El objetivo es que los puntos proyectados por el modelo queden lo más cerca posible de los puntos detectados en las imágenes.

---

<img width="382" height="296" alt="image" src="https://github.com/user-attachments/assets/d29c8010-91fe-43bb-b7bc-839d2662640f" />

---

# 11. Número mínimo de imágenes en Zhang

Se analizan cuántas imágenes del patrón son necesarias.

Supongamos que tenemos:

- $N$ imágenes,
- $M$ esquinas detectadas por imagen.

Entonces tenemos:

$$
NM
$$

puntos observados.

Como cada punto proporciona dos coordenadas de imagen, hay:

$$
2NM
$$

ecuaciones.

Las incógnitas son:

$$
4 + 6N
$$

donde:

- 4 son los parámetros intrínsecos:

$$
s_x, s_y, u_0, v_0
$$

- $6N$ son los parámetros extrínsecos de las $N$ imágenes.

Para que el sistema tenga suficientes restricciones:

$$
2NM \geq 4 + 6N
$$

Reordenando:

$$
2NM - 6N \geq 4
$$

$$
2N(M-3) \geq 4
$$

$$
N(M-3) \geq 2
$$

Por tanto:

$$
N \geq \frac{2}{M-3}
$$

con:

$$
M > 3
$$

El mínimo teórico es:

$$
N = 2
$$

imágenes con:

$$
M = 4
$$

puntos cada una.

Sin embargo, en la práctica se usan muchas más imágenes y muchos más puntos para obtener una calibración robusta.

Existe un caso particular:

$$
N = 1, \quad M = 6
$$

Pero una sola imagen de un patrón plano no es una solución válida para calibración completa, porque todos los puntos son coplanares y no aportan suficiente información tridimensional.

---

# 12. Comparación entre DLT y Zhang

| Aspecto | DLT | Zhang |
|---|---|---|
| Tipo de datos | Puntos 3D-2D | Puntos de un patrón plano en varias imágenes |
| Patrón necesario | Idealmente 3D, no coplanar | Plano, por ejemplo tablero de ajedrez |
| Distorsión | No se considera inicialmente | Se estima explícitamente |
| Modelo principal | Matriz de proyección $P$ | Homografías entre plano e imagen |
| Solución inicial | Lineal | Cerrada usando homografías |
| Refinamiento | Recomendable | Parte esencial del método |
| Uso práctico | Calibración simple o inicialización | Calibración real de cámaras |
| Limitación principal | Mala precisión si hay distorsión | Necesita varias imágenes bien distribuidas |

---

# 13. Interpretación conceptual

La calibración puede entenderse como una forma de responder a las siguientes preguntas.

---

## 13.1 Cómo es la cámara por dentro

Esto lo describe la matriz intrínseca:

$$
K =
\begin{bmatrix}
s_x & 0 & u_0 \\
0 & s_y & v_0 \\
0 & 0 & 1
\end{bmatrix}
$$

Aquí se codifica:

- la distancia focal en píxeles,
- el centro principal,
- la conversión del plano sensor a la matriz imagen.

---

## 13.2 Dónde estaba la cámara en cada imagen

Esto lo describen los parámetros extrínsecos:

$$
R_j, t_j
$$

Cada imagen del patrón tiene su propia pose.

Por eso, en calibración con varias imágenes, hay una única matriz $K$, pero varios pares $(R_j,t_j)$.

---

## 13.3 Cómo de deformada está la imagen

Esto lo describen los parámetros de distorsión:

$$
k_1, k_2
$$

Estos parámetros indican cómo se alejan los píxeles observados de la proyección ideal del modelo pinhole.

---

## 13.4 Qué tan buena es la calibración

Esto se evalúa con el error de reproyección:

$$
\sum_j \sum_i
\|m_{ij}' - \hat{m}_{ij}'\|^2
$$

Una buena calibración debe producir un error de reproyección pequeño y una distribución de errores razonablemente uniforme en toda la imagen.

---

# 14. Relación con la formación de imágenes

La página de formación de imágenes construye el modelo directo:

$$
M_W \longrightarrow m'
$$

La calibración estudia cómo obtener los parámetros de ese modelo a partir de observaciones.

La relación entre ambos temas puede resumirse así:

| Formación de imágenes | Calibración de cámara |
|---|---|
| Parte de $K,R,t$ conocidos | Intenta estimar $K,R,t$ |
| Proyecta puntos 3D a píxeles | Usa puntos 3D y píxeles para recuperar la cámara |
| Modelo directo | Problema inverso |
| Explica cómo se genera la imagen | Explica cómo se encuentra el modelo de la cámara |
| Puede incluir distorsión | Estima los parámetros de distorsión |

En formación de imágenes se escribe:

$$
\lambda \tilde{m}' = K[R|t]\tilde{M}_W
$$

En calibración se busca resolver:

$$
\{(M_i,m_i')\}
\quad \longrightarrow \quad
K,R,t,k_1,k_2
$$

---

# 15. Resumen final

La calibración de cámara permite obtener los parámetros necesarios para usar una cámara en tareas de visión 3D.

El modelo ideal de cámara se basa en:

$$
\lambda \tilde{m}' = K[R|t]\tilde{M}_W
$$

donde:

- $K$ contiene los parámetros intrínsecos.
- $R,t$ contienen los parámetros extrínsecos.
- $P = K[R|t]$ es la matriz de proyección.

En una cámara real también hay que considerar la distorsión radial:

$$
x_d = (1+k_1r^2+k_2r^4)x
$$

$$
y_d = (1+k_1r^2+k_2r^4)y
$$

o, en píxeles:

$$
u_d = u + (u-u_0)\delta_r
$$

$$
v_d = v + (v-v_0)\delta_r
$$

con:

$$
\delta_r = k_1r^2+k_2r^4
$$

El procedimiento general de calibración consiste en:

1. Obtener puntos 3D conocidos del patrón.
2. Detectar sus proyecciones 2D en la imagen.
3. Estimar los parámetros del modelo de cámara.
4. Estimar la distorsión.
5. Refinar todos los parámetros minimizando el error de reproyección.

El método **DLT** estima directamente la matriz de proyección $P$ mediante un sistema lineal, pero no modela la distorsión de lente y necesita puntos 3D no degenerados.

El método **Zhang** utiliza varias imágenes de un patrón plano, estima homografías entre el patrón y cada imagen, obtiene una solución inicial para $K,R,t$, estima la distorsión radial y finalmente refina todos los parámetros mediante optimización no lineal.

Por eso, en la práctica, Zhang es uno de los métodos más utilizados para calibrar cámaras reales.