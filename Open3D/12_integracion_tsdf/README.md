# Integración RGB-D y TSDF

Código didáctico asociado al apartado correspondiente de la wiki. Ajusta las rutas de entrada a tus propios datos o a los datasets documentados en `/datasets`.

## Ejecutar Python

```bash
python3 12_integracion_tsdf/python/main.py
```

## Compilar C++

```bash
cmake -S 12_integracion_tsdf/cpp -B build/12_integracion_tsdf
cmake --build build/12_integracion_tsdf
./build/12_integracion_tsdf/open3d_12_integracion_tsdf
```

Los resultados seleccionados se almacenarán en `../assets/12_integracion_tsdf/` en la fase dedicada a imágenes y vídeos.
