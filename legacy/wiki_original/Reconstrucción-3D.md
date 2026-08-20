# Índice

- [1. Planteamiento general de la reconstrucción 3D](#1-Planteamiento-general-de-la-reconstrucción-3D)

- [2. Triangulación en configuración estéreo ideal](#2-Triangulación-en-configuración-estéreo-ideal)
  - [2.1. Relación entre los sistemas de referencia de las cámaras](#21-Relación-entre-los-sistemas-de-referencia-de-las-cámaras)
  - [2.2. Proyección en ambas cámaras](#22-Proyección-en-ambas-camaras)
  - [2.3. Interpretación de la disparidad](#23-Interpretación-de-la-disparidad)
  - [2.4. Reconstrucción completa del punto 3D](#24-Reconstrucción-completa-del-punto-3D)

- [3. Disparidad en píxeles y relación con la matriz intrínseca](#3-Disparidad-en-píxeles-y-relación-con-la-matriz-intrínseca)

- [4. Precisión de la triangulación](#4-Precisión-de-la-triangulacion)
  - [4.1. Efecto de la baseline](#41-Efecto-de-la-baseline)

- [5. Triangulación en configuración general](#5-Triangulación-en-configuración-general)

- [6. Rectificación estéreo](#6-Rectificación-estereo)

- [7. El problema de las correspondencias](#7-El-problema-de-lascorrespondencias)

- [8. Restricciones para resolver correspondencias](#8-Restricciones-para-resolver-correspondencias)
  - [8.1. Restricción epipolar](#81-Restricción-epipolar)
  - [8.2. Restricción de disparidad mínima y máxima](#82-Restricción-de-disparidad-mínima-y-máxima)
  - [8.3. Continuidad de superficies](#83-Continuidad-de-superficies)
  - [8.4. Unicidad](#84-Unicidad)
  - [8.5. Ordenación](#85-Ordenación)

- [9. Geometría epipolar](#9-Geometría-epipolar)
  - [9.1. Plano epipolar](#91-Plano-epipolar)
  - [9.2. Interpretación geométrica de la línea epipolar](#92-Interpretación-geométrica-de-la-línea-epipolar)
  - [9.3. Epipolos](#93-Epipolos)
  - [9.4. Epipolos en el infinito](#94-Epipolos-en-el-infinito)

- [10. Matriz esencial](#10-Matriz-esencial)
  - [10.1. Propiedades de la matriz esencial](#101-Propiedades-de-la-matriz-esencial)

- [11. Matriz fundamental](#11-Matriz-fundamental)
  - [11.1. Interpretación de la matriz fundamental](#111-Interpretación-de-la-matriz-fundamental)
  - [11.2. Propiedades de la matriz fundamental](#112-Propiedades-de-la-matriz-fundamental)
  - [11.3. Epipolos y matriz fundamental](#113-Epipolos-y-matriz-fundamental)
  - [11.4. Matriz fundamental en la configuración ideal](#114-Matriz-fundamental-en-la-configuración-ideal)

- [12. Reconstrucción desde dos vistas](#12-Reconstrucción-desde-dos-vistas)

- [13. Correlación cruzada normalizada, NCC](#13-Correlación-cruzada-normalizada-NCC)
  - [13.1. Ventanas de correlación y disparidad](#131-Ventanas-de-correlación-y-disparidad)
  - [13.2. Efecto del tamaño de ventana](#132-Efecto-del-tamaño-de-ventana)
  - [13.3. Limitaciones de la correlación](#133-Limitaciones-de-la-correlación)

- [14. Enfoque global para correspondencias](#14-Enfoque-global-para-correspondencias)

- [15. Reconstrucción en zonas sin textura](#15-Reconstrucción-en-zonas-sin-textura)

- [16. Resumen final](#16-Resumen-final)


# 1. Planteamiento general de la reconstrucción 3D

La formación de imágenes estudia cómo un punto tridimensional de la escena acaba proyectándose sobre un píxel de la imagen. En el modelo de cámara pinhole, ese proceso se expresa de forma compacta como:

$$
\lambda \tilde{m}' = K[R|t]\tilde{M}
$$

donde $\tilde{M}$ es un punto 3D en coordenadas homogéneas, $\tilde{m}'$ es su proyección en píxeles, $K$ contiene los parámetros intrínsecos de la cámara y $[R|t]$ describe la pose de la cámara respecto al sistema del mundo.

Este modelo se explicó en la página de [Formación de Imágenes y Modelo de Cámara](https://github.com/IvanCS-Chenfu/OpenCV/wiki/Formaci%C3%B3n-de-Im%C3%A1genes). En particular, conviene tener presentes las secciones sobre la [matriz de proyección de la cámara](https://github.com/IvanCS-Chenfu/OpenCV/wiki/Formaci%C3%B3n-de-Im%C3%A1genes#84-matriz-de-proyecci%C3%B3n-de-la-c%C3%A1mara), las [ecuaciones no lineales resultantes](https://github.com/IvanCS-Chenfu/OpenCV/wiki/Formaci%C3%B3n-de-Im%C3%A1genes#85-ecuaciones-no-lineales-resultantes) y la interpretación inversa de la proyección como un [rayo 3D asociado a un punto 2D](https://github.com/IvanCS-Chenfu/OpenCV/wiki/Formaci%C3%B3n-de-Im%C3%A1genes#55-proyecci%C3%B3n-2d--3d-el-rayo-de-proyecci%C3%B3n).

La reconstrucción 3D desde varias vistas estudia el problema inverso:

$$
\text{varias imágenes 2D} \longrightarrow \text{estructura 3D de la escena}
$$

La idea fundamental es que una sola imagen no permite recuperar directamente la profundidad de un punto, porque un mismo píxel corresponde a infinitos puntos 3D situados sobre el mismo rayo de proyección. Sin embargo, si observamos el mismo punto físico desde dos o más cámaras, podemos intersectar los rayos de visión y recuperar su posición 3D.

Para reconstruir una escena no es estrictamente necesario tener dos cámaras físicas. Lo importante es tener dos o más vistas distintas de la escena.

Hay tres configuraciones habituales:

1. **Sistema estéreo**  
   Se utilizan dos cámaras al mismo tiempo. Normalmente se conocen sus parámetros intrínsecos y la pose relativa entre ellas. Es el caso más clásico de reconstrucción 3D por estéreo.

2. **Structure from Motion, SfM**  
   Se tienen imágenes tomadas desde posiciones diferentes, normalmente desconocidas y no necesariamente ordenadas. El objetivo es estimar simultáneamente la estructura 3D de la escena y la pose relativa de las cámaras. Suele resolverse mediante optimización global, por ejemplo con *Bundle Adjustment*.

3. **MonoVisual SLAM**  
   Es parecido a SfM, pero las imágenes llegan secuencialmente, normalmente desde una única cámara en movimiento. La reconstrucción y la localización se hacen en tiempo real. Las vistas suelen tener pequeña separación temporal y, por tanto, pequeña baseline.

En todos los casos, aparecen dos problemas principales:

1. **Correspondencia o emparejamiento de puntos**  
   Dado un punto, píxel, segmento o región en una imagen, hay que encontrar qué punto de otra imagen corresponde al mismo punto físico de la escena.

2. **Triangulación geométrica**  
   Una vez conocidas las correspondencias y las poses de las cámaras, se calcula la posición 3D del punto observado.

La correspondencia y la triangulación están profundamente relacionadas. Si la correspondencia es incorrecta, la triangulación genera un punto 3D que realmente no existe en la escena.

---

<img width="662" height="245" alt="image" src="https://github.com/user-attachments/assets/e9a5a9c8-9e16-4567-be96-959eef7aaed0" />

---

# 2. Triangulación en configuración estéreo ideal

La configuración estéreo más sencilla es la configuración ideal o rectificada. En ella se asume que:

- Las dos cámaras son idénticas:

$$
K_l = K_r
$$

- Los ejes ópticos son paralelos.
- Las cámaras están separadas horizontalmente una distancia $b$, llamada **baseline**.
- La cámara derecha está desplazada respecto a la izquierda a lo largo del eje $X$.
- Las proyecciones de un mismo punto aparecen en la misma fila de ambas imágenes:

$$
y_l = y_r
$$

Esta última propiedad es muy importante, porque reduce la búsqueda de correspondencias de un problema 2D a un problema 1D: para buscar el punto correspondiente en la imagen derecha, no hace falta explorar toda la imagen, sino únicamente la misma fila.

---

<img width="849" height="521" alt="image" src="https://github.com/user-attachments/assets/355fea41-0d90-4e29-9c52-d1193d7a5a31" />

---

## 2.1. Relación entre los sistemas de referencia de las cámaras

Sea $X_l$ un punto 3D expresado en el sistema de coordenadas de la cámara izquierda:

$$
X_l =
\begin{bmatrix}
X_l \\
Y_l \\
Z_l
\end{bmatrix}
$$

y sea $X_r$ el mismo punto expresado en el sistema de la cámara derecha:

$$
X_r =
\begin{bmatrix}
X_r \\
Y_r \\
Z_r
\end{bmatrix}
$$

En general, la relación entre ambos sistemas se escribe como:

$$
X_r = R_l^r X_l + t_l^r
$$

donde:

- $R_l^r$ es la rotación que expresa la orientación de la cámara izquierda respecto a la derecha.
- $t_l^r$ es la traslación de la cámara izquierda expresada en el sistema de la derecha.

En la configuración ideal:

$$
R_l^r = I
$$

y:

$$
t_l^r =
\begin{bmatrix}
-b \\
0 \\
0
\end{bmatrix}
$$

Por tanto:

$$
X_r =
\begin{bmatrix}
X_l - b \\
Y_l \\
Z_l
\end{bmatrix}
$$

Es decir:

$$
X_r = X_l - b
$$

$$
Y_r = Y_l
$$

$$
Z_r = Z_l
$$

Como ambas cámaras tienen ejes paralelos y la misma orientación, la profundidad del punto respecto a ambas cámaras es la misma:

$$
Z_l = Z_r = Z
$$


## 2.2. Proyección en ambas cámaras

Trabajando con coordenadas métricas en el plano sensor, es decir, con una cámara calibrada, la proyección pinhole de un punto en la cámara izquierda es:

$$
x_l = f\frac{X_l}{Z}
$$

$$
y_l = f\frac{Y_l}{Z}
$$

En la cámara derecha:

$$
x_r = f\frac{X_r}{Z}
$$

Como:

$$
X_r = X_l - b
$$

entonces:

$$
x_r = f\frac{X_l - b}{Z}
$$

La diferencia horizontal entre las dos proyecciones se llama **disparidad**:

$$
d = x_l - x_r
$$

Sustituyendo:

$$
d = f\frac{X_l}{Z} - f\frac{X_l - b}{Z}
$$

$$
d = f\frac{b}{Z}
$$

Por tanto, la profundidad se obtiene como:

$$
Z = \frac{bf}{d}
$$

Esta es una de las ecuaciones fundamentales de la visión estéreo.

## 2.3. Interpretación de la disparidad

La disparidad mide cuánto se desplaza horizontalmente la proyección de un punto entre la imagen izquierda y la derecha.

La relación:

$$
Z = \frac{bf}{d}
$$

indica que:

- Si $d$ es grande, el punto está cerca.
- Si $d$ es pequeña, el punto está lejos.
- Si $d = 0$, el punto estaría en el infinito.
- La profundidad depende directamente de la baseline $b$ y de la distancia focal $f$.
- La profundidad depende inversamente de la disparidad.

Por tanto, los objetos cercanos producen mayor diferencia entre las dos imágenes, mientras que los objetos lejanos apenas cambian de posición.

---

<img width="1216" height="536" alt="image" src="https://github.com/user-attachments/assets/3da020e8-42c7-4f46-8ca0-a0d7b2d88e09" />

---

## 2.4. Reconstrucción completa del punto 3D

No solo se puede recuperar la profundidad $Z$, sino también las coordenadas completas del punto 3D respecto a la cámara izquierda.

A partir de la proyección pinhole:

$$
x_l = f\frac{X_l}{Z}
$$

se obtiene:

$$
X_l = \frac{Z}{f}x_l
$$

y como:

$$
Z = \frac{bf}{d}
$$

entonces:

$$
X_l = \frac{b}{d}x_l
$$

De forma análoga:

$$
Y_l = \frac{b}{d}y_l
$$

y:

$$
Z_l = \frac{bf}{d}
$$

Por tanto, el punto 3D reconstruido en el sistema de la cámara izquierda es:

$$
X_l =
\begin{bmatrix}
\dfrac{b}{d}x_l \\
\dfrac{b}{d}y_l \\
\dfrac{bf}{d}
\end{bmatrix}
$$

o de forma compacta:

$$
X_l = \frac{b}{d}
\begin{bmatrix}
x_l \\
y_l \\
f
\end{bmatrix}
$$

Esta expresión muestra una idea muy importante: reconstruir un punto 3D consiste en tomar el rayo definido por el píxel observado y encontrar el valor de escala correcto usando la disparidad.

---

# 3. Disparidad en píxeles y relación con la matriz intrínseca

Hasta ahora se ha supuesto que las coordenadas de imagen están expresadas en unidades métricas sobre el sensor. Sin embargo, en una imagen digital se trabaja con píxeles.

La relación entre coordenadas métricas del sensor $(x,y)$ y coordenadas de píxel $(u,v)$ puede escribirse como:

$$
u = k_x x + u_0
$$

$$
v = k_y y + v_0
$$

donde:

- $k_x$ y $k_y$ son factores de escala de metros a píxeles.
- $(u_0,v_0)$ es el centro principal.
- En el caso más habitual se considera skew nulo.

Esto está directamente relacionado con la matriz intrínseca explicada en la sección de [parámetros intrínsecos](https://github.com/IvanCS-Chenfu/OpenCV/wiki/Formaci%C3%B3n-de-Im%C3%A1genes#83-par%C3%A1metros-intr%C3%ADnsecos).

Si las dos cámaras tienen el mismo centro principal y el mismo factor de escala horizontal, la disparidad en unidades métricas se relaciona con la disparidad en píxeles mediante:

$$
d = x_l - x_r = \frac{1}{k_x}(u_l - u_r)
$$

Definiendo la disparidad en píxeles como:

$$
d_i = u_l - u_r
$$

se tiene:

$$
d = \frac{d_i}{k_x}
$$

Por tanto:

$$
Z = \frac{bf}{d}
= \frac{bf}{d_i/k_x}
= \frac{b(k_x f)}{d_i}
$$

Como $k_x f$ es la distancia focal expresada en píxeles, se suele escribir:

$$
Z = \frac{b f_x}{d_i}
$$

donde $f_x$ es la focal en píxeles.

Esta forma es la más habitual en implementaciones de visión por computador:

$$
\boxed{Z = \frac{b f_x}{d}}
$$

donde ahora $d$ suele entenderse como disparidad en píxeles.

---

# 4. Precisión de la triangulación

La ecuación:

$$
Z = \frac{bf}{d}
$$

permite analizar cómo afecta un error en la disparidad al error en profundidad.

Derivando respecto a $d$:

$$
\frac{\Delta Z}{\Delta d} =
-\frac{bf}{d^2}
$$

Como:

$$
d = \frac{bf}{Z}
$$

también se puede escribir:

$$
\Delta Z \approx -\frac{Z^2}{bf}\Delta d
$$

Esta expresión tiene una consecuencia muy importante:

$$
|\Delta Z| \propto Z^2
$$

Es decir, para un mismo error de disparidad, el error en profundidad crece cuadráticamente con la distancia.

Por eso la reconstrucción estéreo es mucho más precisa en objetos cercanos que en objetos lejanos.

Por ejemplo, si se tiene:

$$
\Delta d = 10^{-4} \text{ m}
$$

$$
f = 5 \text{ mm}
$$

$$
b = 0.1 \text{ m}
$$

entonces:

$$
\frac{1}{fb} = 2 \cdot 10^3
$$

Para un punto a:

$$
Z = 1 \text{ m}
$$

el error aproximado sería:

$$
\Delta Z = 2 \cdot 10^3 \cdot 10^{-4} = 0.2 \text{ m}
$$

pero para:

$$
Z = 10 \text{ m}
$$

el error pasa a:

$$
\Delta Z = 2 \cdot 10^3 \cdot 10^{-4} \cdot 10^2 = 20 \text{ m}
$$

Esto muestra que la visión estéreo pierde precisión rápidamente con la distancia.

<a id="41-efecto-baseline"></a>
### 4.1. Efecto de la baseline

Una forma de mejorar la precisión es aumentar la baseline $b$.

Como:

$$
\Delta Z \approx -\frac{Z^2}{bf}\Delta d
$$

si $b$ aumenta, el error en profundidad disminuye.

Sin embargo, aumentar la baseline también tiene un coste:

- Las dos imágenes se parecen menos.
- Hay menos solapamiento entre los campos de visión.
- Aparecen más oclusiones.
- Es más difícil encontrar correspondencias fiables.

Por tanto, existe un compromiso:

- **Baseline pequeña**: correspondencias más fáciles, pero poca precisión en profundidad.
- **Baseline grande**: mayor precisión geométrica, pero correspondencias más difíciles.

---

<img width="590" height="319" alt="image" src="https://github.com/user-attachments/assets/22ea8ccd-f875-4103-8685-4384a7115571" />

---

# 5. Triangulación en configuración general

En una configuración real, las cámaras no tienen por qué ser idénticas ni estar perfectamente alineadas. En ese caso, no se puede usar directamente la fórmula simple:

$$
Z = \frac{bf}{d}
$$

Hay que trabajar con las matrices de proyección de cada cámara.

Tomando como sistema de referencia el de la cámara izquierda, se puede escribir:

$$
\lambda_l \tilde{x}'_l = P_l \tilde{X}_l
$$

$$
\lambda_r \tilde{x}'_r = P_r \tilde{X}_l
$$

donde:

$$
P_l = K_l[I|0]
$$

y:

$$
P_r = K_r[R_l^r|t_l^r]
$$

Aquí:

- $\tilde{x}'_l$ y $\tilde{x}'_r$ son los puntos observados en píxeles.
- $\tilde{X}_l$ es el punto 3D en coordenadas homogéneas.
- $\lambda_l$ y $\lambda_r$ son factores de escala.
- $P_l$ y $P_r$ son las matrices de proyección de las cámaras.

El problema es que las ecuaciones tienen factores de escala desconocidos. Para eliminarlos se usa el producto vectorial:

$$
\tilde{x}' \times P\tilde{X} = 0
$$

Cada observación proporciona dos ecuaciones linealmente independientes. Con dos cámaras se obtienen cuatro ecuaciones para estimar el punto 3D.

En el caso ideal, los dos rayos de visión se cortan exactamente en un punto. Pero en la práctica hay ruido:

- error en la detección de puntos,
- error de calibración,
- error en la pose relativa,
- distorsión no corregida,
- correspondencias imperfectas.

Por eso los rayos no suelen intersectar exactamente. En ese caso, se busca el punto 3D que mejor satisface las ecuaciones, normalmente mediante mínimos cuadrados.

Una forma habitual de formular el refinamiento es minimizar el error de reproyección:

$$
\min_X
\sum_i
\left\|
x_i - \pi(P_i X)
\right\|^2
$$

donde $\pi(\cdot)$ representa la división homogénea para pasar de coordenadas proyectivas a coordenadas de imagen.

---

# 6. Rectificación estéreo

Cuando las cámaras no están alineadas, las correspondencias no aparecen necesariamente en la misma fila. La búsqueda de correspondencias sería más costosa porque habría que buscar sobre líneas inclinadas o incluso con distintas orientaciones.

Para simplificar el problema se utiliza la **rectificación estéreo**.

La rectificación transforma ambas imágenes mediante homografías 2D para proyectarlas sobre un plano virtual común. El objetivo es conseguir que las líneas epipolares sean:

- horizontales,
- paralelas,
- y estén a la misma altura en ambas imágenes.

Después de rectificar, el punto correspondiente de un píxel de la imagen izquierda debe buscarse en la misma fila de la imagen derecha.

La rectificación no cambia los centros ópticos de las cámaras. Lo que cambia es la forma en que se reexpresan las imágenes sobre planos virtuales.

---

<img width="670" height="381" alt="image" src="https://github.com/user-attachments/assets/82e9f2f6-7891-4f1c-970b-18536ca364e3" />

---

# 7. El problema de las correspondencias

La triangulación solo funciona si sabemos qué puntos de ambas imágenes corresponden al mismo punto físico de la escena.

Este problema se conoce como **problema de correspondencia** o **data association problem**.

Dado un punto en la imagen izquierda, queremos encontrar su correspondencia en la imagen derecha:

$$
x_l \longleftrightarrow x_r
$$

Si la correspondencia es correcta, los dos rayos de visión corresponden al mismo punto 3D. Si la correspondencia es incorrecta, la triangulación produce un punto 3D inventado.

Se puede intentar emparejar distintos tipos de entidades:

- píxeles,
- keypoints,
- bordes,
- segmentos,
- regiones,
- patches de imagen.

En visión estéreo densa, normalmente se intenta estimar una disparidad para muchos píxeles. En reconstrucción dispersa, se suelen emparejar puntos característicos, como esquinas o keypoints.

El emparejamiento requiere algún descriptor o medida de similitud. Una medida clásica es la correlación cruzada normalizada, conocida como **NCC**.

Sin embargo, seleccionar la correspondencia correcta no es trivial. Incluso si buscamos solo sobre una línea epipolar, pueden aparecer varios candidatos con valores de similitud altos.

---

<img width="1263" height="443" alt="image" src="https://github.com/user-attachments/assets/acab146e-5c55-4940-a025-679bea884524" />

---

# 8. Restricciones para resolver correspondencias

Para que el emparejamiento sea robusto, no basta con comparar apariencia local. También hay que usar restricciones geométricas y restricciones propias del entorno.

Las restricciones más importantes son:

1. Restricción epipolar.
2. Rango mínimo y máximo de disparidad.
3. Continuidad de superficies.
4. Unicidad.
5. Ordenación.

---

## 8.1. Restricción epipolar

La restricción epipolar dice que, dado un punto en una imagen, su correspondencia en la otra imagen no puede estar en cualquier lugar, sino que debe estar sobre una línea concreta: la **línea epipolar**.

Es decir, para un punto $x_l$ en la imagen izquierda, su correspondencia $x_r$ en la imagen derecha debe cumplir:

$$
x_r \in l_r
$$

donde $l_r$ es la línea epipolar correspondiente a $x_l$.

Esto reduce enormemente la búsqueda:

$$
\text{búsqueda 2D en toda la imagen}
\quad \longrightarrow \quad
\text{búsqueda 1D sobre una línea}
$$

En imágenes rectificadas, esa línea es una fila horizontal.

---

<img width="1096" height="303" alt="image" src="https://github.com/user-attachments/assets/ef125277-85a4-4149-ad0c-7c7627007356" />

---

## 8.2. Restricción de disparidad mínima y máxima

En un sistema estéreo, la disparidad esperada no es arbitraria. Depende de:

- la baseline $b$,
- la focal $f$,
- la resolución de la cámara,
- la distancia mínima y máxima de la escena observada.

Como:

$$
d = \frac{bf}{Z}
$$

si conocemos un rango aproximado de profundidades:

$$
Z_{min} \leq Z \leq Z_{max}
$$

podemos obtener un rango de disparidades:

$$
d_{min} = \frac{bf}{Z_{max}}
$$

$$
d_{max} = \frac{bf}{Z_{min}}
$$

Esto permite limitar la búsqueda. Por ejemplo, si sabemos que la escena está dentro de una habitación y que ningún punto está más lejos de cierto valor, no tiene sentido buscar disparidades menores que un determinado umbral.

## 8.3. Continuidad de superficies

La mayoría de superficies reales son continuas. Eso significa que puntos vecinos de la imagen suelen tener profundidades parecidas.

Como la profundidad y la disparidad están relacionadas por:

$$
Z = \frac{bf}{d}
$$

también se espera que píxeles vecinos tengan disparidades parecidas.

Esta restricción solo falla en bordes de oclusión o en discontinuidades reales de profundidad, por ejemplo en el borde entre un objeto cercano y el fondo.

La continuidad puede aplicarse a lo largo de filas y también de columnas. Cuando se aplica a estructuras de la imagen, suele hablarse de **continuidad figural**.

---

<img width="978" height="323" alt="image" src="https://github.com/user-attachments/assets/274964cb-1e72-4ceb-b1bc-09787c487e5f" />

---

## 8.4. Unicidad

La restricción de unicidad dice que un punto de una imagen debería corresponder, como máximo, a un punto de la otra imagen.

En otras palabras, un píxel no debería emparejarse simultáneamente con varios píxeles distintos de la otra imagen.

Esto se basa en la idea de que un píxel observa un único punto visible de la escena.

La restricción puede fallar o volverse ambigua en casos como:

- oclusiones,
- superficies transparentes,
- reflejos,
- zonas repetitivas,
- regiones sin textura.

Pero como regla general es una restricción muy útil para descartar emparejamientos incompatibles.

---

## 8.5. Ordenación

La restricción de ordenación dice que los puntos situados a lo largo de líneas epipolares conjugadas tienden a conservar el mismo orden.

Si en la imagen izquierda tenemos puntos:

$$
1,2,3,4
$$

sus correspondencias en la imagen derecha suelen aparecer en el mismo orden:

$$
1',2',3',4'
$$

Esta propiedad ayuda a evitar emparejamientos cruzados.

Sin embargo, no siempre se cumple. Puede fallar en escenas con:

- oclusiones fuertes,
- objetos delgados,
- estructuras repetidas,
- geometrías complejas,
- cambios bruscos de profundidad.

Aun así, es una restricción muy útil en algoritmos globales de correspondencia.

---

<img width="368" height="185" alt="image" src="https://github.com/user-attachments/assets/122be492-0c6a-4ae3-90f7-64716983d394" />

---

# 9. Geometría epipolar

La geometría epipolar describe las restricciones geométricas que existen entre dos vistas de una escena. Depende únicamente de la pose relativa entre las cámaras y de sus parámetros internos.

Los elementos principales son:

- centros ópticos,
- plano epipolar,
- líneas epipolares,
- epipolos,
- matriz esencial,
- matriz fundamental.

## 9.1. Plano epipolar

Sean:

- $C_l$: centro óptico de la cámara izquierda,
- $C_r$: centro óptico de la cámara derecha,
- $X$: punto 3D de la escena.

Los tres puntos $C_l$, $C_r$ y $X$ definen un plano. Ese plano se llama **plano epipolar**.

El plano epipolar corta cada plano imagen en una recta:

- en la imagen izquierda produce una línea epipolar,
- en la imagen derecha produce la línea epipolar conjugada.

Por tanto, cada punto 3D define un plano epipolar y un par de líneas epipolares.

---

<img width="884" height="260" alt="image" src="https://github.com/user-attachments/assets/c5de3efb-67f3-4981-94ad-b52a0533b8c8" />

---

## 9.2. Interpretación geométrica de la línea epipolar

Supongamos que observamos un punto $x_l$ en la imagen izquierda.

Ese punto define un rayo 3D que sale del centro óptico $C_l$ y pasa por $x_l$. Como se explicó en la interpretación inversa del modelo pinhole, un punto 2D no determina un único punto 3D, sino una recta de posibles puntos en el espacio.

Todos los puntos 3D posibles sobre ese rayo, al proyectarse en la cámara derecha, caen sobre una misma línea: la línea epipolar derecha.

Por eso, si $x_r$ es la correspondencia correcta de $x_l$, necesariamente debe estar sobre esa línea.


## 9.3. Epipolos

El **epipolo** de una imagen es la proyección del centro óptico de la otra cámara sobre esa imagen.

- El epipolo izquierdo es la proyección de $C_r$ sobre la imagen izquierda.
- El epipolo derecho es la proyección de $C_l$ sobre la imagen derecha.

Una propiedad fundamental es que todas las líneas epipolares de una imagen se cortan en su epipolo.

Esto ocurre porque todos los planos epipolares comparten la recta que une los dos centros ópticos:

$$
C_l C_r
$$

Al proyectar esa recta sobre una imagen se obtiene el epipolo.

Conocer la posición del epipolo aporta información sobre la pose relativa de las cámaras.

---

<img width="529" height="231" alt="image" src="https://github.com/user-attachments/assets/37e216dc-350e-457e-a429-5b6041f3066e" />

---

## 9.4. Epipolos en el infinito

En algunas configuraciones, el epipolo puede estar en el infinito.

Esto ocurre cuando el plano imagen es paralelo a la línea que une los centros ópticos.

En el caso estéreo ideal, los dos planos imagen son paralelos entre sí y también paralelos a la baseline. Como consecuencia:

- los epipolos están en el infinito,
- las líneas epipolares son paralelas,
- y, si además están a la misma altura, se obtiene la configuración rectificada.

Esta es la razón geométrica por la que, en estéreo rectificado, las correspondencias se buscan en la misma fila.

---

<img width="529" height="231" alt="image" src="https://github.com/user-attachments/assets/d3a40503-8e73-4476-8d1a-ca9f5a2ee075" />

---


# 10. Matriz esencial

La matriz esencial describe la restricción epipolar cuando las cámaras están calibradas, es decir, cuando se conocen sus matrices intrínsecas.

En este caso trabajamos con coordenadas normalizadas o coordenadas métricas del sensor, no directamente con píxeles.

Sea la relación entre un punto expresado en la cámara derecha y en la cámara izquierda:

$$
X_l = R X_r + t
$$

donde:

- $R$ es la rotación relativa,
- $t$ es la traslación relativa,
- todo está expresado en el sistema de referencia de la cámara izquierda.

Los vectores:

$$
X_l
$$

$$
t
$$

$$
RX_r
$$

son coplanares, porque pertenecen al mismo plano epipolar.

Tres vectores coplanares tienen producto mixto nulo:

$$
X_l^T \left(t \times RX_r\right) = 0
$$

El producto vectorial puede escribirse como multiplicación por una matriz antisimétrica:

$$
[t]_\times =
\begin{bmatrix}
0 & -t_z & t_y \\
t_z & 0 & -t_x \\
-t_y & t_x & 0
\end{bmatrix}
$$

Entonces:

$$
t \times RX_r = [t]_\times RX_r
$$

y la restricción queda:

$$
X_l^T [t]_\times R X_r = 0
$$

Como los puntos 3D están sobre los rayos definidos por sus coordenadas de imagen:

$$
X_l = \lambda_l \tilde{x}_l
$$

$$
X_r = \lambda_r \tilde{x}_r
$$

se obtiene:

$$
\tilde{x}_l^T [t]_\times R \tilde{x}_r = 0
$$

Definiendo:

$$
E = [t]_\times R
$$

tenemos la restricción epipolar calibrada:

$$
\boxed{\tilde{x}_l^T E \tilde{x}_r = 0}
$$

La matriz $E$ se llama **matriz esencial**.

---

## 10.1. Propiedades de la matriz esencial

La matriz esencial:

$$
E = [t]_\times R
$$

contiene la geometría relativa entre dos cámaras calibradas.

Sus propiedades principales son:

- Tiene tamaño $3 \times 3$.
- Tiene rango 2.
- Depende de la rotación relativa $R$.
- Depende de la dirección de la traslación $t$.
- Está definida salvo escala.
- Solo puede usarse directamente con coordenadas calibradas.

Que esté definida salvo escala significa que:

$$
E
$$

y:

$$
\alpha E
$$

representan la misma restricción epipolar para cualquier $\alpha \neq 0$.

Esto implica que, con dos vistas calibradas, se puede recuperar la rotación relativa y la dirección de la traslación, pero no la escala absoluta de la traslación salvo que se conozca alguna distancia real, como la baseline de un sistema estéreo.

---

# 11. Matriz fundamental

Cuando las cámaras no están calibradas, o cuando se trabaja directamente con coordenadas de píxel, se utiliza la **matriz fundamental**.

Las coordenadas calibradas y las coordenadas de píxel están relacionadas por la matriz intrínseca:

$$
\tilde{x}' = K\tilde{x}
$$

por tanto:

$$
\tilde{x} = K^{-1}\tilde{x}'
$$

Partiendo de la restricción con la matriz esencial:

$$
\tilde{x}_l^T E \tilde{x}_r = 0
$$

y sustituyendo:

$$
\tilde{x}_l = K_l^{-1}\tilde{x}'_l
$$

$$
\tilde{x}_r = K_r^{-1}\tilde{x}'_r
$$

se obtiene:

$$
\tilde{x}'_l{}^T K_l^{-T} E K_r^{-1}\tilde{x}'_r = 0
$$

Definiendo:

$$
F = K_l^{-T} E K_r^{-1}
$$

tenemos:

$$
\boxed{\tilde{x}'_l{}^T F \tilde{x}'_r = 0}
$$

La matriz $F$ se llama **matriz fundamental**.

Si ambas cámaras tienen la misma matriz intrínseca $K$, entonces:

$$
F = K^{-T} E K^{-1}
$$

---

## 11.1. Interpretación de la matriz fundamental

La matriz fundamental relaciona puntos y líneas entre dos imágenes.

Con la convención:

$$
\tilde{x}'_l{}^T F \tilde{x}'_r = 0
$$

se puede interpretar así:

- Dado un punto en la imagen derecha, su línea epipolar en la imagen izquierda es:

$$
l_l = F\tilde{x}'_r
$$

- Dado un punto en la imagen izquierda, su línea epipolar en la imagen derecha es:

$$
l_r = F^T\tilde{x}'_l
$$

La ecuación:

$$
\tilde{x}'_l{}^T F \tilde{x}'_r = 0
$$

significa que el punto de una imagen debe estar sobre la línea epipolar inducida por el punto de la otra imagen.

---

## 11.2. Propiedades de la matriz fundamental

La matriz fundamental tiene estas propiedades:

- Es una matriz $3 \times 3$.
- Tiene rango 2.
- Es singular:

$$
\det(F) = 0
$$

- Está definida salvo escala.
- Tiene 7 grados de libertad.
- Puede estimarse a partir de correspondencias entre puntos.
- No requiere conocer explícitamente la matriz intrínseca $K$.

Una forma clásica de estimarla es el algoritmo de los ocho puntos, porque cada correspondencia proporciona una ecuación lineal de la forma:

$$
\tilde{x}'_l{}^T F \tilde{x}'_r = 0
$$

Con al menos ocho correspondencias se puede estimar $F$, aunque en la práctica se usan muchas más y se combina con RANSAC para eliminar correspondencias erróneas.

---

## 11.3. Epipolos y matriz fundamental

Los epipolos también se obtienen a partir de la matriz fundamental.

Si $e_r$ es el epipolo derecho, entonces:

$$
F e_r = 0
$$

Si $e_l$ es el epipolo izquierdo, entonces:

$$
F^T e_l = 0
$$

Esto significa que los epipolos están en los espacios nulos de $F$ y $F^T$.

---

## 11.4. Matriz fundamental en la configuración ideal

En la configuración estéreo ideal:

- las cámaras tienen ejes paralelos,
- la traslación es horizontal,
- los epipolos están en el infinito,
- las líneas epipolares son horizontales.

En ese caso, la línea epipolar de un punto tiene ecuación:

$$
y = y_r
$$

Es decir, la correspondencia debe estar en la misma fila.

Esto conecta directamente la geometría epipolar con la idea práctica de la disparidad:

$$
d = x_l - x_r
$$

En estéreo rectificado, la matriz fundamental codifica precisamente que el emparejamiento se reduce a buscar desplazamientos horizontales.

---

# 12. Reconstrucción desde dos vistas

La reconstrucción desde dos vistas combina todos los conceptos anteriores.

Un flujo típico es:

1. Obtener dos imágenes de la escena.
2. Detectar puntos o regiones relevantes.
3. Buscar correspondencias entre ambas imágenes.
4. Estimar la geometría epipolar mediante $F$ o $E$.
5. Filtrar correspondencias erróneas.
6. Recuperar la pose relativa entre cámaras si se trabaja con $E$.
7. Triangular los puntos.
8. Filtrar puntos con profundidad inválida o error de reproyección alto.
9. Refinar la reconstrucción mediante optimización.

Si las cámaras están calibradas, se suele trabajar con la matriz esencial:

$$
E = [t]_\times R
$$

A partir de $E$ se puede recuperar:

- la rotación relativa $R$,
- la dirección de la traslación $t$.

Como aparecen varias soluciones posibles al descomponer $E$, se selecciona la solución físicamente válida usando la condición de **profundidad positiva**: los puntos triangulados deben quedar delante de ambas cámaras.

Si las cámaras no están calibradas, se trabaja con la matriz fundamental $F$, que permite imponer la restricción epipolar y buscar correspondencias, aunque no proporciona directamente una reconstrucción métrica sin información adicional.

---

# 13. Correlación cruzada normalizada, NCC

En estéreo denso se busca una correspondencia para muchos píxeles. Una técnica clásica consiste en comparar ventanas de imagen mediante **Normalized Cross Correlation**, NCC.

La idea es tomar una ventana alrededor de un píxel en la imagen izquierda y compararla con ventanas candidatas en la imagen derecha, desplazadas según distintos valores de disparidad.

Para un píxel:

$$
(u_0,v_0)
$$

y una disparidad $d$, se compara la ventana de la imagen izquierda centrada en:

$$
(u_0,v_0)
$$

con la ventana de la imagen derecha centrada en:

$$
(u_0 - d, v_0)
$$

en el caso rectificado.

NCC normaliza la comparación para que sea menos sensible a cambios de brillo y contraste.

La idea puede verse de forma vectorial:

1. Una ventana de imagen se convierte en un vector.
2. Se resta la media para eliminar diferencias de brillo.
3. Se divide por la norma o desviación típica para normalizar el contraste.
4. Se calcula el producto escalar entre vectores normalizados.

Así, NCC mide el coseno del ángulo entre dos vectores de apariencia. Si el valor es alto, las ventanas son parecidas.

---

<img width="686" height="307" alt="image" src="https://github.com/user-attachments/assets/f8250bca-aeb9-4572-92cb-3483cbf4d6cb" />

---

## 13.1. Ventanas de correlación y disparidad

En imágenes rectificadas, para cada valor de disparidad se desplaza una ventana a lo largo de la misma fila.

Si la ventana tiene tamaño:

$$
(2N+1) \times (2N+1)
$$

se compara un bloque local de la imagen izquierda con un bloque local de la imagen derecha.

El valor de disparidad que maximiza la similitud se toma como candidato:

$$
d^* = \arg\max_d NCC(d)
$$

Después, la profundidad se calcula como:

$$
Z = \frac{bf}{d^*}
$$

o, en píxeles:

$$
Z = \frac{bf_x}{d^*}
$$

---

## 13.2. Efecto del tamaño de ventana

El tamaño de la ventana afecta mucho a la calidad de la reconstrucción.

Una **ventana pequeña**:

- conserva más detalle,
- permite mapas de profundidad más finos,
- respeta mejor discontinuidades,
- pero es más sensible al ruido.

Una **ventana grande**:

- es menos ruidosa,
- produce medidas de similitud más estables,
- pero suaviza la reconstrucción,
- falla cerca de discontinuidades de profundidad,
- puede mezclar píxeles que pertenecen a objetos con disparidades distintas.

Para que una ventana produzca una buena correspondencia, todos o casi todos sus píxeles deberían tener la misma disparidad. Si la ventana cruza el borde de un objeto, contiene píxeles a diferentes profundidades y la correlación deja de representar bien una única correspondencia.

---

<img width="291" height="305" alt="image" src="https://github.com/user-attachments/assets/e587dae8-cc55-4545-b85f-2d915a2514ed" />

<img width="291" height="305" alt="image" src="https://github.com/user-attachments/assets/8ad94b82-0ad4-4ddf-831d-fd78b314f861" />

---

## 13.3. Limitaciones de la correlación

La correlación local tiene varias limitaciones.

### Cambios de punto de vista

Un mismo punto 3D puede verse con distinta apariencia desde dos cámaras. La textura puede deformarse por perspectiva y la iluminación puede cambiar.

En ese caso, dos ventanas correspondientes pueden no parecerse lo suficiente.

### Superficies sin textura

Si una región tiene intensidad casi constante, muchos desplazamientos producen valores de correlación parecidos. No hay información visual suficiente para decidir la correspondencia.

#### Patrones repetidos

En regiones repetitivas, varios candidatos pueden parecer igualmente buenos.

### Oclusiones

Un punto visible en una imagen puede no ser visible en la otra. En ese caso, no existe correspondencia válida.

### Ambigüedades geométricas

Puede haber situaciones donde dos puntos 3D diferentes producen patches muy parecidos o incluso idénticos. Por ejemplo, una superficie cilíndrica puede generar apariencias locales ambiguas.

Por todo esto, la correlación local no suele ser suficiente por sí sola.

---

# 14. Enfoque global para correspondencias

Una mejora consiste en resolver el problema de correspondencias de forma global, teniendo en cuenta muchas correspondencias al mismo tiempo.

La idea es:

1. Construir un grafo con posibles emparejamientos.
2. Asociar un coste a cada nodo según la similitud local, por ejemplo usando NCC.
3. Asociar costes a los arcos según si se cumplen o no las restricciones geométricas.
4. Buscar el camino de coste mínimo.

En este enfoque, un nodo representa una posible correspondencia entre un punto de la imagen izquierda y un punto de la imagen derecha.

El coste del nodo puede ser menor cuanto mayor sea la similitud entre patches.

Los costes de los arcos penalizan violaciones de restricciones como:

- ordenación,
- unicidad,
- continuidad,
- completitud,
- continuidad figural.

Por ejemplo:

- La restricción de ordenación favorece caminos que avanzan de forma coherente.
- La unicidad evita que un punto se empareje con varios puntos.
- La completitud favorece visitar más correspondencias válidas.
- La continuidad figural favorece soluciones parecidas en líneas epipolares vecinas.

El camino óptimo puede calcularse con algoritmos como Dijkstra o programación dinámica, dependiendo de la formulación.

---

<img width="492" height="464" alt="image" src="https://github.com/user-attachments/assets/72fcdbbe-8c28-4654-af9d-5b939fe3bde7" />

---

# 15. Reconstrucción en zonas sin textura

Las zonas sin textura son especialmente difíciles para estéreo pasivo. Si una pared blanca aparece igual en muchas posiciones, no hay una señal visual clara para decidir qué píxel corresponde a cuál.

Una solución es introducir información adicional en la escena. Por ejemplo, se puede proyectar un patrón de luz o textura artificial sobre el objeto.

Esta idea se usa en técnicas de reconstrucción 3D más invasivas, como sistemas de luz estructurada empleados en digitalización 3D o CAD.

La diferencia principal es:

- En estéreo pasivo, solo se observan imágenes de la escena.
- En métodos activos, el sistema modifica la iluminación o proyecta patrones para facilitar la correspondencia.

Esto permite reconstruir superficies con poca textura natural, aunque requiere controlar el entorno o añadir hardware adicional.

---

<img width="577" height="562" alt="image" src="https://github.com/user-attachments/assets/5e1d5f12-550a-4f92-bf97-4c2781438bc5" />

---

# 16. Resumen final

La reconstrucción 3D desde múltiples vistas se basa en combinar varias proyecciones 2D de una misma escena.

El modelo de formación de imágenes describe el proceso directo:

$$
X \longrightarrow x
$$

La reconstrucción intenta resolver el proceso inverso:

$$
x_l, x_r \longrightarrow X
$$

Con una sola imagen, un píxel define un rayo 3D, pero no un punto único. Con dos vistas, la intersección de rayos permite estimar profundidad.

En la configuración estéreo ideal, la profundidad se calcula mediante:

$$
Z = \frac{bf}{d}
$$

donde:

- $b$ es la baseline,
- $f$ es la distancia focal,
- $d$ es la disparidad.

La precisión de la profundidad depende fuertemente de la distancia:

$$
\Delta Z \approx -\frac{Z^2}{bf}\Delta d
$$

Por tanto, los errores crecen cuadráticamente con la profundidad.

Cuando las cámaras no están alineadas, se trabaja con matrices de proyección:

$$
\lambda_l \tilde{x}'_l = P_l \tilde{X}
$$

$$
\lambda_r \tilde{x}'_r = P_r \tilde{X}
$$

y la triangulación se resuelve eliminando las escalas mediante productos vectoriales o minimizando el error de reproyección.

La geometría epipolar reduce el problema de correspondencia. Dado un punto en una imagen, su correspondencia debe estar sobre una línea epipolar en la otra imagen.

Si las cámaras están calibradas, la restricción epipolar se expresa con la matriz esencial:

$$
\tilde{x}_l^T E \tilde{x}_r = 0
$$

con:

$$
E = [t]_\times R
$$

Si se trabaja en píxeles o con cámaras no calibradas, se usa la matriz fundamental:

$$
\tilde{x}'_l{}^T F \tilde{x}'_r = 0
$$

con:

$$
F = K_l^{-T} E K_r^{-1}
$$

Finalmente, para obtener una reconstrucción densa, se estiman correspondencias para muchos píxeles, normalmente mediante técnicas de correlación, optimización global o métodos más modernos de estéreo. Las restricciones de disparidad, continuidad, unicidad, ordenación y geometría epipolar son esenciales para evitar correspondencias erróneas y obtener una reconstrucción 3D coherente.