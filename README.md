# Visión por Computador

Repositorio práctico asociado a la wiki **Visión por Computador**. La documentación se divide en cuatro hojas lógicas principales:

- **OpenCV** — visión 2D, formación de imagen, procesamiento, características y geometría multivista.
- **Open3D** — nubes de puntos, registro, integración RGB-D y reconstrucción 3D.
- **SLAM** — fundamentos generales de SLAM. Esta parte está marcada para migrarse en el futuro al repositorio de Robótica.
- **ORB-SLAM3** — arquitectura e implementación interna de ORB-SLAM3, referenciando la hoja de SLAM para la teoría general.

La hoja **Reconocimiento de Patrones** permanece temporalmente en la wiki para su futura migración a un repositorio de IA.

## Entorno de referencia

- Ubuntu 24.04 LTS
- C++17
- CMake
- Python 3
- OpenCV 4.x
- Open3D estable compatible con el entorno
- Gazebo Harmonic y ROS 2 Jazzy únicamente cuando sirven para generar datos de sensores; esta wiki no enseña ROS 2.

## Filosofía de los ejemplos

Cada apartado práctico puede contener uno o varios programas. Para OpenCV y Open3D se intenta mantener una versión **Python** y otra **C++** conceptualmente equivalentes. Los conceptos de programación se explican solo de forma breve y se enlazan a la wiki de Programación. ORB-SLAM3 se documenta exclusivamente en C++.

Los directorios `legacy/` conservan el material anterior al rediseño y **no son la implementación oficial de la nueva wiki**.

## ORB-SLAM3

El código de terceros no se copia en este repositorio. La referencia canónica es `https://github.com/UZ-SLAMLab/ORB_SLAM3` fijada para el análisis interno en el commit `4452a3c4ab75b1cde34e5505a36ec3f9edcdc4c4`. Usa `ORB-SLAM3/utils/obtener_orbslam3.sh` para clonar esa revisión localmente.

## Wiki

La versión lista para publicar está en la carpeta hermana `../wiki` dentro del paquete entregado. El script `../subir_wiki.sh` realiza una copia de seguridad local, muestra el diff y solo publica tras confirmación explícita.
