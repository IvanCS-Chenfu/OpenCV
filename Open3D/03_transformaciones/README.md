# Transformaciones y sistemas de referencia

Código didáctico asociado al apartado correspondiente de la wiki. Ajusta las rutas de entrada a tus propios datos o a los datasets documentados en `/datasets`.

## Ejecutar Python

```bash
python3 03_transformaciones/python/main.py
```

## Compilar C++

```bash
cmake -S 03_transformaciones/cpp -B build/03_transformaciones
cmake --build build/03_transformaciones
./build/03_transformaciones/open3d_03_transformaciones
```

Los resultados seleccionados se almacenarán en `../assets/03_transformaciones/` en la fase dedicada a imágenes y vídeos.
