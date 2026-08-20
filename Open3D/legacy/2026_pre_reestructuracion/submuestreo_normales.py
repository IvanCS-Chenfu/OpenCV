import open3d as o3d
import numpy as np

# Hace un "grid 3D" y pone un punto en la posición media de todos los puntos de cada cubo (voxel)
def voxel_downsampling_normales(pcd, flag_normales):

    pcd_down = pcd.voxel_down_sample(voxel_size=0.01)
    print("N. Puntos (Normal):", pcd)
    print("N. Puntos (Submuestreo):", pcd_down)
    
    if flag_normales:
        # Hay que pulsar "N" para observar las normales
        pcd_down.estimate_normals(search_param=o3d.geometry.KDTreeSearchParamHybrid(radius=0.1, max_nn=30))
        # Radio y número de Vecinos
        
        print("Normal del Punto 0:", pcd_down.normals[0])
        
    
    pcd.paint_uniform_color([1,0,0])        # Pintar Normal en Rojo
    pcd_down.paint_uniform_color([0,1,0])   # Pintar Submuestreo en Verde
    
    
    o3d.visualization.draw_geometries([pcd, pcd_down])
    
    
# En vez de hacer la posición media de los puntos de un cubo, hace la posición media de "N" puntos 
def uniform_downsampling_normales(pcd, flag_normales):

    pcd_down = pcd.uniform_down_sample(every_k_points=5)
    print("N. Puntos (Normal):", pcd)
    print("N. Puntos (Submuestreo):", pcd_down)
    
    if flag_normales:
        # Hay que pulsar "N" para observar las normales
        pcd_down.estimate_normals(search_param=o3d.geometry.KDTreeSearchParamHybrid(radius=0.1, max_nn=30))
        # Radio y número de Vecinos
        
        print("Normal del Punto 0:", pcd_down.normals[0])
        
    
    pcd.paint_uniform_color([1,0,0])        # Pintar Normal en Rojo
    pcd_down.paint_uniform_color([0,1,0])   # Pintar Submuestreo en Verde
    
    
    o3d.visualization.draw_geometries([pcd, pcd_down])

if __name__ == '__main__':
    
    pcd = o3d.io.read_point_cloud("./bunny/reconstruction/bun_zipper.ply")
    
    voxel_downsampling_normales(pcd, True)
    uniform_downsampling_normales(pcd, True)