# Puente hacia odometría visual y SLAM

Código didáctico asociado al apartado correspondiente de la wiki. Las versiones Python y C++ persiguen el mismo objetivo conceptual; no tienen por qué ser traducciones línea por línea.

## Ejecutar Python

```bash
python3 21_puente_odometria_visual/python/main.py
```

## Compilar C++

```bash
cmake -S 21_puente_odometria_visual/cpp -B build/21_puente_odometria_visual
cmake --build build/21_puente_odometria_visual
./build/21_puente_odometria_visual/opencv_21_puente_odometria_visual
```

> Ajusta los nombres/rutas de entrada descritos en el código. Las imágenes y vídeos seleccionados para la wiki se guardarán en `../assets/21_puente_odometria_visual/` cuando se prepare la fase visual.
