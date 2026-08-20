# ICP point-to-point y point-to-plane

Código didáctico asociado al apartado correspondiente de la wiki. Ajusta las rutas de entrada a tus propios datos o a los datasets documentados en `/datasets`.

## Ejecutar Python

```bash
python3 08_icp/python/main.py
```

## Compilar C++

```bash
cmake -S 08_icp/cpp -B build/08_icp
cmake --build build/08_icp
./build/08_icp/open3d_08_icp
```

Los resultados seleccionados se almacenarán en `../assets/08_icp/` en la fase dedicada a imágenes y vídeos.
