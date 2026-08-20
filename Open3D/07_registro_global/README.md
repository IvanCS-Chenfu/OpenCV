# Registro global y correspondencias

Código didáctico asociado al apartado correspondiente de la wiki. Ajusta las rutas de entrada a tus propios datos o a los datasets documentados en `/datasets`.

## Ejecutar Python

```bash
python3 07_registro_global/python/main.py
```

## Compilar C++

```bash
cmake -S 07_registro_global/cpp -B build/07_registro_global
cmake --build build/07_registro_global
./build/07_registro_global/open3d_07_registro_global
```

Los resultados seleccionados se almacenarán en `../assets/07_registro_global/` en la fase dedicada a imágenes y vídeos.
