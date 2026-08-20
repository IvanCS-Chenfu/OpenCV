# Datasets

Los datasets grandes no se versionan en Git. Se descargan bajo `datasets/data/`, que está ignorado por `.gitignore`.

Se recomiendan:

- **EuRoC MAV** — visual-inercial, especialmente útil para ORB-SLAM3.
- **TUM RGB-D** — RGB-D, reconstrucción, odometría y SLAM.
- **TUM-VI** — visual-inercial con cámaras fisheye.
- **KITTI** — estéreo, odometría y conducción.
- **Redwood / Open3D demo data** — registro e integración 3D.
- **Stanford Bunny** — geometría y reconstrucción de superficies.

Los scripts de descarga nunca deben sobrescribir datos sin avisar y deben conservar la licencia/origen del dataset.
