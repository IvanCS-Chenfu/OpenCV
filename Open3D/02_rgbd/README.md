# RGB-D y generación de nubes

Código didáctico asociado al apartado correspondiente de la wiki. Ajusta las rutas de entrada a tus propios datos o a los datasets documentados en `/datasets`.

## Ejecutar Python

```bash
python3 02_rgbd/python/main.py
```

## Compilar C++

```bash
cmake -S 02_rgbd/cpp -B build/02_rgbd
cmake --build build/02_rgbd
./build/02_rgbd/open3d_02_rgbd
```

Los resultados seleccionados se almacenarán en `../assets/02_rgbd/` en la fase dedicada a imágenes y vídeos.
