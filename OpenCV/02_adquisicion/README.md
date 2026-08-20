# Adquisición de imagen y vídeo

Código didáctico asociado al apartado correspondiente de la wiki. Las versiones Python y C++ persiguen el mismo objetivo conceptual; no tienen por qué ser traducciones línea por línea.

## Ejecutar Python

```bash
python3 02_adquisicion/python/main.py
```

## Compilar C++

```bash
cmake -S 02_adquisicion/cpp -B build/02_adquisicion
cmake --build build/02_adquisicion
./build/02_adquisicion/opencv_02_adquisicion
```

> Ajusta los nombres/rutas de entrada descritos en el código. Las imágenes y vídeos seleccionados para la wiki se guardarán en `../assets/02_adquisicion/` cuando se prepare la fase visual.
