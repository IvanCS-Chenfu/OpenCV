import open3d as o3d
pc=o3d.io.read_point_cloud("input.ply"); pc.estimate_normals(o3d.geometry.KDTreeSearchParamHybrid(radius=0.05,max_nn=30)); pc.orient_normals_consistent_tangent_plane(20); o3d.io.write_point_cloud("normals.ply",pc)
