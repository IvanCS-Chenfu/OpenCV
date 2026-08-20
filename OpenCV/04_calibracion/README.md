# Calibración y corrección de distorsión

Código didáctico asociado al apartado correspondiente de la wiki. Las versiones Python y C++ persiguen el mismo objetivo conceptual; no tienen por qué ser traducciones línea por línea.

## Ejecutar Python

```bash
python3 04_calibracion/python/main.py
```

## Compilar C++

```bash
cmake -S 04_calibracion/cpp -B build/04_calibracion
cmake --build build/04_calibracion
./build/04_calibracion/opencv_04_calibracion
```

> Ajusta los nombres/rutas de entrada descritos en el código. Las imágenes y vídeos seleccionados para la wiki se guardarán en `../assets/04_calibracion/` cuando se prepare la fase visual.
