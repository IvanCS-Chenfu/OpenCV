# Iterative Closest Point

import open3d as o3d
import numpy as np

import copy

def mostrar_transformacion(pcd, pcd_cambiada, T):
    pcd_mostrar = copy.deepcopy(pcd)
    pcd_cambiada_mostrar = copy.deepcopy(pcd_cambiada)
    
    pcd_mostrar.transform(T)
    
    o3d.visualization.draw_geometries([pcd_mostrar, pcd_cambiada_mostrar])



def normales(pcd, voxel_size):
    
    # Reducir Tamaño (podría no hacerse)
    pcd_down = pcd.voxel_down_sample(voxel_size=voxel_size)
    
    # Calcular Normales (necesario)
    radius_normal = voxel_size * 2
    pcd_down.estimate_normals(search_param=o3d.geometry.KDTreeSearchParamHybrid(radius=radius_normal, max_nn=30))
    
    return pcd_down



def ICP_colored(source, target):
    
    I = np.array([[1.0, 0.0, 0.0, 0.0],
                  [0.0, 1.0, 0.0, 0.0],
                  [0.0, 0.0, 1.0, 0.0],
                  [0.0, 0.0, 0.0, 1.0]])
    
    source = normales(source, 0.1)
    target = normales(target, 0.1)
    
    mostrar_transformacion(source, target, I)
    
    
    umbral = 0.1 
    
    resultado = o3d.pipelines.registration.registration_colored_icp(
        source,target,umbral,I,
        o3d.pipelines.registration.TransformationEstimationForColoredICP(),
        o3d.pipelines.registration.ICPConvergenceCriteria(relative_fitness=1e-6, relative_rmse=1e-6, max_iteration=2000)
    )
    
    print(resultado.transformation)
    mostrar_transformacion(source, target, resultado.transformation)
    
    
if __name__ == '__main__':
    
    source = o3d.io.read_point_cloud("escritorio_color.ply")
    target = copy.deepcopy(source)
    
    T = np.array([[0.862, 0.011, -0.507, -4],
                  [-0.139, 0.967, -0.215, -1],
                  [0.487, 0.255, 0.835, 0.0],
                  [0.0, 0.0, 0.0, 1.0]])
    
    target.transform(T)
    
    ICP_colored(source, target)
    
    # https://www.youtube.com/watch?v=_ajVzSKFDR4&list=PLkmvobsnE0GEZugH1Di2Cr_f32qYkv7aN&index=12
    # Para animar y ver como varía source iteración a iteración.