import open3d as o3d
pc=o3d.io.read_point_cloud("input.ply"); down=pc.voxel_down_sample(0.02); clean,idx=down.remove_statistical_outlier(nb_neighbors=30,std_ratio=2.0); print(len(pc.points),len(down.points),len(clean.points)); o3d.io.write_point_cloud("clean.ply",clean)
