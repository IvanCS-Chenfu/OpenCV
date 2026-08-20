import open3d as o3d, numpy as np
s=o3d.io.read_point_cloud("source.ply"); t=o3d.io.read_point_cloud("target.ply"); threshold=0.05; result=o3d.pipelines.registration.registration_icp(s,t,threshold,np.eye(4),o3d.pipelines.registration.TransformationEstimationPointToPoint()); print(result); print(result.transformation)
