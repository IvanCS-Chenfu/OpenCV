import open3d as o3d, numpy as np
pc=o3d.io.read_point_cloud("input.ply"); T=np.eye(4); T[:3,3]=[0.2,0.0,0.1]; pc.transform(T); o3d.io.write_point_cloud("transformed.ply",pc)
