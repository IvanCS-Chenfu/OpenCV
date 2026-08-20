# Modelo pinhole y proyección

Código didáctico asociado al apartado correspondiente de la wiki. Las versiones Python y C++ persiguen el mismo objetivo conceptual; no tienen por qué ser traducciones línea por línea.

## Ejecutar Python

```bash
python3 03_modelo_camara/python/main.py
```

## Compilar C++

```bash
cmake -S 03_modelo_camara/cpp -B build/03_modelo_camara
cmake --build build/03_modelo_camara
./build/03_modelo_camara/opencv_03_modelo_camara
```

> Ajusta los nombres/rutas de entrada descritos en el código. Las imágenes y vídeos seleccionados para la wiki se guardarán en `../assets/03_modelo_camara/` cuando se prepare la fase visual.
