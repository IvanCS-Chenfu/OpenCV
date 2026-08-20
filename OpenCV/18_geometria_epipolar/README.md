# Geometría epipolar

Código didáctico asociado al apartado correspondiente de la wiki. Las versiones Python y C++ persiguen el mismo objetivo conceptual; no tienen por qué ser traducciones línea por línea.

## Ejecutar Python

```bash
python3 18_geometria_epipolar/python/main.py
```

## Compilar C++

```bash
cmake -S 18_geometria_epipolar/cpp -B build/18_geometria_epipolar
cmake --build build/18_geometria_epipolar
./build/18_geometria_epipolar/opencv_18_geometria_epipolar
```

> Ajusta los nombres/rutas de entrada descritos en el código. Las imágenes y vídeos seleccionados para la wiki se guardarán en `../assets/18_geometria_epipolar/` cuando se prepare la fase visual.
