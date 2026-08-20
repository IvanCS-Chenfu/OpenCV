import open3d as o3d
pg=o3d.pipelines.registration.PoseGraph(); pg.nodes.append(o3d.pipelines.registration.PoseGraphNode()); print("Añade nodos y aristas a partir de registros consecutivos y cierres; luego usa global_optimization. Ver wiki.")
