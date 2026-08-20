#include <open3d/Open3D.h>
int main(){ auto pc=open3d::io::CreatePointCloudFromFile("input.ply"); if(!pc) return 1; pc->EstimateNormals(); auto result=open3d::geometry::TriangleMesh::CreateFromPointCloudPoisson(*pc,9); auto mesh=std::get<0>(result); mesh->RemoveDegenerateTriangles(); open3d::io::WriteTriangleMesh("poisson.ply",*mesh); }
