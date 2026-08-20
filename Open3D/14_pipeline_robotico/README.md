# Pipeline 3D con sensor simulado

Objetivo: disponer de una escena reproducible en Gazebo con una cámara RGB-D o sensor de profundidad para producir datos que después se procesan con OpenCV/Open3D.

**Fuera de alcance:** enseñar ROS 2. Los topics, launch files o bridges se consideran infraestructura. La documentación de esta carpeta debe centrarse en: modelo de ruido, intrínsecos, rango, resolución, sincronización RGB-depth, conversión a nube, filtrado y registro.

Cuando se añada el mundo definitivo, guardar aquí solo los archivos mínimos del ejemplo y en `assets/14_pipeline_robotico/` los resultados visuales seleccionados.

## Ejecutar Python

```bash
python3 14_pipeline_robotico/python/main.py
```

## Compilar C++

```bash
cmake -S 14_pipeline_robotico/cpp -B build/14_pipeline_robotico
cmake --build build/14_pipeline_robotico
./build/14_pipeline_robotico/open3d_14_pipeline_robotico
```

Los resultados seleccionados se almacenarán en `../assets/14_pipeline_robotico/` en la fase dedicada a imágenes y vídeos.
