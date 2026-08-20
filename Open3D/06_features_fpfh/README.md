# Descriptores geométricos FPFH

Código didáctico asociado al apartado correspondiente de la wiki. Ajusta las rutas de entrada a tus propios datos o a los datasets documentados en `/datasets`.

## Ejecutar Python

```bash
python3 06_features_fpfh/python/main.py
```

## Compilar C++

```bash
cmake -S 06_features_fpfh/cpp -B build/06_features_fpfh
cmake --build build/06_features_fpfh
./build/06_features_fpfh/open3d_06_features_fpfh
```

Los resultados seleccionados se almacenarán en `../assets/06_features_fpfh/` en la fase dedicada a imágenes y vídeos.
