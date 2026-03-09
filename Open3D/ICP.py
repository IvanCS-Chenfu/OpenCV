# Iterative Closest Point

import open3d as o3d
import numpy as np

import copy

def mostrar_transformacion(pcd, pcd_cambiada, T):
    pcd_mostrar = copy.deepcopy(pcd)
    pcd_cambiada_mostrar = copy.deepcopy(pcd_cambiada)
    
    pcd_mostrar.transform(T)
    
    pcd_mostrar.paint_uniform_color([0,1,0])  
    pcd_cambiada_mostrar.paint_uniform_color([1,0,0])  
    
    o3d.visualization.draw_geometries([pcd_mostrar, pcd_cambiada_mostrar])

# Para un punto p_i se busca el punto más cercano de q_i (normalmente con KD-Tree)
# Se estima una transformación mediante SVD (Singular VAlue Decomposition). Queremos una R y una t que minimicen:
# sum(abs(R*p_i + t - q_i)^2)
# En cada iteración se aplica la T obtenida y se vuelve a realizar 
def ICP(pcd1, pcd2):
    
    # Transformación Inicial (creemos que por ahí van los tiros)
    I = np.array([[1.0, 0.0, 0.0, 0.0],
                  [0.0, 1.0, 0.0, 0.0],
                  [0.0, 0.0, 1.0, 0.0],
                  [0.0, 0.0, 0.0, 1.0]])
    
    mostrar_transformacion(pcd1, pcd2, I)
    
    
    
    
    umbral = 0.2    # Distancia máxima para considerar correspondencia (solo se consideran puntos si distancia < umbral)
    evaluacion = o3d.pipelines.registration.evaluate_registration(pcd1,pcd2,umbral,I)
    print(evaluacion)   # Fitness = correspondencias / puntos_source
    
    
    icp_p2p = o3d.pipelines.registration.registration_icp(pcd1,pcd2,umbral,I,
                                                          o3d.pipelines.registration.TransformationEstimationPointToPoint(),    # Función de Error: abs(R*p_i + t - q_i)^2
                                                          o3d.pipelines.registration.ICPConvergenceCriteria(max_iteration=2000))    # Criterio de Parada (tras 2000 se para)
    print(icp_p2p)
    print(icp_p2p.transformation)
    
    mostrar_transformacion(pcd1, pcd2, icp_p2p.transformation)
    
    
if __name__ == '__main__':
    
    pcd1 = o3d.io.read_point_cloud("./bunny/reconstruction/bun_zipper.ply")
    pcd2 = copy.deepcopy(pcd1)
    
    T = np.array([[0.862, 0.011, -0.507, 0.005],
                  [-0.139, 0.967, -0.215, 0.007],
                  [0.487, 0.255, 0.835, -0.014],
                  [0.0, 0.0, 0.0, 1.0]])
    
    T = np.array([[0.862, 0.011, -0.507, 0.05],
                  [-0.139, 0.967, -0.215, 0.07],
                  [0.487, 0.255, 0.835, -0.14],
                  [0.0, 0.0, 0.0, 1.0]])
    
    pcd2.transform(T)
    
    ICP(pcd1, pcd2)