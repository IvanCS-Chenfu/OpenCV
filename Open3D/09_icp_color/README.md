# Colored ICP

Código didáctico asociado al apartado correspondiente de la wiki. Ajusta las rutas de entrada a tus propios datos o a los datasets documentados en `/datasets`.

## Ejecutar Python

```bash
python3 09_icp_color/python/main.py
```

## Compilar C++

```bash
cmake -S 09_icp_color/cpp -B build/09_icp_color
cmake --build build/09_icp_color
./build/09_icp_color/open3d_09_icp_color
```

Los resultados seleccionados se almacenarán en `../assets/09_icp_color/` en la fase dedicada a imágenes y vídeos.
