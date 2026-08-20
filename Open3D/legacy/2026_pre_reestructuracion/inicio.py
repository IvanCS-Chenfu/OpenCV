# Voxel downsampling
# Hace un "grid 3D" y pone un punto en la posición media de todos los puntos de cada cubo (voxel)

import open3d as o3d
import numpy as np
import matplotlib.pyplot as plt

import copy

def editar(pcd):
    
    o3d.visualization.draw_geometries_with_editing([pcd])
    # K: Bloquear Cámara
    # ctrl + click izq: Seleccionar Puntos del Polígono
    # C: Crear volumen de Recorte
    # S: Guardar Selección (un json)
    # F: Volver al modo libre
    
    # Esto debería dar un json pero me da error


def recortar(pcd, flag_trasladar):

    json_recorte = o3d.visualization.read_selection_polygon_volume("path_json.json")
    pcd_recortado = json_recorte.crop_point_cloud(pcd)

    
def colorear(pcd):
    # Pintar en Rojo
    pcd.paint_uniform_color([1,0,0])        
    
    o3d.visualization.draw_geometries([pcd])


def bounding_box(pcd):
    # Máximos y mínimos en cada eje (X,)
    bounding_box_alineada = pcd.get_axis_aligned_bounding_box()
    bounding_box_alineada.color = (1,0,0)
    
    # Orientada en dirección de mayor distancia
    bounding_box_orientada = pcd.get_oriented_bounding_box()
    bounding_box_orientada.color = (0,1,0)
    
    o3d.visualization.draw_geometries([pcd, bounding_box_alineada, bounding_box_orientada])
    
    
def distancia(pcd):
    # Obtener el ancho de la boundin box
    bounding_box = pcd.get_axis_aligned_bounding_box()
    ancho = bounding_box.get_extent()[0]
    
    # Trasladar la copia
    pcd_copy = copy.deepcopy(pcd)
    pcd_copy.translate([ancho*1.2, 0, 0])
    
    # Devuelve la distancia de cada punto de "pcd" al punto más cercano de "pcd_copy"
    distancias = pcd.compute_point_cloud_distance(pcd_copy)
    distancias = np.asarray(distancias)
    indices_distancias = np.where(distancias > 0.1)[0]
    
    # De "pcd" solo obtiene los puntos que estén a más de 0.1 de "pcd_copy"
    pcd_distancias = pcd.select_by_index(indices_distancias)
    
    pcd.paint_uniform_color([1,0,0])
    pcd_copy.paint_uniform_color([0,1,0])
    pcd_distancias.paint_uniform_color([0,0,1])
    
    o3d.visualization.draw_geometries([pcd, pcd_copy, pcd_distancias])
    
    print(max(distancia))
    print(ancho*1.2)
    
    
def cerco_convexo(pcd):
    covex_hull, _ = pcd.compute_convex_hull()   # Devuelve un conjunto de mallas traingulares
    print(covex_hull)
    hull_ls = o3d.geometry.LineSet.create_from_triangle_mesh(covex_hull)    # Devuelve las lineas que forman los triangulos de las mallas
    print(hull_ls)
    
    pcd.paint_uniform_color([1,0,0])
    covex_hull.paint_uniform_color([0,1,0])
    hull_ls.paint_uniform_color([0,0,1])
    
    o3d.visualization.draw_geometries([pcd, covex_hull, hull_ls])
    

def plano(pcd):
    # Por minimos cuadrados calcula los coeficientes del plano que más se aproxima a la nube de puntos.
    # También devuelve los índices de los puntos que están cerca del plano (dentro del umbral)
    coefs_plano, inliers = pcd.segment_plane(distance_threshold=0.01,ransac_n=3,num_iterations=1000)
    
    [a,b,c,d] = coefs_plano
    print(f"Ecuación del Plano: {a:.2f}x + {b:.2f}y + {c:.2f}z + {d:.2f} = 0")
    
    pcd_inliers = pcd.select_by_index(inliers)
    pcd_outliers = pcd.select_by_index(inliers, invert=True)
    
    pcd.paint_uniform_color([1,0,0])
    pcd_inliers.paint_uniform_color([0,1,0])
    pcd_outliers.paint_uniform_color([0,0,1])
    
    o3d.visualization.draw_geometries([pcd, pcd_inliers, pcd_outliers])
    

def eliminar_puntos_escondidos(pcd):
    # Distancia diagonal de la nube de puntos
    diametro = np.linalg.norm(np.asarray(pcd.get_max_bound())-np.asarray(pcd.get_min_bound()))
    
    # Parámetros del algoritmo
    camara = [0, -diametro, 0]  # Posición de la cámara (si hubiese una cámara en dicha posición, ciertos puntos no se verían)
    radio = diametro * 1000     # Radio desde la posición de la cámara hasta donde la cámara ve puntos
    
    _, indices_no_escondidos = pcd.hidden_point_removal(camara, radio)
    pcd_no_escondidos = pcd.select_by_index(indices_no_escondidos)
    
    o3d.visualization.draw_geometries([pcd_no_escondidos])
    
    pcd.paint_uniform_color([1,0,0])
    pcd_no_escondidos.paint_uniform_color([0,1,0])
    
    o3d.visualization.draw_geometries([pcd, pcd_no_escondidos])



def DBscan(pcd):
    # Pone el "VerbosityLevel" a "Debug" solo en el comando de abajo "cluster_dbscan"
    # con el fin de mostrar mensajes detallados de lo que ocurre 
    with o3d.utility.VerbosityContextManager(o3d.utility.VerbosityLevel.Debug) as cm:
        # crea un vector del tamaño de puntos de "pcd". A cada punto le da una etiqueta (-1 si no está en un cluster)
        labels = np.array(pcd.cluster_dbscan(eps=0.05, min_points=10, print_progress=True))
        
    max_label = labels.max()
    print("La nube de puntos tiene", max_label+1, "clusteres.")
    
    # Crea un vector de colores y aquellos colores que no esten en un cluster dado por DBscan (labels<0) no les da color
    vector_colores = plt.get_cmap("tab20")(labels / (max_label if max_label > 0 else 1))
    vector_colores[labels<0] = 0
    
    # Le da a los puntos el color según el cluster en el que estén
    pcd.colors = o3d.utility.Vector3dVector(vector_colores[:,:3])
    
    o3d.visualization.draw_geometries([pcd])
        
if __name__ == '__main__':
    
    pcd = o3d.io.read_point_cloud("./bunny/reconstruction/bun_zipper.ply")
    
    #editar(pcd)
    
    #recortar(pcd, False)
    
    #colorear(pcd)
    
    #bounding_box(pcd)
    
    #distancia(pcd)
    
    #cerco_convexo(pcd)
    
    #plano(pcd)
    
    pcd = o3d.io.read_point_cloud("./nube.ply")
    eliminar_puntos_escondidos(pcd)
        
    pcd = o3d.io.read_point_cloud("./data-master/tutorials/room_scan2.pcd")
    #DBscan(pcd)