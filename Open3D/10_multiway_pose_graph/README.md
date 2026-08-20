# Registro multiway y pose graph

Código didáctico asociado al apartado correspondiente de la wiki. Ajusta las rutas de entrada a tus propios datos o a los datasets documentados en `/datasets`.

## Ejecutar Python

```bash
python3 10_multiway_pose_graph/python/main.py
```

## Compilar C++

```bash
cmake -S 10_multiway_pose_graph/cpp -B build/10_multiway_pose_graph
cmake --build build/10_multiway_pose_graph
./build/10_multiway_pose_graph/open3d_10_multiway_pose_graph
```

Los resultados seleccionados se almacenarán en `../assets/10_multiway_pose_graph/` en la fase dedicada a imágenes y vídeos.
