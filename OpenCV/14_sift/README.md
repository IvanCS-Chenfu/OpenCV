# SIFT

Código didáctico asociado al apartado correspondiente de la wiki. Las versiones Python y C++ persiguen el mismo objetivo conceptual; no tienen por qué ser traducciones línea por línea.

## Ejecutar Python

```bash
python3 14_sift/python/main.py
```

## Compilar C++

```bash
cmake -S 14_sift/cpp -B build/14_sift
cmake --build build/14_sift
./build/14_sift/opencv_14_sift
```

> Ajusta los nombres/rutas de entrada descritos en el código. Las imágenes y vídeos seleccionados para la wiki se guardarán en `../assets/14_sift/` cuando se prepare la fase visual.
