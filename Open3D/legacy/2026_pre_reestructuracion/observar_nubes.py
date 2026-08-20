import open3d as o3d
import numpy as np

print(o3d.__version__)
print(o3d.__file__)


pcd = o3d.io.read_point_cloud("./data-master/tutorials/room_scan2.pcd")
#pcd = o3d.io.read_point_cloud("./bunny/data/bun000.ply")

o3d.visualization.draw_geometries([pcd])



