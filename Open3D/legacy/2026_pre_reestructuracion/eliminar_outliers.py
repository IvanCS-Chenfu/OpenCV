import open3d as o3d
import numpy as np

def mostrar_inliers_outliers(pcd, indices_inliers):
    pcd_inliers = pcd.select_by_index(indices_inliers)
    pcd_outliers = pcd.select_by_index(indices_inliers, invert=True)
    
    pcd_inliers.paint_uniform_color([0,1,0])
    pcd_outliers.paint_uniform_color([1,0,0])
    
    o3d.visualization.draw_geometries([pcd_inliers, pcd_outliers])


def statical_outlier(pcd):
    pcd = pcd.voxel_down_sample(voxel_size=0.01)
    
    # Para cada punto se calcula la distancia media a los "k" vecinos más cercanos.
    # Ese punto se elimina si: (media > media_global + std_ratio * desviación_típica_global)
    cl, ind = pcd.remove_statistical_outlier(nb_neighbors = 15, std_ratio = 1.0)
    
    mostrar_inliers_outliers(pcd, ind)
    
    
def radius_outlier(pcd):
    pcd = pcd.voxel_down_sample(voxel_size=0.01)
    
    # Si dentro de un radio no hay más de "nb_points", este punto se elimina
    cl, ind = pcd.remove_radius_outlier(nb_points = 15, radius = 0.02)
    
    mostrar_inliers_outliers(pcd, ind)
    


if __name__ == '__main__':
    
    pcd = o3d.io.read_point_cloud("./bunny/reconstruction/bun_zipper.ply")
    
    statical_outlier(pcd)
    
    radius_outlier(pcd)