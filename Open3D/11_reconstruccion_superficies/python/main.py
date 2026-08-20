import open3d as o3d
pc=o3d.io.read_point_cloud("input.ply"); pc.estimate_normals(); mesh,density=o3d.geometry.TriangleMesh.create_from_point_cloud_poisson(pc,depth=9); mesh.remove_degenerate_triangles(); o3d.io.write_triangle_mesh("poisson.ply",mesh)
