# Umbralización y segmentación clásica

Código didáctico asociado al apartado correspondiente de la wiki. Las versiones Python y C++ persiguen el mismo objetivo conceptual; no tienen por qué ser traducciones línea por línea.

## Ejecutar Python

```bash
python3 10_segmentacion/python/main.py
```

## Compilar C++

```bash
cmake -S 10_segmentacion/cpp -B build/10_segmentacion
cmake --build build/10_segmentacion
./build/10_segmentacion/opencv_10_segmentacion
```

> Ajusta los nombres/rutas de entrada descritos en el código. Las imágenes y vídeos seleccionados para la wiki se guardarán en `../assets/10_segmentacion/` cuando se prepare la fase visual.
