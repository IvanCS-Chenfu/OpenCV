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



def preprocesar_nube(pcd, voxel_size):
    
    # Reducir Tamaño (podría no hacerse)
    pcd_down = pcd.voxel_down_sample(voxel_size=voxel_size)
    
    # Calcular Normales (necesario)
    radius_normal = voxel_size * 2
    pcd_down.estimate_normals(search_param=o3d.geometry.KDTreeSearchParamHybrid(radius=radius_normal, max_nn=30))
    
    # fpfh (Fast Point Feature Histogram) describe la geometría local. Para cada punto calcula histogramas basados en
    # ángulos entre normales y distancias entre puntos
    radius_feature = voxel_size * 5
    pcd_fpfh = o3d.pipelines.registration.compute_fpfh_feature(pcd_down, o3d.geometry.KDTreeSearchParamHybrid(radius=radius_feature, max_nn=100))
    
    return pcd_down, pcd_fpfh



def aplicar_ruido(pcd, mu, sigma):
    noisy_pcd = copy.deepcopy(pcd)
    points = np.asarray(noisy_pcd.points)
    points += np.random.normal(mu, sigma, size=points.shape)
    
    noisy_pcd.points = o3d.utility.Vector3dVector(points)
    
    return noisy_pcd



def global_registration(source, target):
    
    source_down, source_fpfh = preprocesar_nube(source, 0.01)
    target_down, target_fpfh = preprocesar_nube(target, 0.01)
    
    mostrar_transformacion(source_down, target_down, np.identity(4))
    
    distance_threashold = 0.01 * 1.5    # Dice cuando un punto es considerado inlier
    
    # RANSAC (Random Sample Consensus) sirve para encontrar una transformación rígida (T) tal que: 
    # "target = R * source + t". Las correspondencias entre features pueden contener muchos outliers.
    # RANSAC lo resuelve probando muchas hipótesis:
    # Elegir correspondencias aleatorias -> estimar transformación -> aplicar transformación -> contar inliers ->
    # -> repetir miles de veces -> elegir la mejor transformación.
    resultado  = o3d.pipelines.registration.registration_ransac_based_on_feature_matching(
        source_down, target_down, source_fpfh, target_fpfh, True, distance_threashold,  # True: usar mutual filtering
        o3d.pipelines.registration.TransformationEstimationPointToPoint(False), 3,      # Función de Error: abs(R*p_i + t - q_i)^2. "3" puntos para hipótesis (se usan 3 correspondencias para estimar transformación).
        [
            o3d.pipelines.registration.CorrespondenceCheckerBasedOnEdgeLength(0.9),     # Comprueba que las distancias entre puntos no cambian mucho
            o3d.pipelines.registration.CorrespondenceCheckerBasedOnDistance(distance_threashold)    # Descarta correspondencias demasiado lejanas
        ],
        o3d.pipelines.registration.RANSACConvergenceCriteria(100000, 0.999)     # Criterio de Convergencia: 1000 iteraciones máximo y 99,9% de probabilidad de encontrar una solución correcta
    )
    
    print(resultado)
    mostrar_transformacion(source_down, target_down, resultado.transformation)
    
    return resultado
    
    

def refine_registration(source, target, resultado_global):
    
    source_down, source_fpfh = preprocesar_nube(source, 0.01)
    target_down, target_fpfh = preprocesar_nube(target, 0.01)
    
    mostrar_transformacion(source_down, target_down, np.identity(4))
    
    distance_threashold = 0.01 * 0.4
    
    # ICP para refinar la transformación inicial (RANSAC).
    # Point to Plane converge más rápido porque solo minimiza el error perpendicular a la superficie
    resultado  = o3d.pipelines.registration.registration_icp(
        source_down, target_down, distance_threashold, resultado_global.transformation,
        o3d.pipelines.registration.TransformationEstimationPointToPlane()   # Función de Error: abs((R*p_i + t - q_i)*nomral_target)^2.
    )
    
    print(resultado)
    mostrar_transformacion(source_down, target_down, resultado.transformation)
    
    
    
    
def fast_global_registration(source, target):
    
    source_down, source_fpfh = preprocesar_nube(source, 0.01)
    target_down, target_fpfh = preprocesar_nube(target, 0.01)
    
    mostrar_transformacion(source_down, target_down, np.identity(4))
    
    distance_threashold = 0.01 * 0.5
    
    # En vez de usar "RANSAC" (Random Sampling), se utiliza una optimización robusta (más rápida).
    # Función de Error: peso_i * abs(R*p_i + t - q_i)^2.
    resultado  = o3d.pipelines.registration.registration_fgr_based_on_feature_matching(
        source_down, target_down, source_fpfh, target_fpfh,
        o3d.pipelines.registration.FastGlobalRegistrationOption(maximum_correspondence_distance = distance_threashold)  # Distancia máxima entre correspondencias
    )

    print(resultado)
    mostrar_transformacion(source_down, target_down, resultado.transformation)

    return resultado


def robustICP(source, target):
    sigma = 0.01
    source_noise = aplicar_ruido(source, 0, sigma)
    
    mostrar_transformacion(source_noise, target, np.identity(4))
    
    voxel_size = 0.001
    source_down, source_fpfh = preprocesar_nube(source_noise, voxel_size)
    target_down, target_fpfh = preprocesar_nube(target, voxel_size)
    
    distance_threashold = 0.01 * 4
    
    # ICP normal (refine_registration)
    resultado_normal  = o3d.pipelines.registration.registration_icp(
        source_down, target_down, distance_threashold, np.identity(4),
        o3d.pipelines.registration.TransformationEstimationPointToPlane()  
    )
    
    print(resultado_normal.transformation)
    mostrar_transformacion(source_down, target_down, resultado_normal.transformation)
    
    # Robust ICP (me va peor que el ICP normal)
    loss = o3d.pipelines.registration.TukeyLoss(k = voxel_size*3)
    
    resultado_robusto  = o3d.pipelines.registration.registration_icp(
        source_down, target_down, distance_threashold, np.identity(4),
        o3d.pipelines.registration.TransformationEstimationPointToPlane(loss)  
    )
    
    print(resultado_robusto.transformation)
    mostrar_transformacion(source_down, target_down, resultado_robusto.transformation)
    
if __name__ == '__main__':
    
    source = o3d.io.read_point_cloud("./bunny/reconstruction/bun_zipper.ply")
    target = copy.deepcopy(source)
    
    T = np.array([[0.862, 0.011, -0.507, 0.005],
                  [-0.139, 0.967, -0.215, 0.007],
                  [0.487, 0.255, 0.835, -0.014],
                  [0.0, 0.0, 0.0, 1.0]])
    
    target.transform(T)
    
    
    #resultado_global = global_registration(source, target)
    
    #refine_registration(source, target, resultado_global)
    
    #resultado_global_fast = fast_global_registration(source, target)
    
    robustICP(source, target)