import open3d as o3d
import numpy as np

import matplotlib.pyplot as plt


def geometria_imagen(rgb, depth):
    
    # Los valores de escala y trunc son para saber que profundidad máxima hay
    rgbd = o3d.geometry.RGBDImage.create_from_color_and_depth(rgb,depth,depth_scale=1000.0, depth_trunc=10.0, convert_rgb_to_intensity=False)
    
    plt.figure()
    
    plt.subplot(1,2,1)
    plt.imshow(np.asarray(rgbd.color))
    plt.title("Color")
    
    plt.subplot(1,2,2)
    plt.imshow(np.asarray(rgbd.depth))
    plt.title("Profundidad")
    
    plt.show()
    
    # Esto se debería modificar dependiendo de la cámara
    intrinsics = o3d.camera.PinholeCameraIntrinsic(o3d.camera.PinholeCameraIntrinsicParameters.PrimeSenseDefault)
    
    pcd = o3d.geometry.PointCloud.create_from_rgbd_image(rgbd, intrinsics)
    
    pcd.transform([[1,0,0,0],[0,-1,0,0],[0,0,-1,0],[0,0,0,1]])  # Aplicar una matriz de transformación para girar el objeto
    o3d.visualization.draw_geometries([pcd])
    


if __name__ == '__main__':
    
    im_rgb = o3d.io.read_image("./RGB-D/rgb.png")
    im_depth = o3d.io.read_image("./RGB-D/depth.png")
    
    geometria_imagen(im_rgb, im_depth)