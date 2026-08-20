import open3d as o3d
import numpy as np
pts=np.random.default_rng(7).normal(size=(5000,3)); pc=o3d.geometry.PointCloud(o3d.utility.Vector3dVector(pts)); print(pc); o3d.io.write_point_cloud("output.ply",pc)
