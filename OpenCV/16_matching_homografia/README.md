# Matching, RANSAC y homografía

Código didáctico asociado al apartado correspondiente de la wiki. Las versiones Python y C++ persiguen el mismo objetivo conceptual; no tienen por qué ser traducciones línea por línea.

## Ejecutar Python

```bash
python3 16_matching_homografia/python/main.py
```

## Compilar C++

```bash
cmake -S 16_matching_homografia/cpp -B build/16_matching_homografia
cmake --build build/16_matching_homografia
./build/16_matching_homografia/opencv_16_matching_homografia
```

> Ajusta los nombres/rutas de entrada descritos en el código. Las imágenes y vídeos seleccionados para la wiki se guardarán en `../assets/16_matching_homografia/` cuando se prepare la fase visual.
