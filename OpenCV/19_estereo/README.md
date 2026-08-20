# Rectificación, disparidad y profundidad

Código didáctico asociado al apartado correspondiente de la wiki. Las versiones Python y C++ persiguen el mismo objetivo conceptual; no tienen por qué ser traducciones línea por línea.

## Ejecutar Python

```bash
python3 19_estereo/python/main.py
```

## Compilar C++

```bash
cmake -S 19_estereo/cpp -B build/19_estereo
cmake --build build/19_estereo
./build/19_estereo/opencv_19_estereo
```

> Ajusta los nombres/rutas de entrada descritos en el código. Las imágenes y vídeos seleccionados para la wiki se guardarán en `../assets/19_estereo/` cuando se prepare la fase visual.
