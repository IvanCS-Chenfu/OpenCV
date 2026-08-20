import open3d as o3d
mesh=o3d.io.read_triangle_mesh("mesh.ply"); mesh.compute_vertex_normals(); p=mesh.sample_points_poisson_disk(5000); o3d.io.write_point_cloud("sampled.ply",p)
