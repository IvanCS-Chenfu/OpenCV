import open3d as o3d, numpy as np
s=o3d.io.read_point_cloud("source.ply"); t=o3d.io.read_point_cloud("target.ply");
for p in (s,t): p.estimate_normals(o3d.geometry.KDTreeSearchParamHybrid(radius=0.05,max_nn=30))
r=o3d.pipelines.registration.registration_colored_icp(s,t,0.05,np.eye(4)); print(r.transformation)
