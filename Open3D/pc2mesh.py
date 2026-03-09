import open3d as o3d
import numpy as np
import matplotlib.pyplot as plt

# Generalización del cerco convexo
def alpha_shapes(pcd):
    
    alpha = 0.03
    
    # Cada 4 puntos forman un tetraedro. Si la esfera circunscrita del tetraedro cumple (r < alpha), ese tetraedro se mantiene. Si no, se elimina.
    # Los triangulos exteriores de los tetraedros restantes forman la malla. Si "alpha" es infinito -> convex hull.
    mesh = o3d.geometry.TriangleMesh.create_from_point_cloud_alpha_shape(pcd, alpha)
    mesh.compute_vertex_normals()   # Mediante promediado de normales de los triangulos de alrededor
    
    o3d.visualization.draw_geometries([mesh, pcd], mesh_show_back_face=True)    # Muestra los triángulos por ambas caras

    # Calcula ciertas cosas para que no tengan que ser calculadas en cada iteración del bucle (no dependen de alpha)
    tetra_mesh, pt_map = o3d.geometry.TetraMesh.create_from_point_cloud(pcd)
    for alpha in np.logspace(np.log10(0.1), np.log10(0.001), num=4):
        print(alpha)
        
        mesh = o3d.geometry.TriangleMesh.create_from_point_cloud_alpha_shape(pcd, alpha, tetra_mesh, pt_map)
        mesh.compute_vertex_normals()
        o3d.visualization.draw_geometries([mesh, pcd], mesh_show_back_face=True)


# Se crea una bola de radio "r". Si esa bola toca 3 puntos, se crea un triángulo. Desde un triángulo ya encontrado, 
# se hace pivotar la bola alrededor de una arista buscando un tercer punto y creando otro triángulo.
def ball_pivoting(pcd):
    
    pcd.estimate_normals()  # Necesario para saber qué lado de la superficie es el exterior.
    
    radii = [0.005, 0.01, 0.02, 0.04]   # Se utilizan múltiples radios con el fin de abarcar triángulos grandes y pequeños
    
    mesh = o3d.geometry.TriangleMesh.create_from_point_cloud_ball_pivoting(pcd, o3d.utility.DoubleVector(radii))
    
    o3d.visualization.draw_geometries([mesh, pcd], mesh_show_back_face=True)
    
# Reconstruye una función implícita (X) que representa el volumen. Los puntos con normales representan el gradiente de dicha función.
# Se busca una función cuya divergencia coincida con ese campo. Se resuelve la ecuación de Poisson: Nabla^2 X = Nabla * Campo_Normales
def poisson(pcd):
    
    pcd.estimate_normals()
    pcd.orient_normals_consistent_tangent_plane(100)    # Orienta la normales de forma consistente (usando un grafo de vecinos)
    
    mesh, densities = o3d.geometry.TriangleMesh.create_from_point_cloud_poisson(pcd, depth=9)   # depth controla la resolución
    mesh.compute_vertex_normals()
    
    o3d.visualization.draw_geometries([mesh, pcd], mesh_show_back_face=True)
    
    densities = np.asarray(densities)   # Indica cuantos puntos de la nube original han contribuido en reconstruir esa zona de la superficie
    density_colors = plt.get_cmap("plasma")((densities-densities.min()) / (densities.max()-densities.min()))
    density_colors = density_colors[:,:3]
    
    density_mesh = o3d.geometry.TriangleMesh()
    density_mesh.vertices = mesh.vertices
    density_mesh.triangles = mesh.triangles
    density_mesh.triangle_normals = mesh.triangle_normals
    density_mesh.vertex_colors = o3d.utility.Vector3dVector(density_colors)
    
    o3d.visualization.draw_geometries([density_mesh])
    
    indice_remove = densities < np.quantile(densities, 0.01)
    mesh.remove_vertices_by_mask(indice_remove)
    
    o3d.visualization.draw_geometries([mesh])
    
    


if __name__ == '__main__':
    
    pcd = o3d.io.read_point_cloud("./bunny/reconstruction/bun_zipper.ply")
    
    #alpha_shapes(pcd)
    
    #ball_pivoting(pcd)
    
    poisson(pcd)