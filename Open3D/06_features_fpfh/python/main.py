import open3d as o3d
pc=o3d.io.read_point_cloud("input.ply").voxel_down_sample(0.03); pc.estimate_normals(o3d.geometry.KDTreeSearchParamHybrid(radius=0.06,max_nn=30)); f=o3d.pipelines.registration.compute_fpfh_feature(pc,o3d.geometry.KDTreeSearchParamHybrid(radius=0.15,max_nn=100)); print(f.data.shape)
